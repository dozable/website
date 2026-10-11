#!/usr/bin/env python3
"""tools/markdown-build.py — the Markdown twins of the root pages, and /llms.txt and /llms-full.txt.

Every page of the site has a Markdown twin at its URL + .md, for agents (llms.txt convention; a Cloudflare rule can serve
them to `Accept: text/markdown`). This tool writes the ones docs-build.py and blog-build.py do not:

  index.html.md      the home page            timeline.html.md   the timeline
  privacy.md         the privacy policy       signup.md          how to sign up (no form: it needs a browser)
  llms.txt           an index for agents (https://llmstxt.org)
  llms-full.txt      the whole manual (every docs twin, in reading order) and the privacy policy in one file

The root-page twins are generated from the published HTML (so the text cannot drift from the page): a small
HTML-to-Markdown converter with the rules this site's markup needs, links made absolute and pointed at the twins. It also
makes sure each root page's <head> carries <link rel="alternate" type="text/markdown"> (docs and blog pages get theirs
from their own builders). Stdlib only, deterministic. Run it AFTER tools/docs-build.py and tools/blog-build.py (llms.txt
reads their twins), BEFORE tools/stamp.sh. Never edit a twin by hand."""
import html, json, os, re, sys
from html.parser import HTMLParser

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://dozersandbox.com/'
REPO = 'https://github.com/dozer-sandbox/dozer-sandbox'
ROOT_PAGES = [  # (source html, twin file, canonical url)
    ('index.html', 'index.html.md', BASE),
    ('timeline.html', 'timeline.html.md', BASE + 'timeline.html'),
    ('privacy.html', 'privacy.md', BASE + 'privacy'),
    ('signup.html', 'signup.md', BASE + 'signup'),
]


class BuildError(Exception):
    pass


def to_twin(url):
    """A site URL -> its Markdown twin; anything else unchanged."""
    m = re.match(r'^https://dozersandbox\.com(/[^#]*)?(#.*)?$', url)
    if not m:
        return url
    path, frag = m.group(1) or '/', m.group(2) or ''
    if path == '/':
        path = '/index.html.md'
    elif path.endswith('/'):
        path = path + ('index.md' if path.startswith('/blog/') else 'index.html.md')
    elif path.endswith('.html'):
        path += '.md'
    elif path in ('/privacy', '/signup') or path.startswith('/blog/') and '.' not in path.rsplit('/', 1)[1]:
        path += '.md'
    return BASE.rstrip('/') + path + frag


# ------------------------------------------------------------------------------------------------ HTML -> Markdown
SKIP = {'script', 'style', 'svg', 'nav', 'header', 'footer', 'form', 'noscript', 'button', 'template', 'head', 'title',
        'select', 'textarea', 'input', 'label', 'caption'}
BLOCK = {'p', 'div', 'section', 'article', 'main', 'li', 'ul', 'ol', 'table', 'tr', 'figure', 'figcaption', 'h1', 'h2',
         'h3', 'h4', 'h5', 'h6', 'pre', 'blockquote', 'details', 'summary', 'aside', 'hr', 'body', 'time', 'thead',
         'tbody', 'dl', 'dt', 'dd'}


