---
title: "\"Dozer Sandbox 0.33: see what your agent is doing\" — Dozer Sandbox blog"
description: "Now on the stable channel — see what your agent is doing at a glance, a one-word upgrade, the dashboard in the background, and a way to hear about what's next."
date: 2026-10-11
topics: [release-news]
url: https://dozersandbox.com/blog/dozer-0-33
image: https://dozersandbox.com/og-image.png
source: "Dozer Sandbox blog"
---
# "Dozer Sandbox 0.33: see what your agent is doing"

*11 October 2026 · Release news*

Dozer Sandbox 0.33 shows what each agent is doing at a glance, upgrades with one command, runs the dashboard in the
background, and ends setup with an optional sign-up. It's on the stable channel now; here's each change.

## See what the agent is doing

Claude Code and pi now tell Dozer whether they're working, done, or waiting for you. The dashboard shows it on
every tab and tile, and tells you when an agent finishes or needs an answer, even when nobody is watching that
session. Claude Code needs version 2.1.295 or later, and pi 1.1.0 or later.

## `doz upgrade`

One command moves you to the newest version on your channel. It asks first; `-y` skips the question.

```sh
doz upgrade
```

## The dashboard in the background

`doz ui --detach` runs the dashboard without holding a terminal, and `doz ui stop` stops it from any terminal.

## Staying in touch

Setup now ends with an optional sign-up for release news, early access, and tips and tricks, by email. Skip it, or
sign up later with `doz signup`.

## Upgrade

```sh
doz upgrade
```

New to Dozer Sandbox? [Getting started](https://dozersandbox.com/docs/getting-started.html) takes a few minutes.
