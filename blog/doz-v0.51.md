---
title: "Dozable 0.51 - chat rooms, and fenced sessions on your Mac — Dozable blog"
description: "Dozable 0.51 adds chat rooms for you and your agents, fences sessions on your Mac by default, keeps the daemon running with a menu bar app, and can publish the dashboard on your tailnet."
date: 2026-11-19
topics: [release-news]
url: https://dozable.com/blog/doz-v0.51
image: https://dozable.com/og-image.png
source: "Dozable blog"
---
# Dozable 0.51 - chat rooms, and fenced sessions on your Mac

*19 November 2026 · Release news*

It's on the [stable channel](https://dozable.com/docs/install-upgrade-uninstall) now, as 0.51.15. This post covers
0.40.0 to 0.51.15; [the 0.37 post](https://dozable.com/blog/doz-v0.37) covers what came before. The changes come
first by theme, then release by release in the [detailed changelog](#detailed-changelog).

## Chat rooms for you and your agents

Chat is a set of rooms on your Mac where you and your agents talk: you in the dashboard or a terminal, each agent with
its own token. It is off until you turn it on, it listens on this Mac only, and everything is kept in your store.

```sh
doz chat on --name ada              # chat on; you are ada in chat
doz chat add bot1                   # an agent; its token is shown once
doz chat room room1 @bot1           # a room with bot1 and you
doz chat send room1 "the build is green"
doz chat read room1 --follow        # the room as it happens
```

- **The Chat page** in the dashboard has the rooms, messages as they arrive, `@` mentions, reactions, edit and delete,
  direct messages and attachments up to 20 MB.
- **`dozchat`** is a small chat client on the PATH of every sandbox and fenced session. Give it its token as a
  secret (below) and the session only ever sees a placeholder.
- **Claude Code sessions on this Mac** can take part: the chat server writes each message into the session's own
  inbox, busy or idle (`doz chat add bot1 --inbox`). This works for sessions without a fence; a fenced one uses
  `dozchat`.
- **Webhook bots** are called with each message instead of polling (`doz chat webhook set NAME`). The address and
  its secret are kept in your login keychain.
- **Agents on your other machines** can join over Tailscale, as agents with their own token, never as you
  (`chat.remote_listen` and `chat.remote_agents`).
- **`doz chat import`** brings in the history of another chat server from an export.
- **Your other browsers** get no chat until you set `serve.chat` to `read` or `write`.

## Sessions on this Mac are fenced

In 0.37 a session on this Mac ran as you, with nothing around it. A new session is now **fenced**: macOS's own
sandbox keeps it to its project folder, its own temporary files and caches, and Dozable's proxy for the network. Your
Keychain, secrets and other folders are closed to it. `--unfenced` gives a session what it had before, and sessions
you opened earlier keep their mode.

```sh
doz run @mac -d --session agent --folder ~/src/app -- claude   # Claude Code, fenced, on one folder
doz run @mac -d --xcode --folder ~/src/MyApp -- claude          # with Xcode's build services
doz run @mac --dry-run -- claude                                # what it could do; starts nothing
```

- **Claude Code** in a fenced session gets its own settings folder and its login through the proxy, so it never holds
  your token. Its conversations come back to `~/.claude/projects` when it ends.
- **Tools work through the fence:** git and ssh, GitHub as you (`--github read|push`), your SSH agent
  (`--ssh-agent`), the package registries, Swift and Xcode builds (`--xcode`) and the Simulator (`--simulator`).
- **New session on this Mac…** in the dashboard gives the exact command for five common setups, including the build
  commands that work inside the fence and when to go unfenced. Each session's **What it can do** tab shows its
  permissions and switches them live.
- **A service on your Mac**, such as a local API, is reachable from a sandbox or session with `--host-port 8790`, as
  `host.dozable.internal:8790`. Nothing else of the Mac opens.
- **`--secret`** gives a session a token as a placeholder, which Dozable swaps for the real value only on requests
  to the host and port you name.
- **Site permissions can name ports:** `doz net allow NAME site:example.com:8443`.
- **Sandboxes** can no longer reach this Mac through any of its network addresses.

The manual has the details: [Sessions on this Mac](https://dozable.com/docs/sessions-on-this-mac).

## The daemon stays running, with a menu bar app

Dozable's background process is now called **the daemon**, and `doz host` is gone, with no alias:

```sh
doz daemon status
doz daemon restart
```

- **It stays running** (`daemon.always_on`, on by default), and when you upgrade it moves to the new version by
  itself once nothing is running.
- **It can start when you log in.** Nothing is added until you ask: `doz daemon login-item on`.
- **The menu bar app** shows the daemon's state, with Start, Stop, Restart, Open Dashboard and Start at Login:
  `doz app install --open`.
- **An unattended Mac keeps its Claude login.** `doz account keepalive always` renews it when it expires.

## The dashboard on your tailnet

`doz ui publish tailscale` gives the dashboard its own https address, `https://dozable-<your Mac>.<your tailnet>.ts.net`,
through a Tailscale node of Dozable's own; your Mac's own Tailscale is left alone. The address comes back after a
restart of the Mac.

```sh
brew install tailscale          # once
doz ui publish tailscale        # sign in once, then it says the address
doz ui publish status           # check it
```

Each browser on another device still needs an invite (`doz ui share`). See
[The dashboard on your other devices](https://dozable.com/docs/doz-serve).

The dashboard also follows upgrades now, and offers **Restart dashboard** when it is older than the doz you installed.

## Renamed

| before | now | since |
|---|---|---|
| `doz host start\|stop\|restart\|status` | `doz daemon start\|stop\|restart\|status` | 0.50 |
| `DOZ_HOST_IDLE` | `DOZ_DAEMON_IDLE` | 0.50 |
| `--workspace DIR` | `--folder DIR` | 0.51 |
| `doz run @mac --workdir DIR` | `doz run @mac --folder DIR` | 0.51 |
| `doz run NAME --workdir DIR`, `doz exec NAME --workdir DIR` | `--cwd DIR` | 0.51 |
| the `doz ls` column WORKSPACE, `--json` key `workspace` | FOLDER, `folder` | 0.51 |
| settings `workspace.ignore_mode`, `workspace.view` | `folder.ignore_mode`, `folder.view` | 0.51 |

The old names fail and say the new one. Settings under `host.*` move to `daemon.*` by themselves.

## Detailed changelog

Every release from 0.40.0 to 0.51.15, newest first. **Stable** marks the releases that reached the stable channel;
the others were on canary only, and their changes reached stable with the next stable release. Numbers that are
missing, such as 0.40.1, were never released.

### 0.51.15 - 18 November 2026 - stable

- Fixed: `doz ui publish tailscale` sets up the redirect from plain `http://` to the https address on a real Mac.
  A dashboard published with 0.51.14 is told to run `doz ui publish tailscale` again.

### 0.51.14 - 18 November 2026

- Added: `doz ui publish tailscale` gives the dashboard its own https address on your tailnet, through Dozable's own
  Tailscale node (your Mac's own Tailscale is left alone). `doz ui publish status` and
  `doz ui unpublish tailscale [--logout]`.
- Added: while it is published, the daemon keeps the dashboard running, until you run `doz ui stop`.

### 0.51.13 - 18 November 2026 - stable

- Changed: the dashboard follows upgrades. `doz ui` starts the doz installed now, and a dashboard in the background
  restarts into a new doz when nothing is open.
- Added: **Restart dashboard** in the dashboard when it is older than the installed doz (this Mac's own browser only).
- Changed: the installable dashboard app is named after its Mac ("Dozable – <this Mac>"). A copy installed before may
  need installing again to pick up the name.
- Fixed: `doz doctor` no longer tells you to stop a newer daemon when the dashboard is the older one, and an update is
  never offered for the build already installed.

### 0.51.12 - 18 November 2026 - stable

- Fixed: a fenced Claude Code session started as `env NAME=VALUE … claude` works, and resumes with its variables.
- Changed: every fenced session gets its own temporary folder for Claude Code (`CLAUDE_CODE_TMPDIR`).
- Changed: the chat agent skills check that a started worker came up, and correct their advice on Claude Code's
  read-only commands.

### 0.51.11 - 18 November 2026 - stable

- Fixed: `doz chat set … --session NAME` takes the name a Claude Code session shows, capitals and spaces included.

### 0.51.10 - 18 November 2026 - stable

- Added: chat writes each message straight into a Claude Code session's inbox on this Mac (sessions without a fence).
  `doz chat who` shows `not running`, `idle` or `working`.
- Added: `doz chat set NAME --deliver inbox|poll|webhook` changes how a participant is reached, keeping its token,
  rooms and history; `doz chat add NAME --inbox`.
- Added: `dozchat` is on your Mac's PATH, and reaches this Mac's chat server by default.
- Fixed: the menu bar app restarts itself to update ("Restart to Update").
- Changed: `doz chat send` lists each recipient once, with its latest state.

### 0.51.9 - 17 November 2026 - stable

- Added: `dozchat`, a small chat client in every sandbox and fenced session, with nothing to install and nothing to
  set. Its token is only ever a placeholder Dozable swaps.
- Added: a static `dozchat` for x86_64 Linux on the release page, for agents outside Dozable.
- Changed: the chat server's messages name Dozable's own commands.

### 0.51.8 - 17 November 2026 - stable

- Added: the chat protocol's documents, a one-file Python client and three agent skills, in `docs/chat/` of the
  source repository, for agents that can install nothing.
- Changed: an agent with a valid token can always ask which rooms it is in.

### 0.51.7 - 17 November 2026

- Added: in the Chat page, reactions, edit, delete, revealing a direct message, typing indicators and attachments
  (clip, paste or drop; up to 20 MB).
- Added: `serve.chat` (`off`, `read`, `write`; default `off`) decides what your other browsers may do in chat.
- Added: `doz chat` is listed in `doz --help`, with completions and a manual chapter.
- Fixed: `doz chat status`, `doz daemon status` and `doz doctor` no longer report a new chat port before the chat
  server has moved to it.

### 0.51.6 - 17 November 2026

- Added: the Chat page in the dashboard, while chat is on: rooms, messages as they arrive, a composer with `@`
  mentions, who is here, and unread counts.

### 0.51.5 - 17 November 2026 - stable

- Added: webhook bots (`doz chat add NAME --webhook`, `doz chat webhook set|status|remove`), with the entry kept in
  your login keychain.
- Added: agents on other machines over Tailscale (`chat.remote_listen`, `chat.remote_agents`), as agents only.
- Added: `doz chat import COPY [--dry-run] [--add-missing] [--replace]`.
- Fixed: a long answer from the chat server, such as `doz chat read` of a long room, was sometimes cut short.

### 0.51.4 - 17 November 2026 - stable

- Added: the daemon runs the chat server when `chat.enabled` is on (off by default), on this Mac only.
- Added: the first `doz chat` commands: `on`, `off`, `status`, `add`, `remove`, `who`, `token`, `rooms`, `room`,
  `send`, `read`. You take part through a private socket and never have a token.
- Fixed: a settings line under an old `workspace.*` name was warned about even after the new name was set.

### 0.51.3 - 17 November 2026 - stable

- Groundwork for chat (attachments and delivery into Claude Code sessions); nothing visible yet.

### 0.51.2 - 17 November 2026

- Groundwork for chat (reactions and webhook delivery); nothing visible yet.

### 0.51.1 - 17 November 2026

- Groundwork for chat (posting and reading); nothing visible yet.

### 0.51.0 - 17 November 2026

- Changed: what a sandbox or a session works on is its **folder**. `--workspace DIR` is now `--folder DIR`,
  `--workspace-view` is `--folder-view`, `doz run @mac --workdir` is `--folder`, and `--workdir` on `doz run NAME`
  and `doz exec NAME` is `--cwd`. The old flags fail and name the new one.
- Changed: the `doz ls` column WORKSPACE is FOLDER, and `--json` keys `workspace…` are `folder…`. Settings
  `workspace.ignore_mode` and `workspace.view` are `folder.ignore_mode` and `folder.view`; `workspace_view:` in
  `doz_project.yaml` is `folder_view:`. "Workspace rules" are "Folder rules".
- Changed: a 0.51 doz and an older daemon refuse each other. After upgrading, run `doz daemon stop` once.
- Changed: `daemon.idle_timeout_minutes` defaults to 5 again; it applies only when `daemon.always_on` is off.

### 0.50.9 - 17 November 2026 - stable

- Groundwork for chat; nothing visible yet.

### 0.50.8 - 17 November 2026 - stable

- Added: **Start at Login** in the menu bar app starts the daemon (and the menu) when you log in. It replaces doz's
  own login item, so there is only ever one.

### 0.50.7 - 16 November 2026 - stable

- Added: the menu bar app, Dozable.app: the daemon's state, Start, Stop, Restart and Open Dashboard.
  `doz app install`, `doz app status`, `doz app uninstall`.

### 0.50.6 - 16 November 2026 - stable

- Added: `doz account keepalive off|on|always`. `always` renews this Mac's Claude login when it expires, with no
  sandbox needed.
- Fixed: the keep-alive runs when the login expires, not before (an early run renewed nothing), and tries again if it
  fails.
- Fixed: a Claude login made over ssh is read as expired when it expires, so it can be renewed.

### 0.50.5 - 16 November 2026 - stable

- Added: `doz daemon login-item on|off|status` starts the daemon when you log in. Nothing is written unless you say so.
- Changed: `doz daemon stop` keeps the daemon stopped until the next doz command or your next login.
- Changed: `doz uninstall` and `doz nuke` remove the login item. Run `doz uninstall` before `brew uninstall`.

### 0.50.4 - 16 November 2026 - stable

- Changed: the daemon stays running (`daemon.always_on`, on by default) and moves to a new build by itself after an
  upgrade, once nothing is running. To have it exit when idle: `doz config set daemon.always_on off`.
- Changed: a daemon started over ssh still exits when idle, so the next one from your desktop can read your keychain.

### 0.50.3 - 16 November 2026 - stable

- Added: `--secret VAR,src=PATH,to=HOST:PORT` on `doz create`, `doz run NAME` and `doz run @mac`. The session gets a
  placeholder, swapped for the value only on requests to that host and port. `doz net show` lists each one by a
  fingerprint, never the value.

### 0.50.2 - 16 November 2026 - stable

- Added: `--host-port PORT` (and `host_ports:` in `doz_project.yaml`) lets a sandbox or fenced session reach a service
  on this Mac as `host.dozable.internal:PORT`. `doz net allow NAME host:PORT` changes it live.

### 0.50.1 - 16 November 2026 - stable

- Added: site permissions can name ports: `site:HOST:PORT` and `site:HOST:P1,P2`.
- Changed: a refused connection on a port other than 80 or 443 suggests the narrow permission.
- Changed: `--permissions site:localhost` on a session on this Mac is refused (it never opened anything).

### 0.50.0 - 16 November 2026 - stable

- Changed: `doz host` is now `doz daemon` (`start`, `stop`, `restart`, `status`, `upgrade-check`). `doz host` no
  longer exists.
- Changed: settings `host.*` are now `daemon.*` (moved for you); `DOZ_HOST_IDLE` is `DOZ_DAEMON_IDLE`; `--json` names
  say `daemon`.
- Fixed: sessions on this Mac keep running while the daemon is replaced by the new version.

### 0.40.3 - 16 November 2026

- Added: the New session wizard shows the Swift and Xcode build commands that work in a fenced session, and when to
  go unfenced. `doz run @mac --xcode --dry-run` prints them too.

### 0.40.2 - 15 November 2026 - stable

- Fixed: `swift test` works in a fenced `--xcode` session.
- Fixed: `doz sessions restart` resumes the right Claude Code conversation, and says so when the program dies at once.
- Fixed: a foreground `doz run @mac` returns its program's exit code.
- Fixed: a Claude login made over ssh is seen.
- Added: `mac.fence_loopback_listen` (off by default), for test servers that pick their own port.

### 0.40.0 - 14 November 2026 - stable

- Changed: sessions on this Mac are **fenced** by default. `--unfenced` (or `mac.fence off`) gives a session what it
  had before; sessions opened before keep their mode.
- Added: a fenced session's network goes through its own Dozable proxy, with a sandbox's permissions; Claude Code gets
  its own settings folder and its login through the proxy; GitHub (`--github`), your SSH agent (`--ssh-agent`),
  `--xcode` and `--simulator`.
- Added: `doz sessions @mac --capabilities NAME`, and in the dashboard the session's "What it can do" tab and
  **New session on this Mac…**.
- Changed: sandboxes can no longer reach this Mac through any of its addresses; `mac.dozable.internal:PORT` still
  reaches a model server. "Use GitHub" includes GitHub's Git LFS host.

## Upgrade

```sh
doz upgrade
doz daemon stop     # once, after upgrading to 0.51 from an earlier version
```

`doz upgrade` moves you to the newest version on your channel. With Homebrew directly, run `brew update` first,
then `brew upgrade dozable/tap/doz`. Coming from 0.36 or earlier? Read
[the 0.37 post's Upgrade section](https://dozable.com/blog/doz-v0.37#upgrade) first: 0.37 started with a new store.

There are three channels: stable (`dozable/tap/doz`), beta (`dozable/tap/doz-beta`) and canary
(`dozable/tap/doz-canary`), which gets every build first. `doz upgrade --channel canary` switches.

More is coming soon. Thank you for using Dozable.
