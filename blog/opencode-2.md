---
title: "OpenCode 2 is in Dozer Sandbox — Dozable blog"
description: "OpenCode 2, a rebuild of the open-source coding agent around one shared background service, now runs in Dozer Sandbox beside OpenCode 1, on your own key or OpenCode Zen's free models."
date: 2026-10-17
topics: [tool-news]
url: https://dozersandbox.com/blog/opencode-2
image: https://dozersandbox.com/og-image.png
source: "Dozable blog"
---
# OpenCode 2 is in Dozer Sandbox

*17 October 2026 · Tool news*

OpenCode 2 is out, and you can try it in a sandbox with one command. OpenCode 1 stays available, so a project that
depends on it keeps working.

```sh
doz try opencode        # OpenCode 2, in a throwaway sandbox
doz try opencode@1      # OpenCode 1
```

It needs Dozer Sandbox 0.35, now on the [stable channel](https://dozersandbox.com/docs/install-upgrade-uninstall.html).

In the dashboard, OpenCode's card in Quick try has a **Version** choice; it starts on 2. Sandboxes you already have
stay on the version they were made with.

## What's new in OpenCode 2

Anomaly, the company behind OpenCode, announced 2.0 on 12 October as "a major overhaul"
([their post](https://anoma.ly/notes/opencode-2-0/)), about three months after its public beta. Its changelog has
moved to the 2.x series, so 2 is now OpenCode's main release
([The New Stack](https://thenewstack.io/opencode-2-shared-service/) has a good account of the release).

- **One service, several interfaces.** OpenCode now starts a single background service. The terminal interface,
  the web app and the desktop app all talk to it, so you can start a session in the terminal and continue it in the
  browser. Your own scripts can find and use the same service.
- **A new API that lets the agent manage itself.** The agent can create a git worktree for a new task, move a
  session into it, or find and interrupt a session that is stuck. Scripts reach the API through `@opencode/client`;
  `@opencode/sdk` embeds OpenCode in your own application ([SDK docs](https://opencode.ai/v2/docs/build/sdk)).
- **Code Mode.** Instead of one tool call per round trip to the model, the agent writes a short JavaScript program
  that calls several MCP tools or APIs and works with the results, for example reading bug reports from one service
  and filing issues in another. It is the default for every MCP server.
- **Work in the background.** Subagents and shell commands can run while you keep working with the main agent: a
  code review by a subagent on another model, or a long test run that reports back when it finishes. A shortcut
  (ctrl+b) moves a running task to the background.
- **Plugins.** More than 80 of its own features are now plugins, terminal-interface plugins are stable, and plugins
  hot-reload, so OpenCode can write a plugin and use it in the same session
  ([how they rebuilt it](https://anoma.ly/notes/opencode-reloaded/)).

**What breaks:** plugins written for OpenCode 1 don't load in 2, and integrations built on the old server API need
updating.

## In Dozer

OpenCode 2 gets what every tool in Dozer gets:

- **Your key stays on your Mac.** Use a key from xAI, OpenAI, Anthropic, OpenRouter or Vercel AI Gateway; the
  sandbox only ever holds a placeholder. OpenCode Zen's free models take no key at all.
- **A locked network** that reaches its model and nothing else, and a folder of its own. OpenCode 2's background
  service runs inside the sandbox and needs nothing more.
- **A guide beside the try** with the first commands to run.
- **Its web app on your Mac:** run `opencode pair` in the sandbox and open the link it prints, or use the sandbox's
  **Open** button; it shows in your browser, on this Mac only.


Outside Dozer, OpenCode 1 users move with `opencode upgrade --major` or `/update`; since 1.19 it no longer updates
itself ([1.19.0 release notes](https://github.com/anomalyco/opencode/releases/tag/v1.19.0)). In Dozer you choose the
version by name instead, and the sandbox's version comes from Dozer's checked recipe.

## Ways to try it

OpenCode Zen's free models need no account and no key. The picker and `doz models --provider opencode-zen` show each
model's data terms; some may use what you send to improve their models.

```sh
doz try opencode --provider opencode-zen          # Big Pickle, free, no key
```

Or your own key from xAI, OpenAI or Anthropic, or one key for many models through OpenRouter or Vercel AI Gateway:

```sh
doz try opencode                                  # OpenCode 2 on a key you've added
doz try opencode --provider anthropic             # on your Anthropic key
doz try opencode --provider openai                # on your OpenAI key
doz try opencode --gateway openrouter             # through OpenRouter
doz try opencode --gateway openrouter --model anthropic/claude-sonnet-4.6
doz try opencode --gateway vercel-ai-gateway      # through Vercel AI Gateway
doz try opencode@2.0.29                           # exactly this release
doz try opencode --rm                             # delete it when you leave
```

No key for that provider yet? The try asks for one, once, or add it first with
`doz account add openrouter --provider openrouter`. Add `--dry-run` to any of these to see what it would make and what
it can reach, without making anything. In the dashboard, **Try → Quick try → OpenCode** has the same choices: the
Version, and where OpenCode gets its model, with a list of a gateway's models to search.

## Why OpenCode 1 stays

A major version changes what your setup depends on: here, plugins and the API. Dozer pins each tool to a version it
has checked. `opencode` now means OpenCode 2, the version Dozer recommends; OpenCode 1 stays one word away, as
`opencode@1`, and keeps getting 1.x updates. An existing sandbox never moves to a new major version by itself.

New to Dozer Sandbox? [Getting started](https://dozersandbox.com/docs/getting-started.html) takes a few minutes.
