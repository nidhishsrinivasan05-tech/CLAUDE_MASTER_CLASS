# 05. CLAUDE.md Project Brain

## Definition: Project brain

A **project brain** is a shared context file that tells the AI what your project is, how it should behave, and what rules it must follow.

You can think of it as:
- memory
- guardrails
- architecture summary
- style contract

Without it, AI output often becomes inconsistent over time.

---

## Why this file matters

In longer projects, the same AI may otherwise:
- forget your folder conventions
- change naming styles randomly
- mix architecture patterns
- reintroduce decisions you already rejected

A project brain reduces that drift.

---

## What to include

### 1. Project purpose
What problem does the project solve?

### 2. Users
Who uses it?

### 3. Stack
What frameworks and tools are allowed?

### 4. Architecture rules
How is the project organized?

### 5. Coding rules
What style and structural standards should be followed?

### 6. Security rules
What should never be done unsafely?

### 7. Current roadmap
What exists, and what is next?

---

## Example

```md
# Project: StudyFlow

## Purpose
A student productivity backend for study sessions and reminders.

## Stack
- FastAPI
- SQLite
- JWT auth

## Architecture
- routers for HTTP handling
- services for business logic
- schemas for validation
- db layer for persistence

## Rules
- keep routers thin
- never store plain passwords
- never hardcode real secrets
- use consistent JSON responses
- explain new modules before generating them

## Current features
- register
- login
- create task
- list tasks
```

---

## Definitions inside the project brain

### Architecture
The high-level structure of the system.

### Convention
A repeated project rule, such as naming files a certain way.

### Source of truth
The most trusted place describing how the system should currently work.

A project brain should become one of your core sources of truth.

---

## How to use it well

- keep it updated
- make it specific
- prefer rules over vague wishes
- reflect real current decisions

---

## Bad project brain example

```md
This project is cool.
Use good code.
Make it professional.
```

This is too vague to guide anything well.

---

## Good project brain style

- short sections
- direct rules
- no contradictions
- stack clearly named
- features clearly listed

---

## Exercise

Create a `CLAUDE.md` for:
- an e-commerce backend
- a student planner
- a small clinic booking system

Then use it to prompt a first module.
Observe how much more consistent the output feels.