class Conv(HTMLParser):
    """The markup this site uses: headings, paragraphs, lists, tables, code, links, images, figures. Elements that are
    page furniture (header, nav, footer, forms, scripts, svg, buttons) are dropped; `.term` (the rolling command list)
    is replaced by the real command list; aria-hidden and visually hidden text rules keep tables readable."""

    def __init__(self, page_url, term_block=''):
        super().__init__(convert_charrefs=True)
        self.page_url, self.term_block = page_url, term_block
        self.out = []           # finished blocks
        self.buf = []           # the current inline run
        self.stack = []         # (tag, attrs, extra)
        self.skip = 0
        self.skip_tag = None
        self.lists = []         # ('ul'|'ol', counter)
        self.table = None
        self.pre = None
        self.href = []
        self.figcap = None

    # ---- helpers
    def absurl(self, u):
        if not u or u.startswith(('mailto:', 'javascript:')):
            return u
        if u.startswith('#'):
            return self.page_url + u
        if re.match(r'^https?:', u):
            return to_twin(u)
        base = self.page_url
        if not base.endswith('/'):
            base = base.rsplit('/', 1)[0] + '/'
        path, _, frag = u.partition('#')
        parts = (base + path).split('/')
        stack = []
        for seg in parts[3:]:
            if seg == '..':
                if stack:
                    stack.pop()
            elif seg not in ('.', ''):
                stack.append(seg)
        url = BASE + '/'.join(stack) + ('/' if path.endswith('/') or not path else '')
        if path in ('', './'):
            url = base
        return to_twin(url + ('#' + frag if frag else ''))

    def flush(self):
        text = ''.join(self.buf)
        self.buf = []
        text = re.sub(r'[ \t\r\n ]+', ' ', text).strip()
        text = re.sub(r'\s+(\.(?=\s|$)|[,;:!?)])', r'\1', text)
        text = text.replace('****', '** **')
        text = re.sub(r'\*\*(\S[^*]*?)\*\*(?=[A-Za-z0-9`(])', r'**\1** ', text)
        return text

    def emit(self, text, prefix=''):
        if text:
            self.out.append(prefix + text)

    def end_block(self):
        text = self.flush()
        if not text:
            return
        if self.table is not None:
            self.table['cell'].append(text)
            return
        prefix = ''
        li = next((e for e in reversed(self.stack) if e[0] in ('li', 'ul', 'ol')), None)
        if self.lists and li is not None and li[0] == 'li':
            kind, n = self.lists[-1]
            indent = '  ' * (len(self.lists) - 1)
            if li[2].get('transparent'):
                prefix = ''
            elif not li[2].get('marked'):
                li[2]['marked'] = True
                if kind == 'ol':
                    self.lists[-1] = (kind, n + 1)
                    prefix = '%s%d. ' % (indent, n + 1)
                else:
                    prefix = indent + '- '
            else:
                prefix = indent + '  '
        elif self.figcap is not None and self.stack and self.stack[-1][0] == 'figcaption':
            text = '*%s*' % text
        self.emit(text, prefix)

    # ---- parser callbacks
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get('class', '')
        if self.skip:
            if tag not in ('br', 'img', 'hr', 'input', 'meta', 'link'):
                self.skip += 1
            return
        if tag in SKIP or a.get('aria-hidden') == 'true' or 'sr' in cls.split() and tag == 'caption' or \
                'eyebrow' in cls.split() or 'toc' in cls.split() or 'chapters' in cls.split() or 'carousel-ui' in cls.split() or 'skip' in cls.split():
            self.skip = 1
            return
        if 'term' in cls.split() and tag == 'div':
            self.end_block()
            self.out.append(self.term_block)
            self.skip = 1
            return
        if tag == 'section' or tag == 'article':
            self.end_block()
        extra = {}
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self.end_block()
        elif tag == 'p' or tag == 'figure' or tag == 'div' or tag == 'blockquote' or tag == 'aside' or tag == 'time':
            self.end_block()
        elif tag == 'br':
            self.buf.append(' ')
        elif tag in ('ul', 'ol'):
            self.end_block()
            self.lists.append((tag, 0))
        elif tag == 'li':
            self.end_block()
            if 'event' in cls.split():
                extra['transparent'] = True
        elif tag == 'pre':
            self.end_block()
            self.pre = []
        elif tag == 'code' and self.pre is None:
            self.buf.append('`')
        elif tag in ('strong', 'b'):
            self.buf.append('**')
        elif tag in ('em', 'i'):
            self.buf.append('*')
        elif tag == 'a':
            self.href.append(self.absurl(a.get('href', '')))
            self.buf.append('[')
        elif tag == 'img':
            alt = a.get('alt', '')
            src = self.absurl(a.get('src', ''))
            self.end_block()
            self.emit('![%s](%s)' % (alt, src))
        elif tag == 'table':
            self.end_block()
            self.table = {'rows': [], 'row': None, 'cell': None, 'head': False}
        elif tag == 'tr' and self.table is not None:
            self.table['row'] = []
        elif tag in ('td', 'th') and self.table is not None:
            self.table['cell'] = []
            if tag == 'th':
                self.table['head'] = True
        elif tag == 'figcaption':
            self.end_block()
            self.figcap = True
        self.stack.append((tag, a, extra))

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1
            return
        # pop to the matching tag
        k = len(self.stack) - 1
        while k >= 0 and self.stack[k][0] != tag:
            k -= 1
        if k < 0:
            return
        del self.stack[k + 1:]
        if tag == 'li':
            self.end_block()
        _, a, extra = self.stack.pop()
        if tag in ('h1', 'h2', 'h3', 'h4'):
            text = self.flush()
            self.emit(text, '#' * int(tag[1]) + ' ')
        elif tag in ('p', 'div', 'blockquote', 'figure', 'aside', 'time', 'section', 'article', 'figcaption'):
            if tag == 'time':
                text = self.flush()
                self.emit('**%s**' % text if text else '')
            else:
                self.end_block()
            if tag == 'figcaption':
                self.figcap = None
        elif tag == 'li':
            if extra.get('transparent'):
                self.end_block()
            else:
                self.end_block()
        elif tag in ('ul', 'ol'):
            self.end_block()
            if self.lists:
                self.lists.pop()
            self.out.append('')
        elif tag == 'pre':
            text = ''.join(self.pre).strip('\n')
            self.pre = None
            self.out.append('```\n%s\n```' % text)
        elif tag == 'code' and self.pre is None:
            self.buf.append('`')
        elif tag in ('strong', 'b'):
            self.buf.append('**')
            self.buf.append('')
        elif tag in ('em', 'i'):
            self.buf.append('*')
        elif tag == 'a':
            self.buf.append('](%s)' % (self.href.pop() if self.href else ''))
        elif tag in ('td', 'th') and self.table is not None:
            cell = ' '.join(self.table['cell'] or []) + self.flush()
            self.table['row'].append(cell.replace('|', '\\|').strip())
            self.table['cell'] = None
        elif tag == 'tr' and self.table is not None and self.table['row'] is not None:
            self.table['rows'].append((self.table['row'], self.table['head']))
            self.table['row'] = None
            self.table['head'] = False
        elif tag == 'table' and self.table is not None:
            rows = self.table['rows']
            self.table = None
            if rows:
                width = max(len(r) for r, _ in rows)
                lines = []
                for i, (r, _) in enumerate(rows):
                    r = r + [''] * (width - len(r))
                    lines.append('| ' + ' | '.join(r) + ' |')
                    if i == 0:
                        lines.append('|' + '---|' * width)
                self.out.append('\n'.join(lines))
        elif tag in ('span',):
            self.buf.append(' ')

    def handle_data(self, data):
        if self.skip:
            return
        if self.pre is not None:
            self.pre.append(data)
        else:
            self.buf.append(data)

    def markdown(self):
        self.end_block()
        text = '\n\n'.join(b for b in self.out)
        text = re.sub(r'\n{3,}', '\n\n', text)
        # a list block's items are single lines: tighten consecutive items
        pat = re.compile(r'(\n[ ]*(?:- |\d+\. )[^\n]*)\n\n(?=[ ]*(?:- |\d+\. ))')
        while pat.search(text):
            text = pat.sub(r'\1\n', text)
        return text.strip() + '\n'


