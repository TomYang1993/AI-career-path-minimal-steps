# Changelog

Changes to the steps in [README.md](README.md), newest first. Course and project links are re-checked against their live pages when a change lands; the date says when.

Each entry is published as a [GitHub Release](https://github.com/TomYang1993/AI-career-path-minimal-steps/releases) when it lands on `main`: start it with `## YYYY-MM-DD · short title`.

## 2026-11-04 · get hired, harness engineering, essential reads

- Every path now ends with a **Get hired** step after the capstone: interview prep, plus what to publish as a portfolio. The AI engineer step links LevelUp Labs' free AI Engineer interview prep and system design case studies.
- AI engineer step 5.1 is now **Harnesses & production agents**, with [Learn Claude Code](https://github.com/shareAI-lab/learn-claude-code) (build a coding agent's harness step by step) and Anthropic's guide to long-running harnesses.
- Essential guides added as `Read:` lines: OWASP Top 10 for LLM Applications, Building effective agents, Effective context engineering for AI agents, and Demystifying evals for AI agents.
- Agent security: the prompt-injection design patterns paper on step 5.1, and OWASP's list on LLM APIs for both the AI engineer and DevOps paths.
- New **Do the projects for $0** section: free API tiers, local models and free GPU notebooks.
- Several of these came from [awesome-generative-ai-guide](https://github.com/aishwaryanr/awesome-generative-ai-guide), [agentic-engineering-handbook](https://github.com/keyuchen21/agentic-engineering-handbook) and [awesome-ai-resources](https://github.com/mohabdelkarim/awesome-ai-resources).

## 2026-11-03 · capstone follow-alongs and overview

- A table at the top sums up each role: number of steps and skills, a rough total time, and the capstone.
- Each capstone now lists free, end-to-end builds to follow: Decoding AI's Second Brain AI Assistant course (AI engineer), the vLLM Production Stack tutorials (platform), the AI Dev Tools Zoomcamp with Vercel's AI SDK RAG template and the promptfoo GitHub Action (DevOps / full-stack), and nanochat with Reasoning from Scratch (researcher). Where running them costs money (API calls, GPU time), the line says roughly how much.
- nanochat's run time updated to match its README: about 2 hours on one 8×H100 node, around $50.

## 2026-11-03 · first version

First version: the minimal steps for four AI roles, as plain text and links.

- Four roles: AI engineer, Cloud / ML platform engineer, DevOps / full-stack engineer, ML trainer / researcher. Each runs from foundations to specialization and ends with a capstone.
- One course and one project per skill (two where they pair up), each with a line on what to focus on and roughly how long it takes.
- AI engineer merges the agent-builder and RAG-builder archetypes from the [AI Engineering Field Guide](https://github.com/alexeygrigorev/ai-engineering-field-guide): most postings that ask for one also ask for the other. The path shares one trunk, then splits into an agent branch and a retrieval branch.
- No role share percentages: they are estimates from scraped postings and move month to month.
- No transition paths (from full-stack, frontend, data engineering or data science). Overlapping steps across roles show where a background already counts.
- Links checked in November 2026, matching the interactive map at https://tomyang1993.github.io/ai-career-paths/.
