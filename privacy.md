---
title: "Privacy Policy — Dozer Sandbox"
description: "What Dozer Sandbox and dozersandbox.com collect, why, and how to turn it off: anonymous usage statistics, optional sign-up, and the website."
url: https://dozersandbox.com/privacy
image: https://dozersandbox.com/og-image.png
updated: 2026-10-16
---
# Dozer Sandbox Privacy Policy

**Last updated:** 16 October 2026

Dozer Sandbox ("Dozer") is made by **Roundrect Pty Ltd** (ABN 36 613 522 277), Queensland, Australia ("we", "us"). This policy explains what Dozer and dozersandbox.com collect, why, and how to turn it off.

## In short

- **Your work stays on your Mac.** Dozer never collects anything from inside your sandboxes — not your code, files, prompts, commands' arguments, terminal output, sandbox names, paths, the sites your sandboxes reach, or your accounts and keys. Your API keys never leave your Mac.
- **Official builds send anonymous usage statistics** — counts and ranges about how Dozer itself is used, at most once a day — so we can see what to fix and improve. It is **on by default and easy to turn off** (below). You can see exactly what would be sent with `doz telemetry show`.
- **Signing up is optional.** If you give us your email, we use it only for what you ticked, and you can unsubscribe from any email in one click.
- **Builds from the open-source repository send nothing.** The statistics and sign-up code is part of the official builds only and is not open source.

## What gets collected

### 1. Anonymous usage statistics (official builds)

**When:** at most one message per day on days you use Dozer, plus one when you first run a new version. Sent in the background; if your Mac is offline, it is retried and dropped after 7 days.

**Identifier:** a random install ID created on your Mac (not linked to you, your email, your Mac's serial number or name). Reset it any time with `doz telemetry reset`.

**What is sent — the complete list:**

| About | Exactly what |
|---|---|
| The version | Dozer's version, release channel (stable, beta, canary), how it was installed (Homebrew or download), and the version you upgraded from |
| Your Mac | macOS major version (e.g. 26), chip family (e.g. M3), memory as a range (e.g. 16 GB, 24 GB, 64 GB+), CPU cores as a range |
| Commands | how many times each Dozer command was used that day (e.g. `create`: 2, `hibernate`: 3) — the command's name only, never its arguments |
| Failures | how many times a command failed and its exit code (a number), never the error text |
| Getting started | whether setup was done in the terminal or the dashboard, how far it got, and roughly how long until the first sandbox session (e.g. under 5 minutes) |
| Sandboxes created | how many were created with each agent (Claude Code, Codex, pi, none), each base image from Dozer's own list (custom Dockerfiles are counted only as "dockerfile"), each account type (this Mac's login, API key, setup token, none) and each network preset (standard, locked, open, custom) |
| Size of your setup, as ranges | how many sandboxes you keep, how many ran at once, how many restore points, total disk used (e.g. 5–20 GB) |
| Speed | typical and slow times for starting, waking, hibernating and pausing a sandbox that day, rounded to 50 ms |
| Reliability | how many wakes failed, sandboxes restored after a crash, host crashes, and which built-in image-preparation step failed |
| Features used | whether the dashboard, the installed dashboard app and `doz serve` were used, how many other devices are connected (as a range), whether workspace rules are in use, the GitHub access mode (off, read, push), whether an agent reported its status, how many restore points and templates were made, and your update setting |
| Time | how long sandboxes ran and slept, as counts of ranges (e.g. three ran for 5–30 minutes), how old sandboxes were when deleted, total running time and how long agents reported working, as ranges, and how many sandboxes were left running over 8 hours with no activity |

**Added by our server:** your **country**, worked out from the connection when the message arrives. ** We do not store your IP address.**

**Never collected:** the names of your sandboxes, images or projects; file or folder names and paths; anything inside a sandbox; anything you type or that a program prints; command arguments; Dockerfile contents; hostnames, websites or network rules; account names, emails or keys; exact times of day you worked; or any hash or fingerprint of your work.

**Why:** to see how Dozer is used and how well it performs in practice — which features to improve, what fails, what is slow, and what defaults to choose. **Lawful basis (EU/UK GDPR):** our legitimate interest in maintaining and improving the software, balanced by the data being minimal, anonymous and easy to turn off.

**Turning it off** — any one of these stops all sending:

- `doz config set telemetry.send_anonymous_usage_stats false` (or the switch in the dashboard's Settings),
- the environment variable `DO_NOT_TRACK=1`,
- `--no-send-anonymous-usage-stats` on a single command.

The first time an official build runs, it prints one line saying statistics are on and how to turn them off.

### 2. Sign-up (optional)

If you sign up — in Dozer's setup, with `doz signup`, or on dozersandbox.com/signup — we keep your **email address**, what you asked for (** release news**, ** tool news**, ** early access**, ** tips and tricks**), and when you signed up, confirmed and (if you do) unsubscribed. We send a confirmation email first; nothing else is sent until you confirm. Every email has a one-click unsubscribe link. We never sell or share your email, and never link it to your usage statistics. The emails are the posts of our [blog](https://dozersandbox.com/blog/index.md), sent only for the topics you ticked. They contain no open or click tracking. To send each one once and to stop sending to addresses that bounce or report spam, we keep a record of which posts were sent to your address and when, and whether one bounced or was reported; this record is deleted with your sign-up.

### 3. The website and the update feed

- **dozersandbox.com** uses no analytics, advertising or tracking scripts, and sets no cookies of its own — the blog included. Our host, Cloudflare, may set a strictly necessary security cookie and keeps standard request logs under [its own privacy policy](https://www.cloudflare.com/privacypolicy/). The colour picker on the site exists only when you open it on your own computer.
- **Update checks:** Dozer checks `updates.dozersandbox.com` for new releases at most once a day (or when you ask). That request carries Dozer's version and channel in its user agent and nothing else. It is part of keeping Dozer up to date, not the usage statistics; turn it off with `doz config set updates.mode off`.

## Where it is kept, and for how long

| What | Where | Kept |
|---|---|---|
| Usage statistics | Cloudflare: Workers Analytics Engine (global) and D1 (Oceania region) | raw messages up to 90 days; daily totals that cannot identify an install, indefinitely |
| Sign-up details | Cloudflare D1; emails sent through **Resend** (Resend, Inc., USA; sent from its Tokyo, Japan region) | until you unsubscribe or ask us to delete them; deleted within 30 days of a request (usually at once) |

Our service providers — **Cloudflare** (hosting, statistics storage) and **Resend** (sending email) — process data only on our behalf. Their servers may be outside your country (including the United States and Japan); we rely on their standard contractual protections for these transfers.

## Your choices and rights

You can turn statistics off at any time (above), reset your install ID, unsubscribe from any email, or ask us to access, correct or delete your sign-up details by writing to **privacy@dozersandbox.com**. Because the statistics are anonymous, we cannot find "your" statistics without your install ID — `doz telemetry show` prints it if you want us to delete its records. If you are in the EU or UK, you also have the right to object, to restrict processing and to complain to your data protection authority; in Australia, you can complain to the Office of the Australian Information Commissioner (OAIC). Signing up is based on your consent, which you can withdraw at any time by unsubscribing.

## Children

Dozer is a developer tool, not intended for children under 16, and we do not knowingly collect their information.

## Changes

If we change what is collected, we will update this page and the list Dozer shows in `doz telemetry show`, and note the change in the release notes. A change that collects more will never apply to data already sent.

## Contact

Roundrect Pty Ltd (ABN 36 613 522 277), Queensland, Australia — **privacy@dozersandbox.com**
