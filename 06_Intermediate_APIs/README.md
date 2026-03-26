# 06. Intermediate APIs

## Definition: API

An **API** in this context is the set of rules and endpoints that allow a client to communicate with your backend.

At beginner level, you learn “route returns data”.
At intermediate level, you learn:
- models
- validation
- modular routing
- auth boundaries
- maintainable project structure

---

## CRUD definition

CRUD stands for:
- **Create**
- **Read**
- **Update**
- **Delete**

These are the four most common operations for persistent data.

Example for tasks:
- create task
- list tasks
- update task
- delete task

---

## Why intermediate structure matters

A single-file app is great for learning.
But as soon as your app grows, everything in one file becomes painful.

That is why intermediate projects introduce layers.

### Common layers

#### Routers
Handle HTTP paths, request methods, and response entry points.

#### Schemas
Validate data shapes using tools like Pydantic.

#### Services
Contain business logic.

#### DB / repository layer
Handle storage access.

#### Core utilities
Contain shared helpers like config, auth, and security.

---

## Example folder structure

```text
app/
├── main.py
├── core/
│   ├── config.py
│   └── security.py
├── routers/
│   ├── auth.py
│   └── tasks.py
├── schemas/
│   ├── auth.py
│   └── task.py
├── services/
│   ├── auth_service.py
│   └── task_service.py
└── db/
    └── store.py
```

---

## Why this split is useful

If login breaks, you can inspect `auth_service.py`.
If request validation breaks, inspect the schema.
If the path is wrong, inspect the router.

This makes debugging and growth more manageable.

---

## Authentication definitions

### Authentication
Proving who the user is.

### Authorization
Checking what the authenticated user is allowed to do.

### JWT
JSON Web Token, a signed token used to identify a client after login.

### Hashing
Turning a password into a secure fixed representation so you do not store the raw password.

---

## JWT practical flow

1. user sends email and password
2. backend verifies credentials
3. backend creates a signed token
4. frontend stores token
5. frontend sends token with protected requests
6. backend verifies token and identifies the user

---

## HTTP status codes you should understand

- `200 OK`: success
- `201 Created`: resource created
- `400 Bad Request`: invalid input
- `401 Unauthorized`: not authenticated or token invalid
- `403 Forbidden`: authenticated but not allowed
- `404 Not Found`: resource does not exist
- `500 Internal Server Error`: unhandled server-side failure

---

## Strong intermediate design questions

Before coding, ask:
- what entities exist?
- what fields do they need?
- what routes are required?
- which routes need auth?
- what validation rules apply?
- what should happen when something fails?

---

## Best practices

- keep route functions small
- move logic into services
- validate inputs at the edge
- return consistent response shapes
- protect private data

---

## Common mistakes

- writing database logic directly inside routes
- duplicating token logic in many files
- returning inconsistent error formats
- skipping authorization checks

---

## Exercise

Design an API for one of these:
- blog posts
- products
- student sessions
- customer tickets

For each one, define:
- entity fields
- CRUD routes
- auth needs
- validation rules
