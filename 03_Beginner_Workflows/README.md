# 03. Beginner Workflows

## Definition: Workflow

A **workflow** is the repeatable process you follow to build and improve software.
Beginners often fail not because they are “bad at coding”, but because they have no reliable workflow.

A strong beginner workflow reduces panic and guesswork.

---

## Core beginner loop

### Prompt → Code → Run → Observe → Fix → Re-run

This is the simplest healthy AI-assisted development cycle.

### Step 1: Prompt
Ask for one clear feature.

### Step 2: Code
Generate only the minimum files needed.

### Step 3: Run
Start the app immediately.

### Step 4: Observe
Look at what actually happens, not what you hoped would happen.

### Step 5: Fix
Target the real issue.

### Step 6: Re-run
Verify that the change worked.

---

## Why this loop matters

This loop teaches:
- how software behaves in reality
- how to interpret errors
- how to separate setup problems from code problems
- how to improve prompts using feedback from execution

---

## First practical definition set

### Endpoint
An endpoint is a URL path on your backend that handles a specific action.

Examples:
- `GET /health`
- `POST /auth/login`

### Request
A request is what the client sends to the server.

### Response
A response is what the server returns.

### JSON
JSON is a text format commonly used to exchange structured data.
Example:
```json
{
  "status": "ok"
}
```

### Validation
Validation checks whether input matches expected rules.

---

## Beginner project 1: Health endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

### What this teaches
- creating an app instance
- defining a route
- returning JSON
- testing a running server

### How to run
```bash
uvicorn main:app --reload
```

---

## Beginner project 2: Notes API

This project adds:
- request body parsing
- Pydantic validation
- delete behavior
- 404 handling

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
notes = []

class NoteCreate(BaseModel):
    title: str
    content: str

@app.get("/notes")
def get_notes():
    return notes

@app.post("/notes")
def create_note(note: NoteCreate):
    item = {"id": len(notes) + 1, "title": note.title, "content": note.content}
    notes.append(item)
    return item

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            return notes.pop(i)
    raise HTTPException(status_code=404, detail="Note not found")
```

---

## Definition: In-memory storage

In-memory storage means data is stored in the running program’s memory only.
When the server restarts, the data disappears.

**Why use it in beginner projects**
- keeps learning simple
- focuses on API logic first

**Why it is not enough later**
- data is not persistent
- not appropriate for real production apps

---

## How to think during beginner debugging

When something breaks, ask:

### 1. Did the server start?
If not, it is likely syntax, imports, or environment.

### 2. Is the route correct?
Maybe the method or path is wrong.

### 3. Is the body shape correct?
Maybe the API expects JSON but you sent plain text.

### 4. Is the logic correct?
Maybe the code runs, but the behavior is wrong.

---

## Pro tips

- test after every endpoint
- keep features very small
- prefer many tiny wins over one giant prompt
- write your own small changes after generation

---

## Common mistakes

- adding too many features before testing
- not knowing which file is the entry point
- confusing route path errors with logic errors
- skipping error messages because they “look scary”

---

## Exercise

Take the notes API and add:
- update note
- search notes by title
- return 400 if title is empty

Then write down which part felt easiest and which part felt confusing.
That self-observation is part of becoming better.
