---
title: "The Dozer Sandbox manual — Dozer Sandbox docs"
description: "The user manual for Dozer Sandbox: install, set up, and run AI coding agents in fast, resumable Linux sandboxes on your Mac, with the doz command or its dashboard."
url: https://dozersandbox.com/docs/
image: https://dozersandbox.com/og-image.png
source: "Dozer Sandbox manual"
updated: 2026-10-11
---
# The Dozer Sandbox manual

Dozer Sandbox runs AI coding agents in small Linux virtual machines on your Mac: each agent gets its
own disk, a network that only reaches what you allow, and your project folder if you share it. A
sandbox pauses in a millisecond and wakes from disk in a third of a second, with everything where you
left it.

You drive it with the `doz` command or its dashboard in your browser (`doz ui`). Every page here shows
both.

## Reading order

**New to Dozer?** Read these first, in order:

1. [Getting started](https://dozersandbox.com/docs/getting-started.html.md) — install, set up, and talk to Claude in a sandbox in 15 minutes.
2. [Sandboxes and their lifecycle](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md) — pause, sleep, hibernate, wake; what's kept where.
3. [Terminals and sessions](https://dozersandbox.com/docs/terminals-and-sessions.html.md) — attaching, the Ctrl-] menu, what the agent is doing, the clipboard, tmux.
4. [What the agent can do](https://dozersandbox.com/docs/permissions-and-network.html.md) — permissions and the network.

**Then, as you need them:**

| page | read it when you want to… |
|---|---|
| [Installing, upgrading and uninstalling](https://dozersandbox.com/docs/install-upgrade-uninstall.html.md) | install with Homebrew, upgrade safely, remove Dozer |
| [Setting up](https://dozersandbox.com/docs/setting-up.html.md) | (re)run onboarding in the terminal or the wizard |
| [Projects](https://dozersandbox.com/docs/projects.html.md) | give a folder its own sandbox with `doz_project.yaml` and `doz up` |
| [The dashboard](https://dozersandbox.com/docs/the-dashboard.html.md) | use `doz ui`: its pages, banners, sign-in links |
| [The dashboard on your other devices](https://dozersandbox.com/docs/doz-serve.html.md) | use the dashboard from another computer, a tablet or a phone on your network (`doz serve`) — and behind your own HTTPS reverse proxy |
| [Images and bases](https://dozersandbox.com/docs/images-and-bases.html.md) | pick a language base, use your own Dockerfile, rebuild an out-of-date image |
| [Agents and accounts](https://dozersandbox.com/docs/agents-and-accounts.html.md) | use Claude Code or pi, add accounts, change what the agent is told |
| [Codex](https://dozersandbox.com/docs/codex.html.md) | run OpenAI's Codex on your ChatGPT plan (Dozer's own sign-in) or an OpenAI key — the token never enters the sandbox |
| [Signing in from a sandbox](https://dozersandbox.com/docs/signing-in-from-a-sandbox.html.md) | let a tool in a sandbox sign in through your Mac's browser |
| [GitHub as you](https://dozersandbox.com/docs/github.html.md) | let git and gh in a sandbox use your GitHub login — read-only or with push — without the token entering it |
| [The tools layer](https://dozersandbox.com/docs/the-tools-layer.html.md) | know which tools Dozer puts in a sandbox for its settings (gh, the ssh client, tmux …) and check them |
| [Workspace rules](https://dozersandbox.com/docs/workspace-rules.html.md) | keep the agent out of some files in your shared folder (`.dozignore`), or let it read but not change them (`.dozreadonly`) |
| [The workspace view](https://dozersandbox.com/docs/the-workspace-view.html.md) | `dozview`, the small program in the sandbox every workspace goes through: why (programs keep their folder across a wake), what it costs, `workspace.view`, the rules it enforces, its two processes, sleep and wake, how to look inside. |
| [Prompts for your agent](https://dozersandbox.com/docs/prompts-for-your-agent.html.md) | prompts to paste into Claude Code, Codex or Cursor on your Mac: install, set up, and three uses — a risky change, jailing an untrusted agent, a project with secrets |
| [Restore points, duplicates and templates](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md) | undo, copy a sandbox, make your own starting image |
| [Resources and disk space](https://dozersandbox.com/docs/resources-and-disk-space.html.md) | see where the disk went and free some |
| [Letting another agent drive Dozer](https://dozersandbox.com/docs/letting-another-agent-drive.html.md) | have the agent on your Mac run sandboxes for you |
| [Settings reference](https://dozersandbox.com/docs/settings-reference.html.md) | look up any setting, its default and when it applies |
| [Security model](https://dozersandbox.com/docs/security-model.html.md) | understand what protects your Mac, and what doesn't |
| [Troubleshooting and FAQ](https://dozersandbox.com/docs/troubleshooting-and-faq.html.md) | fix something, or find a quick answer |
| [Audio sandboxes (EXPERIMENTAL)](https://dozersandbox.com/docs/audio-experimental.html.md) | try a sandbox with your Mac's microphone and speakers |

## Conventions

- Commands are shown as you type them: `doz up`. `NAME` is a sandbox's name; `my-app` is an example.
- Every command takes `--json` (machine-readable output), `--store DIR`, `-v` (every step) and `-q`
  (no progress). `doz help COMMAND` shows a command's options.
- Settings are named `section.name`, like `sandbox.clipboard`; see the
  [Settings reference](https://dozersandbox.com/docs/settings-reference.html.md).
- Screenshots use the light theme; the dashboard follows your Mac's appearance.

This manual is checked against `doz` itself on every build: every command, flag and setting it names
exists, and the settings reference is generated from the program.

The command-line [user guide](https://github.com/dozer-sandbox/dozer-sandbox/blob/main/docs/CLI-USER-GUIDE.md) and the [walkthrough](https://github.com/dozer-sandbox/dozer-sandbox/blob/main/docs/CLI-WALKTHROUGH.md) cover
the same ground for command-line users, more tersely.
