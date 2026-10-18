---
title: "Dozer Sandbox is now Dozable — Dozable blog"
description: "Dozer Sandbox has a new name, Dozable, in 0.36.1; the doz command, your sandboxes, your settings and how you upgrade all stay as they are."
date: 2026-10-19
topics: [release-news]
url: https://dozable.com/blog/dozable
image: https://dozable.com/og-image.png
source: "Dozable blog"
---
# Dozer Sandbox is now Dozable

*19 October 2026 · Release news*

A search for "dozer sandbox" finds sand toys, toy bulldozers and a sand-play centre in Kansas, and it will for a long
time: both are everyday words. Dozable is one word that only means us, and it says what the product does: sandboxes
that doze and wake in about a third of a second.

Dozable 0.36.1 is on the stable channel now.

## What changes

- **The name.** Dozable, everywhere: the dashboard, `doz --help`, the manual and this blog.
- **The website** moves to dozable.com. Every dozersandbox.com address keeps working and takes you to the same page.
- **The Homebrew tap** is now `dozable/tap`. New installs use it:

```sh
brew trust --tap dozable/tap
brew install dozable/tap/doz
```

## What stays

- **`doz`**, the Dozable command line. Every command and option is the same.
- **Your sandboxes, images and settings.** Nothing moves on your Mac.
- **Upgrading.** If you installed from `dozer-sandbox/tap`, you don't need to do anything: that name keeps working,
  and `doz upgrade` uses it.
- **Your subscription.** You're still subscribed to the same topics, and unsubscribing is still one click.

## Upgrade

```sh
doz upgrade
```
