# 04. Prompt Engineering

## Definition: Prompt engineering

Prompt engineering is the process of designing AI instructions so the output is more accurate, useful, and aligned with your goal.

It is not about magic wording.
It is about **clear specification**.

A strong prompt behaves like a mini engineering brief.

---

## The five-part prompt model

### 1. Role
Who should the AI act as?

Examples:
- senior backend engineer
- code reviewer
- debugging specialist
- product architect

### 2. Goal
What should be built or analyzed?

### 3. Context
Where does this feature live?
What already exists?

### 4. Constraints
What must or must not happen?

### 5. Output
How should the answer be structured?

---

## Why vague prompts fail

Weak prompt:
> create a full app

This fails because it leaves too much undefined:
- what language?
- what framework?
- what architecture?
- what features?
- what output format?
- what level of explanation?

---

## Strong prompt example

> Act as a senior FastAPI engineer.  
> Build a JWT authentication backend with:
> - FastAPI
> - modular folder structure
> - register, login, and `/me`
> - bcrypt password hashing
> - protected route example
> - explanation of each file
> Return the answer file by file and include run instructions.

This works better because it defines:
- role
- stack
- scope
- constraints
- delivery style

---

## Definitions you should know

### Scope
The boundaries of what should be built.

### Constraint
A rule the output must follow.

### Output format
The exact shape in which you want the response.

### Refinement
A follow-up instruction that improves a previous answer.

### Tradeoff
A design compromise, such as simplicity versus scalability.

---

## Prompting by phase

### Planning phase
Ask for:
- architecture
- file tree
- entity list
- API contracts

### Build phase
Ask for:
- file generation
- step-by-step implementation
- tests
- run instructions

### Debug phase
Ask for:
- root cause
- smallest patch
- explanation
- prevention advice

### Refactor phase
Ask for:
- cleaner structure
- duplication removal
- naming improvements
- behavior preservation

---

## Practical prompt templates

### Beginner
```text
Act as a beginner-friendly teacher.
Build a single-file FastAPI app with one GET route and one POST route.
Explain what each part does and how to run it.
```

### Intermediate
```text
Act as a backend engineer.
Build a CRUD API for tasks using FastAPI, routers, schemas, and services.
Return a file tree first, then generate files in order.
```

### Advanced debugging
```text
Act as a senior debugger.

Problem:
The login endpoint returns a token, but protected routes still return 401.

Context:
FastAPI app with JWT auth.

Tasks:
1. identify the root cause
2. explain why it happens
3. return the minimal patch
4. suggest one regression test
```

### Elite architecture
```text
Act as a principal engineer.
Design a full-stack SaaS starter architecture with FastAPI backend, React frontend, JWT auth, and background jobs.
Start with domain entities, then API contracts, then backend folder structure.
```

---

## Best practices

- ask for one layer at a time
- include current code when debugging
- ask for tradeoff reasoning in architecture questions
- request minimal patches when fixing issues
- ask the model to preserve behavior during refactors

---

## Common mistakes

- asking for too much in one prompt
- prompting without showing current code or context
- changing frameworks mid-project
- not telling the model what level of explanation you need

---

## Exercise

Write a prompt for:
1. building a login API
2. reviewing a broken FastAPI route
3. refactoring a large Node route file into smaller modules

Then compare them and identify where role, context, and constraints appear.
