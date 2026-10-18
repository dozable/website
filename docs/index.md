---
title: "The Dozable manual — Dozable docs"
description: "The user manual for Dozable: install, set up, and run AI coding agents in fast, resumable Linux sandboxes on your Mac, with the doz command or its dashboard."
url: https://dozable.com/docs/
image: https://dozable.com/og-image.png
source: "Dozable manual"
updated: 2026-10-18
---
# The Dozable manual

Dozable runs AI coding agents in small Linux virtual machines on your Mac: each agent gets its
own disk, a network that only reaches what you allow, and your project folder if you share it. A
sandbox pauses in a millisecond and wakes from disk in a third of a second, with everything where you
left it.

You drive it with the `doz` command or its dashboard in your browser (`doz ui`). Every page here shows
both.

## Reading order

**New to Dozable?** Read these first, in order:

1. [Getting started](https://dozable.com/docs/getting-started.md) — install, set up, and talk to Claude in a sandbox in 15 minutes.
2. [Sandboxes and their lifecycle](https://dozable.com/docs/sandboxes-and-lifecycle.md) — pause, sleep, hibernate, wake; what's kept where.
3. [Terminals and sessions](https://dozable.com/docs/terminals-and-sessions.md) — attaching, the Ctrl-] menu, what the agent is doing, the clipboard, tmux.
4. [What the agent can do](https://dozable.com/docs/permissions-and-network.md) — permissions and the network.

**Then, as you need them:**

| page | read it when you want to… |
|---|---|
| [Installing, upgrading and uninstalling](https://dozable.com/docs/install-upgrade-uninstall.md) | install with Homebrew, upgrade safely, remove Dozable |
| [Setting up](https://dozable.com/docs/setting-up.md) | (re)run onboarding in the terminal or the wizard |
| [Projects](https://dozable.com/docs/projects.md) | give a folder its own sandbox with `doz_project.yaml` and `doz up` |
| [The dashboard](https://dozable.com/docs/the-dashboard.md) | use `doz ui`: its pages, banners, sign-in links |
| [The dashboard on your other devices](https://dozable.com/docs/doz-serve.md) | use the dashboard from another computer, a tablet or a phone on your network (`doz serve`) — and behind your own HTTPS reverse proxy |
| [Images and bases](https://dozable.com/docs/images-and-bases.md) | pick a language base, use your own Dockerfile, rebuild an out-of-date image |
| [Agents and accounts](https://dozable.com/docs/agents-and-accounts.md) | use Claude Code or pi, add accounts, change what the agent is told |
| [Trying agents, and what Dozable supports](https://dozable.com/docs/try-and-search.md) | try an agent in one command (`doz try`), check what Dozable runs (`doz search`), see a plan before anything is made (`--dry-run`) |
| [More agents](https://dozable.com/docs/more-agents.md) | run Antigravity CLI, Grok Build or Gemini CLI with an API key — what each may reach, what is kept out, whether it is current |
| [Other AI tools](https://dozable.com/docs/ai-tools.md) | AI tools that are not coding agents (Fabric, …) — tried like an agent, each on an API key |
| [Codex](https://dozable.com/docs/codex.md) | run OpenAI's Codex on your ChatGPT plan (Dozable's own sign-in) or an OpenAI key — the token never enters the sandbox |
| [Web ports](https://dozable.com/docs/web-ports.md) | open a web page a tool serves in a sandbox (a playground, your dev server) in your Mac's browser — `doz ports`, `doz open` |
| [Signing in from a sandbox](https://dozable.com/docs/signing-in-from-a-sandbox.md) | let a tool in a sandbox sign in through your Mac's browser |
| [GitHub as you](https://dozable.com/docs/github.md) | let git and gh in a sandbox use your GitHub login — read-only or with push — without the token entering it |
| [The tools layer](https://dozable.com/docs/the-tools-layer.md) | know which tools Dozable puts in a sandbox for its settings (gh, the ssh client, tmux …) and check them |
| [Workspace rules](https://dozable.com/docs/workspace-rules.md) | keep the agent out of some files in your shared folder (`.dozignore`), or let it read but not change them (`.dozreadonly`) |
| [The workspace view](https://dozable.com/docs/the-workspace-view.md) | `dozview`, the small program in the sandbox every workspace goes through: why (programs keep their folder across a wake), what it costs, `workspace.view`, the rules it enforces, its two processes, sleep and wake, how to look inside. |
| [Prompts for your agent](https://dozable.com/docs/prompts-for-your-agent.md) | prompts to paste into Claude Code, Codex or Cursor on your Mac: install, set up, and three uses — a risky change, jailing an untrusted agent, a project with secrets |
| [Restore points, duplicates and templates](https://dozable.com/docs/restore-points-duplicates-templates.md) | undo, copy a sandbox, make your own starting image |
| [Resources and disk space](https://dozable.com/docs/resources-and-disk-space.md) | see where the disk went and free some |
| [Letting another agent drive Dozable](https://dozable.com/docs/letting-another-agent-drive.md) | have the agent on your Mac run sandboxes for you |
| [Settings reference](https://dozable.com/docs/settings-reference.md) | look up any setting, its default and when it applies |
| [Security model](https://dozable.com/docs/security-model.md) | understand what protects your Mac, and what doesn't |
| [Troubleshooting and FAQ](https://dozable.com/docs/troubleshooting-and-faq.md) | fix something, or find a quick answer |
| [Audio sandboxes (EXPERIMENTAL)](https://dozable.com/docs/audio-experimental.md) | try a sandbox with your Mac's microphone and speakers |

## Conventions

- Commands are shown as you type them: `doz up`. `NAME` is a sandbox's name; `my-app` is an example.
- Every command takes `--json` (machine-readable output), `--store DIR`, `-v` (every step) and `-q`
  (no progress). `doz help COMMAND` shows a command's options.
- Settings are named `section.name`, like `sandbox.clipboard`; see the
  [Settings reference](https://dozable.com/docs/settings-reference.md).
- Screenshots use the light theme; the dashboard follows your Mac's appearance.

This manual is checked against `doz` itself on every build: every command, flag and setting it names
exists, and the settings reference is generated from the program.

The command-line [user guide](https://github.com/dozer-sandbox/dozer-sandbox/blob/main/docs/CLI-USER-GUIDE.md) and the [walkthrough](https://github.com/dozer-sandbox/dozer-sandbox/blob/main/docs/CLI-WALKTHROUGH.md) cover
the same ground for command-line users, more tersely.
