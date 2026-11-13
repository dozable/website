---
title: "Working together with Grok Bot in a Claude Code session, enabled by Dozable — Dozable blog"
description: "Grok Bot hands design and coding to Claude Code sessions in templated Dozable sandboxes, and I can watch the same session or type in it."
date: 2026-11-13
topics: [tips]
url: https://dozable.com/blog/grok-bot-claude-dozable
image: https://dozable.com/og-image.png
source: "Dozable blog"
---
# Working together with Grok Bot in a Claude Code session, enabled by Dozable

*13 November 2026 · Tips and tricks*

I quickly fell for Grok Bot's charm and capabilities. From marketing to product management (I even have a librarian), my bots handle their daily duties well, and I now rely on them. But they can't design, and they can't code! At least not to the level I reliably get from Claude Code.

So I decided they should be able to delegate that work to Claude Code on my Mac, using my own subscription, just like I do. If all you want is command-line access, that's easy to set up in the Grok Bot app on your computer. The hard part came when I realised what I really wanted was for Grok Bot and me to work together in Claude Code.

Cheto, my CTO bot, now runs this in one Dozable sandbox per kind of work.

The fix was to give the bot the ability to use Claude's peer session messaging. This is a very cool feature that lets Claude sessions talk to each other. But it's only Claude to Claude, which meant giving the bot its own Claude session to pass messages to the working Claude (which can also message back), like a **relay**.

The relay is a long-lived Claude session that runs in the background, inside the sandbox, rather than in a project folder. It sends messages to the work sessions in that sandbox and prints what comes back, and it files the events those sessions raise. One relay serves every session in its sandbox. A second kind of work gets its own sandbox and its own relay, because a session cannot message a session in another sandbox.

## Why Dozable

