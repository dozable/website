---
title: "Dozer Sandbox — fast, resumable, secure Linux sandboxes for AI coding agents on your Mac"
description: "Run Claude Code, Codex or pi in a secure Linux VM on your Mac. Your API keys never enter the sandbox, every connection follows your policy, and it pauses in 1 ms and wakes in 0.3 s."
url: https://dozersandbox.com/
image: https://dozersandbox.com/og-image.png
---
# Suspend AI agents Wake in 0.3s

Fast, resumable, secure Linux sandboxes for AI coding agents on your Mac — your API keys never go inside. Free and open source.

Alpha Stable v0.32.0 [Version history →](https://github.com/dozer-sandbox/dozer-sandbox/releases)

```
brew trust --tap dozer-sandbox/tap && brew install dozer-sandbox/tap/doz && doz ui
```

Apple silicon Mac · macOS 26 or later · [Homebrew](https://brew.sh)

![Line drawing of a bulldozer asleep, with Zs rising](https://dozersandbox.com/dozer-sleeping.jpg)

## Built for sandboxing AI agents. Everything happens in milliseconds.

- **~0.3 s** **Start** with the image prepared
- **~1 ms** **Pause** attached terminals freeze and continue
- **~0.35 s** **Sleep** to disk — its memory goes back to the Mac
- **~0.3 s** **Wake** with programs, sessions and terminal screens as they were

Measured on an M3, with an Alpine guest of 512 MiB to 1 GiB.

## One command line does it all. For you, and for your agents.

`doz` is the whole of Dozer Sandbox — 112 commands to create, start, pause, sleep and wake sandboxes, run and attach to their sessions, and manage their network, keys, images and restore points. It even hosts its own web app: `doz ui` on your Mac, `doz serve` for your LAN, home-lab and Tailscale connected devices.

- `doz onboard` — Set up this Mac for Dozer Sandbox (once): check it, choose and confirm Access (the Claude account, GitHub, the SSH agent), choose what workspace rules do, write the settings, prepare images in the background. ([manual](https://dozersandbox.com/docs/setting-up.html.md))
- `doz init` — Make a folder a Dozer Sandbox project: write doz_project.yaml there (onboarding this Mac first if it never was). ([manual](https://dozersandbox.com/docs/projects.html.md))
- `doz uninstall` — Remove Dozer Sandbox from this Mac: the store, the settings and the installed doz — listed first, asked once. ([manual](https://dozersandbox.com/docs/install-upgrade-uninstall.html.md))
- `doz upgrade` — Look for a newer doz on your channel and install it (Homebrew: brew upgrade; a tarball install: the signed download) — asks first; -y does not. ([manual](https://dozersandbox.com/docs/install-upgrade-uninstall.html.md))
- `doz new` — The quickest way in: a new sandbox with every default — created, started and attached. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz create` — Create a sandbox (it stays off until start or up). ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz up` — Create the sandbox if it is missing, start or wake it, then attach (vagrant up / compose up). ([manual](https://dozersandbox.com/docs/projects.html.md))
- `doz start` — Boot a sandbox — or wake it, if it is asleep; resume it if paused. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz pause` — Pause: guest CPU to 0 in ~1 ms, RAM kept. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz resume` — Resume after pause (from sleep it wakes). ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz sleep` — Sleep: pause + snapshot to disk; RAM kept, and it survives a host crash. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz hibernate` — Hibernate: snapshot to disk and stop the VM — RAM returned; sessions come back on wake. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz wake` — Wake from sleep or hibernation (~0.3 s), sessions and pids where they were. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz shutdown` — Shut down: a cold stop that keeps the disk; running programs end. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz reset` — Reset to the image: shut down and discard the disk (restore points and the state disk stay). ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz rm` — Remove a sandbox and everything it has on disk. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz ls` — List the sandboxes: phase, RAM held, disk, sessions, network. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz inspect` — Everything about a sandbox, as JSON (--prompt: the agent's environment prompt, as its next session gets it). ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz sessions` — The sandbox's terminal sessions: list them (the default), end one, or restart one. ([manual](https://dozersandbox.com/docs/terminals-and-sessions.html.md))
- `doz sessions end` — End a session's program: it is hung up (as when its terminal closes), then terminated, then killed if it must be. ([manual](https://dozersandbox.com/docs/terminals-and-sessions.html.md))
- `doz sessions ls` — The sandbox's terminal sessions (they survive pause, sleep and hibernate). ([manual](https://dozersandbox.com/docs/terminals-and-sessions.html.md))
- `doz sessions restart` — Restart a session: end its program and start the same one again, in the same folder. ([manual](https://dozersandbox.com/docs/terminals-and-sessions.html.md))
- `doz attach` — Attach this terminal to a session (a paused or sleeping sandbox is woken). ([manual](https://dozersandbox.com/docs/terminals-and-sessions.html.md))
- `doz run` — Open a NEW session running a program, and attach to it. ([manual](https://dozersandbox.com/docs/terminals-and-sessions.html.md))
- `doz exec` — Run a command in the sandbox, non-interactively; its output and exit code pass through. ([manual](https://dozersandbox.com/docs/terminals-and-sessions.html.md))
- `doz image` — Images: the built-in lab, claude-code and pi, and custom images saved from restore points. ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz point` — Restore points: instant disk-only copies (APFS clones) to go back to or fork from. ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz net` — What a sandbox's agent may do (its permissions), its raw policy and its connection log. ([manual](https://dozersandbox.com/docs/permissions-and-network.html.md))
- `doz key` — Credentials held by the host's proxy — the sandbox only ever sees a placeholder. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz account` — Accounts the host holds for sandboxes: the Mac's Claude login, setup tokens, API keys; for Codex, a ChatGPT sign-in or an OpenAI key. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz metrics` — Lifecycle timings recorded by the host: per action count, median, p90, min, max, failures. ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz doctor` — Check this Mac and the store: macOS, Apple silicon, the entitlement, the kernel, vmnet, disk, the host. ([manual](https://dozersandbox.com/docs/troubleshooting-and-faq.html.md))
- `doz host` — The per-user host that owns every running sandbox (started for you; exits when idle). ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz events` — Follow what the host does: phases, timed steps, notes (Ctrl-C stops). ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz console` — Show a sandbox's boot console (the kernel and init); --follow keeps printing it as it boots (Ctrl-C stops). ([manual](https://dozersandbox.com/docs/terminals-and-sessions.html.md))
- `doz base` — The recommended bases a sandbox's image is made from (an image is a base × an agent). ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz base ls` — List the recommended bases: the image each follows, its download, the registries its sandboxes reach, which agents' images are prepared. ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz builder` — Apple's container tool, which builds Dockerfile bases (installed on demand; its services started only when you say so). ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz builder status` — Whether Apple's container tool is installed, supported and running. ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz builder start` — Start Apple's container services (container system start --enable-kernel-install) — asks first. ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz builder install` — Install Apple's container tool: its signed package (pinned, sha256-checked) opened in macOS Installer — asks first; never sudo. ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz image ls` — List the images and whether each is baked in this store (--tree: the lineage, with sizes). ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz image bake` — Bake (or rebuild) a built-in image now (otherwise the first start does it; minutes, needs network). ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz image rm` — Remove an image's baked disk (sandboxes cloned from it keep working). ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz image pull` — Pull an image from a registry (not yet). ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz image push` — Push an image to a registry (not yet). ([manual](https://dozersandbox.com/docs/images-and-bases.html.md))
- `doz point take` — Take a restore point (a running sandbox pauses for the clone: milliseconds). ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz point ls` — The sandbox's restore points, oldest first. ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz point revert` — Shut down and go back to a restore point (a "before revert" point is taken first). ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz point fork` — A new sandbox whose disks are a restore point's (it cold-boots on start). ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz point rm` — Delete a restore point (any, in any order). ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz point save-image` — Save a restore point (or the stopped sandbox's disk) as a custom image other sandboxes can start from. ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz net show` — What the agent can do: its permissions as a checklist, its sites, and what it was refused lately (the default: doz net NAME). ([manual](https://dozersandbox.com/docs/permissions-and-network.html.md))
- `doz net allow` — Switch permissions on (install:python, web, update, …; install = every ecosystem), allow a site (site:api.example.com), or set a preset (standard, locked, open). ([manual](https://dozersandbox.com/docs/permissions-and-network.html.md))
- `doz net deny` — Switch permissions off (web, update, install:node, …) or deny a site (site:HOST). ([manual](https://dozersandbox.com/docs/permissions-and-network.html.md))
- `doz net permissions` — Every permission, what it means, and the hosts behind it (this doz's). ([manual](https://dozersandbox.com/docs/permissions-and-network.html.md))
- `doz net policy` — Show the policy, or change it live (the next connection is judged by it; it is kept for the next start). ([manual](https://dozersandbox.com/docs/permissions-and-network.html.md))
- `doz net log` — The connection log (metadata only: host, verdict, rule, bytes — never contents). ([manual](https://dozersandbox.com/docs/permissions-and-network.html.md))
- `doz key set` — Give a proxied sandbox a key: read from stdin (or a prompt) or the keychain — never an argument. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz key rm` — Forget a key. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz key ls` — Which keys a sandbox has (never their values). ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz key policy` — What the proxy does with a credential the guest supplies itself: allow (and flag), strict (refuse), or auto. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz account ls` — The accounts (never a secret). ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz account add` — Add an account: a setup token or an API key (prompt or stdin), another Claude config dir's Mac login, a ChatGPT sign-in or an OpenAI key (Codex). ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz account verify` — Check an account: one tiny request to api.anthropic.com (or api.openai.com for an OpenAI key); a ChatGPT sign-in is renewed when it is due. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz account rm` — Remove an account and the keychain item doz made for it. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz account default` — The account sandboxes that follow the default use (or none). ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz account use` — Which account a sandbox uses: a name, default (follow the store's), or none. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz account keepalive` — on: near expiry, while a sandbox uses a Mac login and no Claude Code runs on the Mac, the host runs the Mac's claude once (off by default). ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz access` — Every credential sandboxes can use — the Claude account, GitHub as you, the SSH agent — confirmed live; set a choice. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz access show` — Show each credential choice and confirm it works now (the default: doz access). ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz access set` — Change an Access choice (the defaults for new sandboxes) and confirm it — failures are said, never blocking. ([manual](https://dozersandbox.com/docs/agents-and-accounts.html.md))
- `doz tools` — A sandbox's tools layer: the tools Dozer manages from its settings, why, and their state (--apply: set them up again now). ([manual](https://dozersandbox.com/docs/the-tools-layer.html.md))
- `doz ignore` — Workspace rules: what a .dozignore / .dozreadonly in a sandbox's workspace folder does, and why. ([manual](https://dozersandbox.com/docs/workspace-rules.html.md))
- `doz ignore check` — Which rule decides each path — locked, hidden, read-only or visible — and from which line of which file. ([manual](https://dozersandbox.com/docs/workspace-rules.html.md))
- `doz ignore show` — A sandbox's workspace rules: every pattern with its line, the mode, warnings, and whether the view runs in the sandbox. ([manual](https://dozersandbox.com/docs/workspace-rules.html.md))
- `doz host start` — Start the host (detached, unless --foreground). ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz host stop` — Hibernate every running sandbox and stop the host (the next command starts a new one; wake brings each back). ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz host restart` — Stop the host (running sandboxes hibernate) and start it again — on this doz's build (after an update). ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz host status` — Is a host running, and what does it hold? ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz host upgrade-check` — After an upgrade: is a host of an older build still running? ([manual](https://dozersandbox.com/docs/sandboxes-and-lifecycle.html.md))
- `doz ui` — A local web dashboard for this store: sandboxes, sessions, terminals, images, restore points, network, accounts, metrics, events. ([manual](https://dozersandbox.com/docs/the-dashboard.html.md))
- `doz ui link` — A new one-use link to the running UI of this store (opened, or printed with --print-url). ([manual](https://dozersandbox.com/docs/the-dashboard.html.md))
- `doz ui restart` — Restart the running UI of this store — the same port (or a changed ui.port), open pages stay signed in and reconnect by themselves. ([manual](https://dozersandbox.com/docs/the-dashboard.html.md))
- `doz ui start` — Start the UI (the default) — or, when one runs for this store, open a new link to it. ([manual](https://dozersandbox.com/docs/the-dashboard.html.md))
- `doz ui stop` — Stop the running UI of this store (a detached one, or one in another terminal); its open pages say it stopped. ([manual](https://dozersandbox.com/docs/the-dashboard.html.md))
- `doz serve` — The dashboard for your other computers, tablets and phones: http://<this Mac>.local:7443 on your network. ([manual](https://dozersandbox.com/docs/doz-serve.html.md))
- `doz serve devices` — The browsers let in: name, when first and last seen, from where, which browser. ([manual](https://dozersandbox.com/docs/doz-serve.html.md))
- `doz serve log` — What the other browsers did (the audit log): admissions, changes, terminals, refusals. ([manual](https://dozersandbox.com/docs/doz-serve.html.md))
- `doz serve rename` — Give a browser a name you will recognise ("Kitchen iPad"). ([manual](https://dozersandbox.com/docs/doz-serve.html.md))
- `doz serve revoke` — Remove a browser (by its ID from doz serve devices), or --all: it is signed out at once and needs a new invite. ([manual](https://dozersandbox.com/docs/doz-serve.html.md))
- `doz serve share` — An invite for one more browser: a QR code, a short code and a link (each works once, for five minutes). ([manual](https://dozersandbox.com/docs/doz-serve.html.md))
- `doz serve start` — Start serving (the default) — or, when doz serve runs for this store, say where. ([manual](https://dozersandbox.com/docs/doz-serve.html.md))
- `doz serve status` — Whether doz serve runs for this store, where, and how many browsers are let in. ([manual](https://dozersandbox.com/docs/doz-serve.html.md))
- `doz serve stop` — Stop the running doz serve of this store (its browsers stay let in for the next one). ([manual](https://dozersandbox.com/docs/doz-serve.html.md))
- `doz template` — Templates: a sandbox's root disk saved as an image other sandboxes are created from (never its state disk). ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz template create` — Save a sandbox's root disk (now, or a restore point's) as a template. ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz template ls` — The templates in this store. ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz template rm` — Remove a template (sandboxes created from it keep working). ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz duplicate` — A new sandbox from an existing one's disk (or a restore point), with a new workspace, CPUs, memory, network or account. ([manual](https://dozersandbox.com/docs/restore-points-duplicates-templates.html.md))
- `doz config` — Settings: the doz.toml file, every value and where it came from (flag, env, file or default). ([manual](https://dozersandbox.com/docs/settings-reference.html.md))
- `doz config show` — Every setting: its effective value and its source (the default). ([manual](https://dozersandbox.com/docs/settings-reference.html.md))
- `doz config get` — One setting's effective value (--json adds its source and default). ([manual](https://dozersandbox.com/docs/settings-reference.html.md))
- `doz config set` — Set one setting in the file (checked against its type and range). ([manual](https://dozersandbox.com/docs/settings-reference.html.md))
- `doz config unset` — Put one setting back to its default (comment it out in the file). ([manual](https://dozersandbox.com/docs/settings-reference.html.md))
- `doz config init` — Write the settings file: every setting with its default commented out (an existing file keeps its values and gains any new settings). ([manual](https://dozersandbox.com/docs/settings-reference.html.md))
- `doz config path` — Where the settings file is (${XDG_CONFIG_HOME:-~/.config}/dozer-sandbox/doz.toml). ([manual](https://dozersandbox.com/docs/settings-reference.html.md))
- `doz resources` — Everything Dozer uses (disk to the byte, memory, CPUs, network) and deleting what can go. ([manual](https://dozersandbox.com/docs/resources-and-disk-space.html.md))
- `doz resources ls` — The account: every byte of the store on a row (the last row, unattributed, is ~0), then memory, CPUs, traffic and kernels. ([manual](https://dozersandbox.com/docs/resources-and-disk-space.html.md))
- `doz resources rm` — Delete resources by id (doz resources lists them): shows what goes, what it frees and what each costs later, then asks once. ([manual](https://dozersandbox.com/docs/resources-and-disk-space.html.md))
- `doz resources clean` — Delete what is re-creatable AND unused: the download cache, base disks, old kernels, images no sandbox was created from lately, leftovers. ([manual](https://dozersandbox.com/docs/resources-and-disk-space.html.md))
- `doz resources kernel` — The kernel NEW sandboxes boot: a kernel:<version> doz resources lists, or pinned (this build's). ([manual](https://dozersandbox.com/docs/resources-and-disk-space.html.md))
- **For people** Readable output, live progress, and a question before anything is deleted.
- **For agents** Let the agents you trust sandbox the ones you don't: Claude Code or Codex on your Mac can create, watch and clean up sandboxes for you — every command takes `--json`, with exit codes to act on. [Prompts for your agent →](https://dozersandbox.com/docs/prompts-for-your-agent.html.md)
- **Hosts its own web app** `doz ui` opens the dashboard; `doz serve` shares it with your other browsers, by invite.

## A dashboard for every sandbox.

Your sandboxes and their terminals in one place, in your browser or installed as an app. `doz ui` on this Mac; `doz serve` for your LAN, home-lab and Tailscale devices.

![The Sandboxes page: host status, memory and disk totals, and a table of seven sandboxes in different phases: hibernated, off, failed, paused, asleep and running.](https://dozersandbox.com/shots/ui-overview.jpg)

**Every sandbox at a glance** The host, the memory held and the disk used, then each sandbox with its phase and its next action.

![A running sandbox's page with a terminal showing a passing test run, lifecycle buttons above it and an overview panel on the right.](https://dozersandbox.com/shots/ui-sandbox-terminal.jpg)

**A live terminal, in your browser** Pause, sleep or hibernate from the sandbox's own page, with its terminal and details beside it.

![A sandbox page where the agent's session tab carries a blue working badge, and the sidebar marks the sandbox.](https://dozersandbox.com/shots/ui-agent-working.jpg)

**See what your agent is doing** Claude Code and pi report when they are working, blocked or done, and the session tab and the sidebar show it.

![The All sessions page: two terminal tiles, one labelled working at 40 percent.](https://dozersandbox.com/shots/ui-all-sessions.jpg)

**Every session, side by side** All sessions of all running sandboxes in one grid, live and read-only. Click one to open it.

![The Network tab of a sandbox with a Locked, Standard and Open switch and toggles for talking to the AI model, signing in, updating and installing software.](https://dozersandbox.com/shots/ui-network.jpg)

**Network permissions you can read** Locked, Standard or Open, then switch each permission on or off, with the hosts behind it one click away.

![The New sandbox wizard on its Agent and base step, showing Claude Code, pi, Codex and none, and base images such as Node.js, Python, Go and Alpine.](https://dozersandbox.com/shots/ui-new-sandbox.jpg)

**A guided New sandbox** Ten steps: pick the agent and a base image, and your choices are written to the project's doz_project.yaml.

![The Images page in lineage view: an Alpine image, a template, sandboxes and restore points, each with shared and own sizes.](https://dozersandbox.com/shots/ui-images-lineage.jpg)

**Images, templates and restore points** The lineage from base image to sandbox to restore point, with what each shares and what it owns.

![The Resources page: a bar of kept, clean-up and shared space and a table of sandboxes with sizes and what would be freed.](https://dozersandbox.com/shots/ui-resources.jpg)

**Every byte accounted for** What Dozer uses on disk, what deleting each item would free, and a safe clean up.

![The dashboard in dark mode with a sandbox terminal showing a process list and a notice that doz ui restarted.](https://dozersandbox.com/shots/ui-reattach-dark.jpg)

**Dark mode, and terminals that come back** When doz ui restarts, its terminals reattach by themselves.

## How it compares.

A Claude Code sandbox, measured by us on an M3 MacBook Air (24 GB, macOS 27) in September 2026 — the median of 5 runs, each tool at its defaults.

| Measure | Dozer Sandbox | Docker containers | Docker Sandboxes | Apple container |
|---|---|---|---|---|
| Start, to Claude Code's first screen | 1.46 s | 0.78 s | 5.12 s | 2.24 s |
| Pause and resume, memory kept | about 1 ms | about 35 ms | not offered | not offered |
| Put away, memory freed | 1.16 s (hibernate) | 0.12 s (stop) | 5.31 s (stop) | 0.18 s (stop) |
| Back to a working agent | 0.57 s | 0.71 s | 1.28 s | 2.01 s |
| The same programs running afterwards | Yes — same process, same screen | No — restarted | No — restarted | No — restarted |

Dozer is slower to start cold and to put away — it writes the sandbox's memory to disk, so it can bring the same programs back.

| Measure | Dozer Sandbox | Docker containers | Docker Sandboxes | Apple container |
|---|---|---|---|---|
| Its own virtual machine per sandbox | Yes | No (one shared VM) | Yes | Yes |
| Hibernate and wake with programs still running | Yes | No | No | No |
| Survives a restart of the app that runs it | Yes | No | No | No |
| No network card — the only way out is a proxy | Yes | No | No | No |
| Blocks the network by default, with rules per sandbox | Yes | No | Yes | No |
| Your keys never enter the sandbox | Yes | No | Yes | No |
| Every connection logged | Yes | No | Yes | No |

Versions: Docker Desktop 4.91.0, Docker Sandboxes (sbx) 0.38.0, Apple container 1.2.2, and an earlier Dozer build. Docker Sandboxes' network and key rows are from its documentation; everything else was measured. One machine's numbers — yours will differ.

## The VM is the boundary.

Each sandbox is its own Linux virtual machine on Apple's Virtualization framework, with your project folder inside it. Run Claude Code, Codex or pi with its permission prompts off.

## Every connection. A policy you can read.

A sandbox has no network card. The proxy on your Mac judges every connection against permissions you can read and change with doz net permissions.

## Your keys never go in.

The proxy swaps your credentials in on the way out. The sandbox only ever sees a placeholder.

## Your project, at /workspace.

A folder on your Mac, shared into the sandbox. Keep .env files and secrets out of reach with .dozignore, or read-only with .dozreadonly. The rules guard against accidents; they are not a security boundary.

## Hibernate. Give the memory back.

A hibernated sandbox lets go of its memory and wakes with every program still running where it was. After a crash, sleeping sandboxes are restored with their sessions.

## On every screen you own.

doz serve shows the same dashboard to your other computers, tablets and phones on your network, admitted with an invite or a QR code.

## Undo is instant.

Restore points, duplicates and templates are APFS clones. Go back to a moment before the change, or fork a new sandbox from it.

## Bring your agent.

Claude Code, Codex and pi run ready to work, told where they run, with their credentials kept on your Mac.

## Three things worth a sandbox.

### A risky change

- A dependency upgrade, a big refactor, a migration. Let a sandboxed agent work on your project folder, with a restore point to fall back to. Review it with git diff.

### Jail an untrusted agent

- No folders shared, no logins held, the clipboard, browser and file bridges off, and the internet only where you allow it.

### A project that holds secrets

- Keep .env files, credentials and customer data out of the agent's reach, without moving anything.

[Prompts to paste for each, in the manual.](https://dozersandbox.com/docs/prompts-for-your-agent.html.md)

## brew install dozer-sandbox/tap/doz

```
# once per Mac: Homebrew loads a third-party tap only once trusted
brew trust --tap dozer-sandbox/tap
brew install dozer-sandbox/tap/doz
# opens the dashboard; a new install starts on its setup wizard
doz ui
```

Prefer the terminal? Run `doz onboard` once, then `doz up` in a project folder.

### Requirements

- Apple silicon. macOS 26 or later. [Homebrew](https://brew.sh). For an agent, an account it can use.

### Channels

- `doz` is stable and recommended. `doz-beta` and `doz-canary` come earlier.

### Trust

- Signed and notarised. Updates come from a feed signed with the project's own key, and nothing unverified is installed.

## Everything free and in the box.

- **Sleeps like a laptop** Pause in 1 ms. Hibernate to disk. Wake in 0.3 s, programs still running.
- **No network card** Every connection goes through a policy you can read.
- **Keys never go in** The proxy swaps credentials in. The sandbox sees a placeholder.
- **Dashboard** doz ui. An installable app, with terminals in the browser.
- **Claude Code, Codex, pi** Sessions outlive your terminal.
- **Restore points** Instant APFS clones. Go back, or fork.
- **.dozignore, .dozreadonly** Lock files, or make them read-only.
- **doz serve** The dashboard on your LAN, with invites and QR codes.
- **Pause, resume** About 1 ms.
- **Crash recovery** Back, with their sessions.
- **Permissions** Readable and editable.
- **Images** Base images and Dockerfiles.
- **Templates, duplicates** Start set up your way.
- **GitHub as you** Read-only by default.
- **Signed and notarised** The doz binary is signed and notarised.
- **Signed update feed** Stable, beta and canary. Nothing unverified installs.
- **Let your Mac's agent drive** Prompts to install, set up and run sandboxes.
- **SSH agent** Forward your Mac's agent.
- **Browser sign-in** Opens on your Mac, back in the sandbox.
- **Clipboard, open files** Bridges to your Mac.
- **Resources** Every byte accounted. Clean up safely.
- **Settings** doz config, doz.toml, dashboard.
- **Tools layer** gh, ssh and tmux, set up for you.

## Follow along.

The story so far is in the [Timeline](https://dozersandbox.com/timeline.html.md). For what comes next, leave your email: release news, early access and tips and tricks. [Read past issues →](https://dozersandbox.com/blog/index.md)
