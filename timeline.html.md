---
title: "Dozer Sandbox timeline — from a probe to a public release"
description: "How Dozer Sandbox grew from a sleep-and-wake experiment into fast, resumable, secure Linux sandboxes for AI coding agents on your Mac, in about two weeks."
url: https://dozersandbox.com/timeline.html
image: https://dozersandbox.com/og-image.png
---
# From one experiment to a product, in two weeks.

Dozer Sandbox gives every coding agent its own small Linux computer on your Mac — one that pauses in a millisecond, hibernates to disk and wakes with everything still running. This is how it was built.

- **1 ms** to pause a sandbox
- **0.3 s** to wake from disk, programs still running
- **0** API keys inside a sandbox
- **100** sandboxes on one MacBook Air
- [The engine](https://dozersandbox.com/timeline.html#engine)
- [The command line](https://dozersandbox.com/timeline.html#cli)
- [The dashboard](https://dozersandbox.com/timeline.html#dashboard)
- [Agents & credentials](https://dozersandbox.com/timeline.html#agents)
- [Workspace & sessions](https://dozersandbox.com/timeline.html#workspace)
- [Going public](https://dozersandbox.com/timeline.html#public)

Era I · 25–27 Sep 2026

## The engine

Can a sandbox on your own Mac sleep like a laptop — and wake with its agent exactly where it was?

**25 Sep**

Prototype

### A Linux VM that sleeps like a laptop

Driving Apple's Virtualization framework directly, a Linux VM paused in a millisecond, saved itself to disk and came back — even in a new process after a crash. A small session holder inside the VM keeps terminal screens alive through all of it.

**0.23 s** back from disk, every process intact

**25 Sep**

v0.1.0

### The engine

The whole lifecycle in one library: start from an instant APFS clone, pause, sleep, hibernate, wake, and restore after a crash. Terminals reattach in under 60 ms.

**0.3 s** from an image to a running Linux

**25 Sep**

v0.2.0

### An agent in its own computer

Claude Code and pi baked into ready-to-run VM images. Each sandbox is a copy-on-write clone with its own disk for the agent's state, and restore points let you revert, fork or save a sandbox as an image in milliseconds.

**25 Sep**

v0.3.0

### No network card. Only a proxy.

A sandbox has no network interface at all: every connection goes through a policy on your Mac, deny by default, and every one is logged. Your API keys never enter — the sandbox holds a placeholder that is swapped for the real key on the way out.

**26 Sep**

Measured

### 100 sandboxes on a MacBook Air

Built in eight and a half minutes with zero errors. Wake time stays flat from one to twelve running sandboxes.

**~14,000** hibernated sandboxes would fit on its disk

**26 Sep**

v0.4.0

### Hardened, and lighter

Crash-safe disks, no leaks across hundreds of sleep cycles, safe parallel wakes — and a memory balloon that hands a woken sandbox's unused memory back to your Mac.

**−44 %** memory for a woken Claude Code sandbox

Era II · 27–28 Sep 2026

## The command line

One command, a host that looks after every VM, and your own Claude subscription.

**27 Sep**

v0.5.0

### `doz up`

One command creates, boots or wakes a sandbox and attaches your terminal. A per-user host owns every VM, starts only when it's needed and leaves when there's nothing to do.

**1 ms** pause · **0.3 s** wake, same processes and screens

**27 Sep**

v0.6.0

### Your Claude subscription, no API key

Sandboxes use this Mac's own Claude Code login. The token never enters the VM, and Dozer never touches the refresh token, so your Mac stays signed in.

**27 Sep**

v0.7.0

### Images that share their disk

Every image is an APFS clone of its base, so preparing one is three times faster and each extra image costs a fraction of the space. A journal makes disks crash-safe; TRIM hands deleted space back.

**~255 MiB** saved per extra image

**28 Sep**

v0.8.1

### Documentation

A first-sandbox tutorial, the concepts, and a command reference that is checked against the real CLI on every build.

Era III · 28 Sep – 2 Oct 2026

## The dashboard

Everything in your browser — without opening a door into your Mac.

**28 Sep**

v0.8.0

### `doz ui`

A built-in dashboard, locked to your Mac: loopback only, a one-use sign-in link, strict origin checks, and every button exactly one typed operation the CLI also has.

**29 Sep**

v0.9.0

### Terminals in the browser

Real terminals, isolated in a sandboxed frame, with tabs, a split and a watch-only mode. A hibernated sandbox wakes on your first keystroke and shows the very same screen.

**30 Sep**

v0.11.0

### A page for every sandbox

Each sandbox gets its own page with its terminals front and centre; All sessions shows every session at once. A sleeping sandbox shows its saved screen without being woken.

**1 Oct**

v0.12.0

### A first run done properly

`doz onboard` and a dashboard wizard check your Mac, set up your agent's account and prepare images up front. Sandboxes follow your Mac's time zone and tell the agent where it is running.

**~2 min** from a clean Mac to a prepared agent image

**1 Oct**

v0.13.0

### Resources

Every byte Dozer uses, including what clones share, and a way to give space back that previews exactly what goes before anything is deleted.

**2 Oct**

v0.14.0

### Install with Homebrew

No clone, no build: `brew install`, and upgrades that never pull the program out from under a running sandbox.

Era IV · 2 Oct 2026

## Agents, bases & credentials

What a sandbox is made of, what its agent may reach, and how it uses your accounts without ever holding them.

**2 Oct**

v0.15.0

### Any base, or your own Dockerfile

Ten language bases from Node and Python to Rust and .NET, or build from your own Dockerfile — with your agent on top of any of them.

**2 Oct**

v0.16.0

### Permissions in plain words

“Install Python packages”, “Update itself”, “Browse the web”: switches instead of firewall rules, with Locked, Standard and Open presets and a one-click fix when the agent is refused.

**2 Oct**

v0.17.0 – v0.18.0

### Bridges back to your Mac

An agent's copy lands on your clipboard, a sign-in started in the sandbox opens in your Mac's browser and finds its way back, and HTML or Markdown files open in your Mac's apps. Plus a full user manual.

**2 Oct**

v0.19.0 – v0.22.0

### One click, or nine careful steps

Quick add makes a sandbox with your defaults in one click. The New Sandbox wizard walks every choice and writes a `doz_project.yaml` your project keeps.

**2 Oct**

v0.20.0 – v0.23.0

### GitHub as you, read-only by default

git and `gh` use your Mac's GitHub login through the proxy; the token never enters the sandbox, and pushes are refused until you allow them. The tools your settings need appear by themselves.

Era V · 5–8 Oct 2026

## Workspace & sessions

Finer control over your files, a second first-class agent, the dashboard on your other devices, and sessions that never lose their place.

**5 Oct**

v0.24.0

### `.dozignore` and `.dozreadonly`

Keep an agent out of parts of your project — with Docker's exact pattern rules and without moving a file — or let it read but not change them.

**6 Oct**

v0.25.0

### A calmer dashboard

A style guide first, then every page restyled: one primary action per view, readable in light and dark, keyboard-friendly throughout.

**6 Oct**

v0.26.0

### Sound, as an experiment

Your Mac's microphone and speakers inside a sandbox. An experiment for now, held back for a later version.

**7 Oct**

v0.27.0

### Codex, first-class

OpenAI's Codex runs like Claude Code: on any base, without approval prompts, signed in with your Mac's Codex login or an API key — and the token never enters the sandbox.

**7 Oct**

v0.28.0

### Install the dashboard

Add it to your Dock as an app. It stays signed in, rides out restarts calmly and reattaches your terminals by itself.

**7 Oct**

v0.29.0

### `doz serve`

Your dashboard on your other computers, tablets and phones. Admit a browser with a QR code or an eight-character code and revoke it any time; sandboxes can never reach it.

**8 Oct**

v0.30.0

### Sessions survive every wake

Programs keep their working folder through every hibernation and host restart, and Restart session brings an agent back mid-conversation.

**8 Oct**

v0.30.1 – v0.30.2

### Steadier terminals

Full-screen agents draw cleanly in the browser, and a session opened while a sandbox is still preparing simply waits for it.

Era VI · October 2026

## Going public

The first public release.

**Coming**

v0.31.0

### Dozer Sandbox, for everyone

Signed and notarised, with a signed update feed and three channels — stable, beta and canary. Dozer tells you when there's a new release, or updates itself if you ask it to.

`brew install dozer-sandbox/tap/doz`
