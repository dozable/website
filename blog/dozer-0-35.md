---
title: "Dozer Sandbox 0.35 - try 42 AI tools in one command — Dozer Sandbox blog"
description: "Dozer Sandbox 0.35 runs 42 coding agents and AI tools, each one command away, on your own key from any major provider or through a gateway, with a guide beside every try."
date: 2026-10-17
topics: [release-news]
url: https://dozersandbox.com/blog/dozer-0-35
image: https://dozersandbox.com/og-image.png
source: "Dozer Sandbox blog"
---
# Dozer Sandbox 0.35 - try 42 AI tools in one command

*17 October 2026 · Release news*

It's on the [stable channel](https://dozersandbox.com/docs/install-upgrade-uninstall.html) now, as 0.35.1. It
includes everything from 0.34, which went straight from canary to this release.

## Try a tool in one command

`doz try` makes a throwaway sandbox for any tool Dozer supports, starts it and puts you in it. The tool gets a new
empty folder of its own, a network that reaches its AI model and nothing else, and your key for its provider.

```sh
doz try                 # the list: coding agents, then AI tools, and which are ready
doz try opencode        # a try of OpenCode
doz try fabric --rm     # delete it when you leave
```

When you leave, it asks whether to sleep, delete or keep it running.

![doz try lists the coding agents and AI tools, and which have a key ready](https://dozersandbox.com/blog/images/dozer-0-35/try-terminal.jpg)

## Quick try in the dashboard

**Try → Quick try** shows the same tools as cards. Search, or filter by kind and category, and **Try now** opens its
setup: where the tool gets its model, your key and the folder.

![Quick try: coding agents and AI tools, with filters and each tool's readiness](https://dozersandbox.com/blog/images/dozer-0-35/quick-try.jpg)

## A guide beside every try

A try opens on its **Guide**: what the tool is, the facts of this try (version, model, network, folder), and the
first commands to run. **Run** types a step into the tool's session; **Copy** puts it on your clipboard.

![A Fabric try: the guide on the right, two steps run in the session on the left](https://dozersandbox.com/blog/images/dozer-0-35/try-guide.jpg)

## 42 coding agents and AI tools

Claude Code, Codex and pi are joined by Gemini CLI, Grok Build, OpenCode, GitHub Copilot CLI, Goose, Qwen Code,
Cline, OpenHands, Crush and more coding agents, and by tools such as Fabric, llm, AIChat, ShellGPT, promptfoo and
Google Stitch. The [manual](https://dozersandbox.com/docs/more-agents.html) lists them all, with what each needs.

Grok Build, Factory Droid and Docker Agent now report working and done in the dashboard, as Claude Code and pi do.

## Your key, from any provider or gateway

Use a key from OpenAI, Anthropic, Google or xAI. Or use one key for many models through OpenRouter or Vercel AI
Gateway, now offered to every tool that can take an OpenAI-style API. The key stays in your Mac's keychain; the
sandbox only ever holds a placeholder. Dozer can also read it from 1Password, AWS Secrets Manager or a command each
time it's needed.

```sh
doz account add work --openai-key          # paste the key when asked
doz account add grok --provider xai --from op://Dev/xAI/credential
```

The dashboard's **Accounts & keys** page is new too. Keys are grouped by provider, with the tools each one serves,
and the default chosen in place. A key that stopped working comes first, with what the provider said and how to fix
it.

![Accounts & keys: keys grouped by provider, a refused key first](https://dozersandbox.com/blog/images/dozer-0-35/accounts-keys.jpg)

## Choose the model

A try's setup and New Sandbox now have one section for where the tool gets its model: your providers, then the
gateways, each with its key. Pick a model from the gateway's own list, or type any model id.

```sh
doz models --gateway openrouter claude     # OpenRouter's models that match "claude"
doz try opencode --gateway openrouter --model anthropic/claude-sonnet-4.6
```

## OpenCode 2, and free models with no key

OpenCode 2 is the `opencode` Dozer recommends now; OpenCode 1 stays one word away as `opencode@1`, and a sandbox you
already have keeps its version. [Our OpenCode 2 post](https://dozersandbox.com/blog/opencode-2) has what's new
in it.

OpenCode Zen's free models need no account and no key at all:

```sh
doz try opencode --provider opencode-zen
```

The picker and `doz models` show each free model's data terms; some may use what you send to improve their models.

## Also new

- `doz search aider` says whether Dozer runs a tool, and how, or why not yet.
- Tools that serve a web page, and your own dev servers, open in your Mac's browser: the sandbox's **Open** button,
  or `doz ports add my-app 3000` then `doz open my-app 3000`. The page is on this Mac only.

## Fixed

- Icons in the dashboard no longer blink every few seconds.
- The Quick try window opens at once, and Start responds the moment you click it.
- A key its provider refuses now shows as refused, instead of a green "ok".

## Upgrade

```sh
doz upgrade
```

New to Dozer Sandbox? [Getting started](https://dozersandbox.com/docs/getting-started.html) takes a few minutes.