def convert(html_text, page_url, term_block=''):
    body = html_text[html_text.index('<body'):] if '<body' in html_text else html_text
    c = Conv(page_url, term_block)
    c.feed(body)
    return c.markdown()


def read(path):
    with open(os.path.join(SITE, path), encoding='utf-8') as f:
        return f.read()


def write(path, text):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full) or SITE, exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(text)


def meta(page_html, key):
    m = re.search(r'<meta (?:name|property)="%s" content="([^"]*)"' % re.escape(key), page_html)
    return html.unescape(m.group(1)) if m else ''


def front(title, description, url, **extra):
    lines = ['---', 'title: %s' % json.dumps(title, ensure_ascii=False),
             'description: %s' % json.dumps(description, ensure_ascii=False), 'url: %s' % url,
             'image: %sog-image.png' % BASE]
    lines += ['%s: %s' % (k, v) for k, v in extra.items()]
    return '\n'.join(lines + ['---', ''])


def term_block():
    cmds = json.load(open(os.path.join(SITE, 'cli-commands.json'), encoding='utf-8'))
    return '\n'.join('- `%s` — %s ([manual](%s))' % (c['cmd'], c['desc'], to_twin(c['manual'])) for c in cmds)


def alternates(canonical_page, md_url):
    """Make sure a root page's <head> links its Markdown twin."""
    s = read(canonical_page)
    s = re.sub(r'<link rel="alternate" type="text/markdown"[^>]*>\n?', '', s)
    link = '<link rel="alternate" type="text/markdown" href="%s">\n' % md_url
    m = re.search(r'<link rel="canonical"[^>]*>\n', s)
    if m:
        s = s[:m.end()] + link + s[m.end():]
    else:
        m = re.search(r'</title>\n', s)
        s = s[:m.end()] + link + s[m.end():]
    write(canonical_page, s)