Dozable was the right tool because of its session keeper. A session lives in the sandbox, not in a window. Several people or windows can view the same one, and what is typed in one shows in the others. I attach from Terminal.app with [`doz attach`](https://dozable.com/docs/terminals-and-sessions#in-the-terminal), or I open the session in the [dashboard](https://dozable.com/docs/the-dashboard) (`doz ui`). Watch, in the dashboard, is read-only. An attach, or Open, can type.

The other half is the boundary. A sandbox is a Linux virtual machine with its own kernel, so the tools for a workload are installed in its image and not on the Mac. They don't pollute the tools already there. For Remotion I save that image as a [template](https://dozable.com/docs/restore-points-duplicates-templates#templates), and the next team starts from it. A [recipe](https://dozable.com/docs/images-and-bases) is what bakes an agent's image, and a recipe cannot yet add the system packages this workload needs, so the template is the quick start I use.

The same work is what led Dozable to put the session keeper on the Mac itself. Xcode and signing cannot run in a Linux sandbox, and a session there is held the same way: detach, come back, type from a script, from Terminal.app or the dashboard. Those shared host sessions are isolated with macOS Seatbelt: `sandbox-exec` and a sandbox profile. It is the same technique [Claude Code](https://code.claude.com/docs/en/sandboxing), the [Codex CLI](https://learn.chatgpt.com/docs/sandboxing) and the [Gemini CLI](https://geminicli.com/docs/cli/sandbox/) use for agent isolation on macOS. The commands are in [Letting another agent drive](https://dozable.com/docs/letting-another-agent-drive), [Terminals and sessions](https://dozable.com/docs/terminals-and-sessions) and [Sessions on this Mac](https://dozable.com/docs/sessions-on-this-mac).

## The relay command

Cheto reaches the Mac through a Cursor [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines) worker, and the command is `relay`.

`relay up` makes the sandbox if it is missing, starts the relay, and starts one Claude Code session per project, each in its own folder.

```sh
relay up <sandbox> --team remotion-video --sessions 3 --workspace <parent-folder> --as <worker> --primary-agent "Grok Bot"
```

`--as` names the one driver of that sandbox.

`relay ask` types a short line into the relay. The relay uses Claude Code's [`SendMessage`](https://code.claude.com/docs/en/cross-session-messaging), by exact session name, and the answer arrives labelled `Message from @<sender-name>`. The request and the replies are files under `.agent-relay/`, and the worker passes them to the bot word for word.

```sh
relay ask <sandbox> video-1,video-2 --file task.md --detach
```

`--detach` returns at once. When every named session has answered, `relay forward` posts a `reply` event to the bot's webhook, the bot wakes, and `relay result` reads the text. The webhook address and its key stay in the Mac's login Keychain. The worker never prints them.

From [Dozable 0.37.44](https://dozable.com/docs/install-upgrade-uninstall), `relay` types and reads with [`doz sessions send`](https://dozable.com/docs/terminals-and-sessions#typing-into-a-session-and-reading-its-screen-from-a-script) and `doz sessions screen`. It does not attach, because an attach waits for a keyboard.

## A sandbox from a template

A team template is one YAML file: the size, the packages, the session names, the facts each session is told, a brief and the checks. `relay team ls` lists them. I have two. `remotion-video` is an 8G sandbox with 4 CPUs, Chromium, ffmpeg and fonts, and sessions named `video-1` onwards. `go-react-web` is a 4G sandbox with Go and Node, and one session named `app`, on the default base. The Go base refuses npm installs.

`--save-image`, the first time on a Mac, saves the tools as a [Dozable template](https://dozable.com/docs/restore-points-duplicates-templates#templates). The Remotion image is about 2.5 GiB, and the next team of that kind starts from it in about 20 seconds. I rebuild it when Claude Code moves on.

Sessions in one sandbox share the tools, the memory, the CPUs and the network. A different toolchain is another sandbox. If the work needs more network than the standard set, `relay` says so and I decide.

## Watching, and typing

Ctrl-] detaches, and the session keeps running.

```sh
doz attach <sandbox> <session>
```

A watcher is not a reason for the bot to stop. I set that rule on 13 November 2026. The bot stops typing only when I start: unsent text is on the line that it did not write, or I submit a line. It does not overwrite that text. When the line is clear, it carries on.

`relay rc` prints a claude.ai Remote Control link, for a phone or another browser. It depends on behaviour neither Dozable nor Claude Code documents, and an update to either can break it. `doz attach` is the way in I count on.

## The diagram

[Interactive diagram](https://dozable.com/blog/images/grok-bot-claude-dozable/diagram.html)

Play walks one round trip. Expand fills the window, and the link opens the diagram on its own page.

## How I got here

On 10 November, Claude Code 2.1.321 had no `claude send`, and resuming a running session with extra flags started a copy. A session that skipped permission prompts held a message from one that did not, on a prompt that was still waiting about four minutes later. That evening a script typed `SEND R1`, then `SEND R2`, then `SEND R3` into a throwaway relay. Each reply came back, in about 29, 15 and 18 seconds, without a restart. It was one receiver, and nothing woke the bot. `relay ask`, the shared-session rule and the webhook closed those gaps. Inside a sandbox, Dozable's Claude wrapper skips permission prompts. The sandbox is the boundary.

## A session

Sample output is marked with a `#`. Names are generic.

```timeline
left: Grok Bot (via its worker)
right: Me
---
> Which team templates are there?
$ relay team ls
remotion-video	Remotion videos
go-react-web	Go and React
# proven line omitted
---
> Let me watch.
$ doz ui
# Watch is read-only
# Open can type
---
> Starting three Remotion sessions.
$ relay up demo-remotion \
  --team remotion-video --sessions 3 \
  --workspace ~/work --as worker \
  --primary-agent "Grok Bot"
ready: demo-remotion — 3 sessions.
---
> I'll sit on video-1.
$ doz attach demo-remotion video-1
# attached; it keeps running when I leave
---
> Asking video-1 to make the intro.
$ relay ask demo-remotion video-1 \
  --file task.md --detach
# request 1700000000-1001 delivered
# then: relay result …
---
> Make the title two seconds longer.
make the title two seconds longer
# a line I type in the same terminal
---
> It can keep going while you watch.
# an attached client is not a reason to stop
---
> I'll leave it running.
# Ctrl-] twice detaches
# doz: d detach · n next · p prev · s sessions
# the session keeps running
---
> A reply should wake me.
$ relay forward demo-remotion --once
# a reply event wakes the bot
# no address is shown
---
> I'll watch the reply, read-only.
# Watch on video-1, read-only
---
> video-1 finished.
$ relay result demo-remotion 1700000000-1001
status: complete
# the rest is the session's reply
---
> I can see the reply.
# I see the reply on the session
---
> Here is a link to that session.
$ relay rc demo-remotion video-1
# prints a claude.ai link, not shown
---
> I'll type from the dashboard.
# Open types into video-1
---
> I'll keep a copy of the work.
$ relay collect demo-remotion
collected: ~/agent-relay-archive/demo-remotion/…
---
> Collect does not need me.
# collect does not need me
---
> I'm retiring the team.
$ relay retire demo-remotion --as worker
4/4 marked retired
RETIRED: demo-remotion. Nothing was deleted.
---
> It's still there. I have not removed it.
# hibernated; I have not removed it
```

## What still applies

A relay reaches only the sessions in its own sandbox. Xcode cannot run in a Linux sandbox, so that work is a shared host session (`doz run @mac`), isolated with macOS Seatbelt. Its prompt tells it to stop before signing or sending anything out. I leave tmux off in a sandbox. `relay collect` copies finished work onto the same Mac, and it is not a backup.

## The skill

The `relay` command, the session prompts, the two team templates and a health check that uses no model are one skill, `agent-relay`. I'm planning to publish the skills in their own public repo.

## About Dozable

Dozable gives each coding agent its own small Linux computer on your Mac, so you can let it work. A sandbox starts in about a third of a second, and your API keys stay on the Mac. Try it at [dozable.com](https://dozable.com).
