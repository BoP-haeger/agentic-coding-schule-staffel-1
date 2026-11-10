# Agentic Katas — Participant Guide

## What This Session Is About

This isn't a coding exercise. It's a *process* exercise. The thing you build today doesn't matter nearly as much as *how* you build it.

We're practicing **agentic coding** — using AI tools not as autocomplete, but as a thinking partner that helps you explore problems, make decisions, and build with confidence.

Think of this like a code retreat, but instead of practicing TDD or design patterns, you're practicing how to work *with* an AI agent effectively.

---

## The Rules

**Rule 1: Explore before you build.**
You are not allowed to choose a programming language or framework until you've had a conversation with your AI tool about what the best approach is. You should be able to justify your choice.

**Rule 2: Plan before you code.**
Before you write your first line of implementation code, you should have a written plan — even a rough one. This can be a markdown file, notes in your agents.md, or a conversation summary. The plan should cover: what you're building, what libraries/tools you're using, and how you're handling the key requirements.

**Rule 3: Set up your workspace.**
Write an `agents.md` (or `CLAUDE.md`, `.github/copilot-instructions.md` — whatever your tool uses). Think of this as onboarding a new team member. The more context you give your AI upfront, the better its output will be.

**Rule 4: Verify, don't assume.**
Read what the AI generates. Test it. Check that it actually meets the requirements — especially any privacy or security constraints in the brief. The AI is a collaborator, not an oracle.

---

## The Process

This is the loop we're practicing today:

```
Explore → Plan → Set Up Context → Build → Verify
```

### 1. Explore (~15 min)
Read the kata brief. Open a conversation with your AI tool. Ask it questions:
- What are the best approaches for the core technical challenge?
- What libraries exist? What are the tradeoffs?
- What language makes the most sense for this kind of task?
- Where are the requirements deliberately vague? What concrete targets should I set?
- What edge cases should I think about?

### 2. Plan (~5 min)
Write down your approach. It doesn't need to be long. Cover:
- Language and key libraries
- API design (endpoints, input, output, error responses)
- How you'll handle any privacy or security constraints
- Known edge cases and how you'll handle them

### 3. Set Up Context (~5 min)
Create your project. Write your agents.md. Include your plan, your library choices, your constraints. This file is the single most impactful thing you can do to improve your AI tool's output.

### 4. Build (~30–40 min)
Use your agentic tool to implement the service. Give it tasks with context, not just line-by-line completions. When something breaks, ask it to help debug. When you're unsure about an approach, ask it to explain the tradeoffs.

### 5. Verify (~10 min)
Test your service with real input. Try edge cases. Ask your AI to help you write test scripts. Check any privacy or security requirements — is any user data being written to disk or logged when it shouldn't be?

---

## Encoding vs Autocomplete

**Autocomplete looks like:**
> "Build me an [X] server in TypeScript with Express."

You already decided everything. The AI is just typing for you.

**Encoding looks like:**
> "I need to [solve this problem from the brief]. What are my options? What are the tradeoffs between accuracy, speed, and ease of setup?"

You're using the AI to *think*, not just to *type*.

The goal today is to practice encoding.

---

## What You'll Need

- Your preferred agentic coding tool (Claude Code, Copilot, Cursor, Windsurf, etc.)
- A terminal and the ability to install packages
- Test data appropriate to the kata you're working on
- The kata brief (provided by your facilitator or chosen from the Katas directory)

---

## Extra Credit

Every kata brief includes an extra credit extension — a meaningfully harder version of the problem. If you finish early, this is a great reason to run through the explore-plan-build loop a second time. The people who did Phase 1 well will find the extension much easier.

---

*The thing you build is the excuse. The loop is the lesson.*