def signup_twin():
    page = read('signup.html')
    intro = convert(page, BASE + 'signup')
    topics = re.findall(r'<input type="checkbox" name="interests" value="([a-z-]+)"><span><b>([^<]*)</b><small>([^<]*)</small>',
                        page)
    if len(topics) < 3:
        raise BuildError('signup.html: the three topic checkboxes were not found')
    lines = [intro.rstrip('\n'), '', '## How to sign up', '',
             'The sign-up form needs a browser. Choose one:', '',
             '- Open <https://dozersandbox.com/signup> in a browser, enter an email address and tick at least one topic. '
             'The same form is at the end of the home page.',
             '- Or, in Terminal: `doz signup`.', '',
             'We send a confirmation email first; nothing else is sent until you click its link. Every email has a '
             'one-click unsubscribe link. See the [privacy policy](%sprivacy.md).' % BASE, '', '## Topics', '']
    lines += ['- **%s** (`%s`) — %s' % (html.unescape(b), v, html.unescape(d)) for v, b, d in topics]
    return '\n'.join(lines) + '\n'


def main():
    out = {}
    tb = term_block()
    for src, twin, url in ROOT_PAGES:
        page = read(src)
        title, desc = html.unescape(re.search(r'<title>(.*?)</title>', page, re.S).group(1)), meta(page, 'description')
        if src == 'signup.html':
            body = signup_twin()
        else:
            body = convert(page, url, tb if src == 'index.html' else '')
        extra = {}
        if src == 'privacy.html':
            m = re.search(r'Last updated:\s*(\d{1,2}) (\w+) (\d{4})', re.sub(r'<[^>]+>', '', page))
            if m:
                months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                          'October', 'November', 'December']
                extra['updated'] = '%s-%02d-%02d' % (m.group(3), months.index(m.group(2)) + 1, int(m.group(1)))
        out[twin] = front(title, desc, url, **extra) + body
    for twin, text in out.items():
        write(twin, text)
    for src, twin, url in ROOT_PAGES:
        alternates(src, BASE + twin)
    if os.path.exists(os.path.join(SITE, 'DESIGN.html')):
        alternates('DESIGN.html', BASE + 'DESIGN.md')
    llms(out)
    print('markdown-build: %d root twins, llms.txt (%d bytes), llms-full.txt (%d bytes)'
          % (len(out), os.path.getsize(os.path.join(SITE, 'llms.txt')), os.path.getsize(os.path.join(SITE, 'llms-full.txt'))))
    print('  now run tools/stamp.sh')


