# 07. Advanced: Agents and Worktrees

## Definition: Agent role

In AI-assisted development, an **agent role** is a specialized perspective you ask the model to take.

Examples:
- architect
- builder
- debugger
- reviewer
- refactorer
- tester

You are not literally creating five separate minds here.
You are structuring the work so each pass has a different job.

---

## Why this matters

Without role separation, the AI may:
- build without planning
- refactor without preserving behavior
- review without context
- debug without isolating the actual failure

Role separation creates cleaner thinking.

---

## Common role breakdown

### Architect
Plans structure, entities, routes, and boundaries.

### Builder
Implements the planned structure.

### Reviewer
Critiques code quality, clarity, maintainability, and risk.

### Tester
Defines edge cases and verification scenarios.

### Refactorer
Improves the code without changing what it does.

---

## Example advanced workflow

1. Architect defines auth module shape.
2. Builder generates files.
3. Reviewer checks for security issues.
4. Tester suggests invalid token and wrong password cases.
5. Refactorer improves naming and reuse.

This is much more powerful than “build auth system” in one prompt.

---

## Definition: Git worktree

A **Git worktree** lets you check out multiple branches into separate folders at the same time.

That means you can work on:
- auth in one folder
- dashboard in another
- stable main version in the original folder

without repeatedly switching branches in place.

---

## Why worktrees are useful

They help when:
- multiple features are in progress
- you want parallel experiments
- you want AI to work in a focused feature scope
- you want less branch-switch chaos

---

## Worktree commands

Create a new worktree:
```bash
git worktree add ../feature-auth feature/auth
```

List worktrees:
```bash
git worktree list
```

Remove a worktree:
```bash
git worktree remove ../feature-auth
```

---

## Real-world example

Imagine you are building:
- login feature
- admin dashboard
- API cleanup

Using worktrees, you can keep each effort isolated.
That isolation makes both humans and AI less likely to mix unfinished work together.

---

## Advanced debugging pattern

When debugging with AI, provide:
- exact bug
- expected behavior
- current behavior
- relevant files
- what you already tested

This shifts the AI from guessing to analysis.

---

## Best practices

- keep one clear purpose per worktree
- name branches and folders clearly
- use reviewer prompts before merging
- summarize decisions back into your project brain

---

## Common mistakes

- too many worktrees with no naming discipline
- forgetting which folder belongs to which branch
- using advanced agent roles without shared context
- refactoring without tests or manual verification

---

## Exercise

Choose a project in `projects/`.
Pretend you are improving it professionally.

Do this sequence:
1. architect prompt for a new feature
2. builder prompt to implement it
3. reviewer prompt to critique it
4. tester prompt for edge cases
5. refactorer prompt to clean it up
