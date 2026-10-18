---
title: "Dozer Sandbox 0.35 - doz try, and keys from any provider — Dozable blog"
description: "Dozer Sandbox 0.35 adds doz try for any of 42 coding agents and AI tools, keys from any major provider or gateway, a choice of model, and OpenCode 2."
date: 2026-10-18
topics: [release-news]
url: https://dozable.com/blog/doz-v0.35
image: https://dozable.com/og-image.png
source: "Dozable blog"
---
# Dozer Sandbox 0.35 - doz try, and keys from any provider

*18 October 2026 · Release news*

It's on the [stable channel](https://dozable.com/docs/install-upgrade-uninstall) now, as 0.35.1. It
includes everything from 0.34, which went straight from canary to this release.

## doz try

One command puts you in a throwaway sandbox with any of 42 coding agents and AI tools: its own empty folder, a
network that reaches only its model, and your key kept on your Mac. [doz try has its own post](https://dozable.com/blog/doz-try).

```sh
doz try opencode
```

## Keys from any provider, and a choice of model

Use a key from OpenAI, Anthropic, Google or xAI, or one key for many models through OpenRouter or Vercel AI Gateway.
Dozer can also read a key from 1Password, AWS Secrets Manager or a command each time it's needed. A try's setup and
New Sandbox let you pick the model from the gateway's own list, and `doz models` lists them.

The **Accounts & keys** page groups keys by provider, with the tools each one serves. A key that stopped working
comes first, with what the provider said and how to fix it.

![Accounts & keys: keys grouped by provider, a refused key first](https://dozable.com/blog/images/doz-v0.35/accounts-keys.jpg)

## Tools

- [OpenCode 2](https://dozable.com/blog/opencode-2) is the `opencode` Dozer recommends; OpenCode 1 stays as
  `opencode@1`. Its free OpenCode Zen models need no key.
- [Grok Build](https://dozable.com/blog/grok-build-status), Factory Droid and Docker Agent report working and
  done in the dashboard.

## Also new

- `doz search aider` says whether Dozer runs a tool, and how, or why not yet.
- A sandbox's web page opens in your Mac's browser: the sandbox's **Open** button, or `doz open`.

## Fixed

- Icons in the dashboard no longer blink every few seconds.
- A key its provider refuses shows as refused, instead of a green "ok".

## Upgrade

```sh
doz upgrade
```