# ------------------------------------------------------------------------------------------------------ llms files
def parse_front(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    fm = {}
    for line in m.group(1).split('\n'):
        k, _, v = line.partition(': ')
        v = v.strip()
        if v.startswith('"'):
            v = json.loads(v)
        fm[k] = v
    return fm, text[m.end():]


def chapter_title(body):
    return re.match(r'^# (.*)$', body, re.M).group(1).strip()


def llms(root):
    docs = []
    for f in sorted(os.listdir(os.path.join(SITE, 'docs'))):
        if f.endswith('.html.md') and f != 'index.html.md':
            fm, body = parse_front(read('docs/' + f))
            docs.append((int(fm['chapter']), f, fm, body))
    docs.sort(key=lambda d: d[0])
    index_fm, _ = parse_front(read('docs/index.html.md'))
    posts = []
    for f in sorted(os.listdir(os.path.join(SITE, 'blog'))) if os.path.isdir(os.path.join(SITE, 'blog')) else []:
        if f.endswith('.md') and f != 'index.md':
            fm, body = parse_front(read('blog/' + f))
            posts.append((fm.get('date', ''), f, fm))
    posts.sort(reverse=True)
    home = read('index.html')
    lede = re.search(r'<p class="lede[^"]*">(.*?)</p>', home, re.S)
    summary = html.unescape(re.sub(r'<[^>]+>', '', lede.group(1))).strip() if lede else ''
    L = ['# Dozer Sandbox', '', '> %s' % summary, '', index_fm['description'], '',
         'Pages have Markdown twins: add `.md` to a page URL (docs pages: `.html.md`).', '', '## Docs', '']
    for _, f, fm, body in docs:
        L.append('- [%s](%sdocs/%s): %s' % (chapter_title(body), BASE, f, fm['description']))
    L += ['- [The manual — contents](%sdocs/index.html.md): every chapter in reading order.' % BASE, '', '## Blog', '',
          '- [Blog index](%sblog/index.md): news, early access, tips and tricks.' % BASE]
    for _, f, fm in posts:
        L.append('- [%s](%sblog/%s): %s' % (fm['title'].replace(' — Dozer Sandbox blog', ''), BASE, f, fm['description']))
    L += ['', '## Site', '',
          '- [Home](%sindex.html.md): what Dozer Sandbox is, speed, the CLI, the web UI, a comparison, install.' % BASE,
          '- [Timeline](%stimeline.html.md): how Dozer Sandbox was built, release by release.' % BASE,
          '- [Privacy policy](%sprivacy.md): what is collected, why, and how to turn it off.' % BASE,
          '- [Sign up](%ssignup.md): release news, early access and tips and tricks by email.' % BASE, '',
          '## Optional', '',
          '- [llms-full.txt](%sllms-full.txt): the whole manual and the privacy policy in one file.' % BASE,
          '- [Source code](%s): the GitHub repository (MIT licence).' % REPO,
          '- [Releases](%s/releases): every version, with notes.' % REPO,
          '- [Blog feed](%sblog/feed.xml): Atom.' % BASE, '- [Sitemap](%ssitemap.xml)' % BASE]
    write('llms.txt', '\n'.join(L) + '\n')
    F = ['# Dozer Sandbox — the manual and privacy policy', '', '> %s' % summary, '',
         'The complete user manual (every chapter, in reading order) followed by the privacy policy. Each part starts '
         'with the URL of its page.', '']
    for _, f, fm, body in docs:
        F += ['---', '', 'URL: %s' % fm['url'], '', body.strip('\n'), '']
    pfm, pbody = parse_front(root['privacy.md'])
    F += ['---', '', 'URL: %sprivacy' % BASE, '', pbody.strip('\n'), '']
    write('llms-full.txt', '\n'.join(F))


if __name__ == '__main__':
    try:
        main()
    except BuildError as e:
        print('markdown-build: FAILED: %s' % e, file=sys.stderr)
        sys.exit(1)
