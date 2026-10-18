---
title: "Grok Build now tells Dozer what it's doing — Dozable blog"
description: "Grok Build 1.0.52 reports when it's working, waiting for you or done, and Dozer Sandbox 0.35 shows it in the dashboard, as it does for Claude Code and pi."
date: 2026-10-17
topics: [tool-news]
url: https://dozable.com/blog/grok-build-status
image: https://dozable.com/og-image.png
source: "Dozable blog"
---
# Grok Build now tells Dozer what it's doing

*17 October 2026 · Tool news*

Grok Build 1.0.52 reports its status, and Dozer Sandbox 0.35 runs that version. Start a Grok Build sandbox and leave it to
work; the dashboard shows when it's busy, when it needs you, and when it's finished.

```sh
doz try grok
```

## What you see

While Grok Build works, its tab says **working**, and a dot beside the sandbox in the sidebar says something is going
on.

![A Grok Build session at work: the tab says working](https://dozable.com/blog/images/grok-build-status/grok-working.jpg)

When it stops to ask you something, such as permission to run a command, a notice at the top of the dashboard says
so, with an **Open** button that takes you straight to the session, whichever page you're on.

![Grok Build asking permission to run a command: the notice names it, and the tab says needs permission](https://dozable.com/blog/images/grok-build-status/grok-needs-permission.jpg)

When it finishes, the tab says **done**. **All sessions** shows the same on every tile, so with several agents
running you can see which one is still busy and which is waiting for you.

![All sessions: Grok Build done beside other sessions](https://dozable.com/blog/images/grok-build-status/grok-all-sessions.jpg)

## Where it comes from

xAI's [changelog for 1.0.52](https://x.ai/changelog/build) lists "support for OSC 7501". That's a terminal escape
sequence for program status, [proposed by Mitchell Hashimoto](https://mitchellh.com/writing/program-status-osc7501):
a program asks the terminal whether it understands the sequence, and if it does, reports its state each time it
changes.

Inside every sandbox, Dozer answers that question for each session and keeps the latest report, whether or not the
dashboard is open. Nothing is read from the screen or guessed: Dozer shows exactly what Grok Build reports.

## Agents that report their status

Claude Code, pi and now Grok Build report their status. So do Factory Droid and Docker Agent, which also arrive in
0.35. When another tool adds support, Dozer turns it on in that tool's recipe once we've seen it work.

[Upgrade to 0.35](https://dozable.com/docs/install-upgrade-uninstall), then `doz try grok`.
