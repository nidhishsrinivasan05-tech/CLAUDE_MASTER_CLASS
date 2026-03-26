# 01. Foundations

## What Claude Code really is

Claude Code is not just “AI autocomplete in a terminal”.
A stronger mental model is this:

- **You** are the architect
- **Claude Code** is the implementation engine
- **Your files** provide memory and constraints
- **Your prompts** direct the work
- **Your validation** makes the result trustworthy

That means good outcomes do not come from asking for random code.
They come from building a repeatable system.

## The AI coding paradigm shift

Traditional software development treated the computer as a blank slate you manually filled with instructions. AI-assisted development inverts this: the AI generates candidate solutions and you guide it toward the right one.

**Key difference**: You're no longer typing every character. You're designing, validating, and improving.

The hard part is *not* getting code written. The hard part is writing code that's:
- maintainable
- secure
- scalable
- aligned with your architecture
- sane enough to change later

AI can help with all of this *if you know what you want*.

## AI Coding vs Traditional Coding

### Traditional flow
1. You think through the design (30% of time)
2. You manually implement everything (60% of time)
3. You debug line by line (7% of time)
4. You refactor later (3% of time)
5. **Time to ship: 8 weeks**

### AI-assisted flow
1. You define intent very clearly (20% of time)
2. You give context, constraints, and architecture (10% of time)
3. The AI generates a draft implementation (5% of time)
4. You validate behavior, structure, and edge cases (30% of time)
5. You improve the prompt and the design in loops (25% of time)
6. You test and refine (10% of time)
7. **Time to ship: 2 weeks**

The biggest difference is **speed of iteration and error recovery**.

In traditional coding, changing core design takes days. With AI, changing your context or constraints takes minutes.

## Four pillars of strong AI coding

### 1. Context
The model must understand:
- **what the project does**: "This is a task management API for students"
- **what stack you use**: "FastAPI, SQLite, JWT auth"
- **what the coding rules are**: "Thin routers, service layer for logic, no DB in routes"
- **what output shape you expect**: "One file at a time with explanation"
- **what you've already built**: "We have auth and user models, now adding tasks"

Without context, the AI makes random choices that conflict later.

Example context that works:
```
This is a FastAPI backend for a study planning app.
Stack: FastAPI, SQLite with SQLAlchemy ORM, JWT via python-jose.
Architecture: routes → services → repos → models.
We've built: users, auth, registration.
We need next: a tasks module with create, list, and mark-complete.
```

### 2. Constraints
Without constraints, AI tends to overbuild or become inconsistent.

Good constraints:
- "Keep functions under 30 lines"
- "Use FastAPI only, no Django"
- "Do not add external APIs yet"
- "Store data in SQLite, not MongoDB"
- "Use Pydantic for all request validation"
- "Never import from routers into services"
- "Return consistent JSON response shapes"

Bad constraints (over-constrained):
- "Use only 3 lines of code"
- "Use no external packages"
- "Build the whole system in one function"

Good constraints prevent consistency drift without dictating how to solve problems.

### 3. Validation
Never treat generated code as correct by default.
Always validate:

**Does it run?**
```bash
python -m pytest
uvicorn app:main --reload
```

**Does it follow the architecture?**
- Are routes thin?
- Is business logic in services?
- Are dependencies injected?

**Does it handle bad input?**
```python
# Test with invalid email, missing fields, SQL injection attempts
POST /auth/register
{"email": "invalid", "password": ""}

POST /auth/register
{"email": "test@test.com'; DROP TABLE users; --", "password": "123"}
```

**Does it leak secrets or unsafe patterns?**
- Hardcoded API keys?
- Unescaped SQL?
- Passwords logged?
- Secrets in error responses?

**Does it match the contract?**
- Right response codes?
- Right field names?
- Right authentication rules?

### 4. Iteration
AI coding works best as a loop, not a one-shot request.

Process:
1. **Define** (20%): Write a clear initial prompt with context + constraints
2. **Generate** (5%): Let the AI create a draft
3. **Validate** (30%): Run it, check it, find problems
4. **Refine** (30%): Change the prompt based on what you learned
5. **Test** (15%): Verify it works in realistic scenarios
6. **Integrate** (10%): Make sure it fits with existing code

Example iteration loop:

**Round 1:**
- Prompt: "Build register endpoint"
- Result: Works but password validation is weak
- Refinement: "Add password validation with min 8 chars, 1 uppercase"

**Round 2:**
- Result: Works but response exposes too much user info
- Refinement: "Return only user_id and email, never password hash"

**Round 3:**
- Result: Works and secure
- Move to next feature

This is normal and expected. First drafts are rarely production-ready.

## Core vocabulary

- **Prompt**: the instruction you give the model
- **Context**: information about your project the AI needs to understand it
- **Constraints**: rules the AI must follow during generation
- **Validation**: checking whether the result is correct and safe
- **Project Brain**: shared context file that guides future outputs (usually `CLAUDE.md`)
- **Scaffold**: initial project structure and files
- **Refactor**: improving code without changing behavior
- **Workflow**: the repeated system you use to ship features consistently
- **Agent role**: a specialized way of instructing AI (architect, builder, reviewer, tester, debugger)
- **Iteration loop**: the cycle of prompt → generate → validate → refine → test

## Beginner mindset shift

**Do not ask:**
```
build me something cool
```

**Ask:**
```
I'm building a task management API.
Stack: FastAPI, SQLite, JWT auth.
Can you create:
1. A register endpoint that hashes passwords with bcrypt
2. A login endpoint that returns a JWT token
3. A /me endpoint to get the current user
Use routes, services, and schemas folders.
Explain each file.
```

That tiny difference changes the quality enormously.

Generic prompts get generic answers. Specific prompts get targeted answers.

## Real-world use case

A student wants to build a task app.

Weak process:
- ask for the whole app in one shot
- copy everything
- get stuck at first error

Strong process:
- define stack and structure
- generate the backend first
- test endpoints
- then add auth
- then add frontend
- then polish and deploy

## Pro tips

- Treat prompts like mini design documents.
- Make AI work in layers: structure first, then features, then polish.
- Ask for explanations after implementation, not before every tiny step.
- Keep a running source of truth in README or project brain files.

## Common mistakes

- asking for everything in one giant prompt
- no folder structure
- no testing
- changing stacks mid-project
- trusting code that has never been run

## Exercise

Write two prompts for the same idea:
1. a weak prompt
2. a strong prompt

Use this feature idea:
- “Task manager API with login and task ownership”
