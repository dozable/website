---
title: "Dozable 0.37 - sessions on this Mac — Dozable blog"
description: "Dozable 0.37 holds sessions on this Mac for work a Linux sandbox cannot do, and adds Claude Code with local models, your own recipes, and dotfiles in every sandbox."
date: 2026-11-13
topics: [release-news]
url: https://dozable.com/blog/doz-v0.37
image: https://dozable.com/og-image.png
source: "Dozable blog"
---
# Dozable 0.37 - sessions on this Mac

*13 November 2026 · Release news*

It's on the [stable channel](https://dozable.com/docs/install-upgrade-uninstall) now, as 0.37.46, and
includes everything since 0.35.

## Sessions on this Mac

Dozable holds [terminal sessions on this Mac](https://dozable.com/docs/sessions-on-this-mac), for work a Linux sandbox cannot do: Swift,
Xcode, signing and notarisation. A session runs as you: your files, Keychain and network,
with no sandbox and no proxy.

The dashboard's **This Mac** page lists them. Opening a session starts read-only; **Type into
it** switches to typing. Start one with `doz run @mac`; other devices see none of this by
default.

## Claude Code with other models

[Claude Code can use](https://dozable.com/docs/claude-code-other-models) a model server on this Mac (Ollama, LM Studio or oMLX), OpenRouter's
Anthropic endpoint, or Anthropic as before. The proxy lets that sandbox reach only the port
you chose.

## Recipes and dotfiles

You can add [your own recipe](https://dozable.com/docs/your-own-recipes) with `doz recipe new` or `doz recipe add`, and a signed community
catalogue with `doz recipe source add`. A sandbox can use [your dotfiles](https://dozable.com/docs/dotfiles) from a git repository
or a folder on this Mac: fetched on the Mac, applied as the image's user, and never
overwriting an existing file.

## Also new

- Claude Code keeps its conversations, instead of deleting them after 30 days. A cleanup
  period you already set is left alone.
- A sandbox's **Files** tab shows `/workspace` as a live, editable tree. **Open folder**
  opens it in the Finder or an editor on this Mac (`doz files open`).
- `doz sessions send` types into a session from a script; `doz sessions screen` prints the
  screen as it is now. Both work on a sandbox's sessions too.
- Dozable offers Claude Code, Codex, pi and OpenCode (1 and 2), with OpenRouter as the
  gateway. The other tools, and Vercel AI Gateway, are unpublished for now and return in a
  later release; sandboxes already made with them keep working.

## Fixed

- A busy sandbox is no longer starved of memory after a wake, and one unresponsive sandbox
  can no longer hang `doz ls`.
- A sandbox that stopped answering is shown as "not answering".

## Upgrade

0.37 starts fresh: settings, the store and caches live in new `doz` folders, and nothing is
migrated from the earlier paths. The [install and upgrade](https://dozable.com/docs/install-upgrade-uninstall)
page says what to do before and after. If you are upgrading from 0.35, trust the Homebrew
tap once, then upgrade:

```sh
brew trust --tap dozable/tap
doz upgrade
```

Then try a session on this Mac, or Claude Code with a local model.
