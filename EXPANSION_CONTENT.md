# Comprehensive Module Expansion Guide

This file contains expanded content for modules 02-11. You can copy and paste these sections into the respective README files, or use this as a reference for what each module should cover.

## Module 02: Setup and Tooling - EXPANDED

# 02. Setup and Tooling

## Goal of this module

Set up a usable development environment so AI-generated code can be run, tested, and improved without chaos. A sloppy setup leads to mysterious errors later. A good setup means you can focus on learning.

## Recommended local stack

### Required
- **Python 3.11+** (3.12 recommended) - download from python.org
- **Node.js 20+** (not needed if Python-only) - download from nodejs.org
- **Git** (version control) - download from git-scm.com
- **VS Code** (editor) - download from code.visualstudio.com
- **Terminal access** (PowerShell on Windows, Terminal on macOS/Linux)

### Helpful tools
- **Postman** or **Thunder Client** (API testing - easier than curl for beginners)
- **Docker** (containerization - for later, optional now)
- **GitHub Desktop or CLI** (makes git easier - get from github.com/apps)
- **Code formatter**: Prettier (JavaScript) or Black (Python)
- **Linter**: ESLint (JavaScript) or Ruff (Python)

## Development environment strategy

### Why each tool matters

| Tool | Why you need it | Cost |
|------|-----------------|------|
| Python/Node | The languages we code in | Free |
| Git | Track changes, work with others | Free |
| VS Code | Write code with good debugging | Free |
| Postman | Test APIs visually | Free (basic) |
| Terminal | Run code from command line | Free |

### Why VSCode specifically?

- Built-in Git integration
- Integrated terminal
- AI-friendly (GitHub Copilot built in)
- Extensions for every language
- Lightweight compared to full IDEs
- Works on Windows, macOS, Linux

## Step-by-step setup for Windows

### 1. Install Python

```powershell
# Check if Python is installed
python --version

#If not, download from python.org
# During install, **CHECK "Add Python to PATH"**
# This is critical!

# After installation, verify
python --version
pip --version
```

### 2. Install VS Code

- Download from code.visualstudio.com
- Install with default options
- Open VS Code
- Extensions to install immediately:
  - Python (by Microsoft)
  - Pylance (for Python type checking)
  - Git Graph (visual Git history)
  - REST Client (test APIs in VS Code)

### 3. Install Node.js (optional but recommended)

```powershell
# Download from nodejs.org
# Verify installation
node --version
npm --version
```

### 4. Initialize Git

```powershell
# Set your name and email (global, set once)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Verify
git config global user.name
```

### 5. Create your first project folder

```powershell
# Create a folder
New-Item -ItemType Directory -Path C:\Dev\MyFirstApp
cd C:\Dev\MyFirstApp

# Initialize Git
git init

# Create .gitignore
@"
__pycache__/
.venv/
.env
node_modules/
.DS_Store
"@ | Out-File .gitignore

# First commit
git add .
git commit -m "Initial project"
```

## Step-by-step setup for macOS/Linux

### 1. Install Python

```bash
# Check if installed
python3 --version

# If needed, use homebrew (macOS)
brew install python3

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Verify
python --version
```

### 2. Install Node.js (optional)

```bash
# Using homebrew
brew install node

# Verify
node --version
npm --version
```

### 3. Install VS Code

```bash
# Download from code.visualstudio.com or use:
brew install --cask visual-studio-code
```

## Python project setup (most common for this course)

### Create a virtual environment

```bash
# Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS/Linux
python -m venv .venv
source .venv/bin/activate

# You should see (.venv) in your terminal prompt
```

### Activate it every time

If you restart your terminal, reactivate:

```bash
# Windows
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

### Install common packages

```bash
# Update pip first
pip install --upgrade pip

# Install core packages
pip install fastapi uvicorn pydantic python-jose[cryptography] passlib[bcrypt]

# Create requirements.txt for reproducibility
pip freeze > requirements.txt

# Later, someone can install all packages:
pip install -r requirements.txt
```

### Verify it worked

```bash
python -c "import fastapi; print(fastapi.__version__)"
```

## Node.js project setup

### Initialize a new project

```bash
npm init -y

# Install common packages
npm install express jsonwebtoken cors dotenv axios
npm install -D nodemon  # Development only
```

### Create package.json scripts

```json
{
  "scripts": {
    "start": "node src/server.js",
    "dev": "nodemon src/server.js",
    "test": "jest"
  }
}
```

Then run with:

```bash
npm run dev   # Development with auto-reload
npm start     # Production
```

## VS Code configuration

### Recommended settings (Ctrl+,)

``` json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "ms-python.python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "files.exclude": {
    "**/__pycache__": true,
    "**/node_modules": true
  }
}
```

### Recommended extensions quick install

```bash
# Install extensions via command line
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension eamodio.gitlens
code --install-extension humao.rest-client
code --install-extension esbenp.prettier-vscode
code --install-extension dbaeumer.vscode-eslint
```

## Terminal confidence checklist

You should be able to do these without thinking:

- [ ] Navigate folders (`cd`, `ls`/`dir`)
- [ ] Create files and folders (`touch`/`New-Item`, `mkdir`)
- [ ] Read file contents (`cat`, `type`)
- [ ] Run Python (`python script.py`)
- [ ] Run Node (`node script.js`)
- [ ] Install packages (`pip install`, `npm install`)
- [ ] Start a server and see it running
- [ ] Stop a running server (Ctrl+C)
- [ ] Read error messages and understand them
- [ ] Commit to Git (`git add`, `git commit`)

If you can't do all of these, practice before moving to coding.

## Directory structure best practices

```
my-project/
├── .git/                  # Git history (automatic)
├── .venv/                 # Virtual environment (Python)
├── node_modules/          # Installed packages (Node)
├── .gitignore             # Tell Git what to ignore
├── .env                   # Secrets (NEVER commit!)
├── .env.example           # Template for .env
├── README.md              # What this project is
├── requirements.txt       # Python dependencies
├── package.json           # Node dependencies
├── src/ or app/           # Your code
│   ├── main.py
│   ├── routes/
│   └── etc.
└── tests/                 # Test files
    └── test_main.py
```

## Environment variables (.env files)

### Why .env?

Never commit secrets (API keys, passwords, database URLs) to Git.

```bash
# Create .env file
API_KEY=sk_live_abc123
DATABASE_URL=postgresql://user:pass@localhost/db
DEBUG=True

# In your code
import os
api_key = os.getenv("API_KEY")

# Tell Git to ignore it
# Add to .gitignore:
.env
```

### But share a template

```bash
# Create .env.example with empty values
API_KEY=your_key_here
DATABASE_URL=your_url_here
DEBUG=False

# Commit .env.example, not .env
# Others copy it: cp .env.example .env
```

## Common setup errors and fixes

| Error | Cause | Fix |
|-------|-------|-----|
| "python: command not found" | Python not installed or not in PATH | Reinstall with "Add to PATH" checked |
| "pip: command not found" | Pip not installed or wrong Python version | Reinstall Python |
| "No module named 'fastapi'" | Package not installed in active environment | `pip install fastapi` in correct venv |
| ".venv not found" | Venv not created | `python -m venv .venv` |
| "Activate.ps1 cannot be loaded" | PowerShell execution policy too strict | Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |

## Version checking commands

```bash
# Check everything
python --version
pip --version
node --version
npm --version
git --version
code --version

# Check your project's installed packages
pip freeze           # Python
npm list             # Node
```

## Pre-flight checklist

Before you start coding with AI:

- [ ] Primary language installed and working (Python or Node)
- [ ] VS Code installed with Python extension
- [ ] Virtual environment created and activated (Python)
- [ ] Git initialized in your project
- [ ] .gitignore file created
- [ ] First commit made
- [ ] You can open the integrated terminal in VS Code
- [ ] You can run your first hello.py or hello.js
- [ ] You've verified all packages install correctly

## Exercise

### Part 1: Setup verification
Run each of these and screenshot or note the output:

```bash
python --version
pip --version
git --version
node --version    # Optional if Node
npm --version     # Optional if Node
```

### Part 2: Create your first project

```bash
# Create the folder
mkdir my-first-api
cd my-first-api

# Initialize Git
git init

# Create .gitignore
# (copy from above)

# First commit
git add .
git commit -m "Initialize project"

# List Git history
git log
```

### Part 3: Create virtual environment (Python)

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install a package
pip install requests

# See it in requirements.txt
pip freeze > requirements.txt

# Show the file
type requirements.txt  # Windows
# cat requirements.txt  # macOS/Linux
```

### Part 4: Open in VS Code

```bash
# From folder
code .

# Or from VS Code File > Open Folder > select your folder
```

See the folder structure in the Explorer panel. You're ready!

---

## Module 03: Beginner Workflows - EXPANDED

# 03. Beginner Workflows

## Your first reliable workflow

At beginner level, you don't need a huge system. You need a **repeatable loop**:

1. **Define** one small feature
2. **Prompt** for a minimal version with tests
3. **Run** it and verify it works
4. **Read** the error message carefully
5. **Fix** only that specific layer (router, service, database)
6. **Test** the result manually
7. **Commit** progress to Git

This is the **Prompt → Code → Run → Fix → Commit** workflow.

### Why commit often?

Git lets you revert if something breaks badly. Commit after each working feature.

```bash
git add .
git commit -m "Add health check endpoint"
```

## Example feature workflow

### Feature: Health check endpoint

Description:
> Build a `/health` endpoint that returns `{"status": "ok"}` in JSON

Prompt to AI:
```
I'm building a FastAPI app. Create a simple FastAPI application with:
- One GET endpoint at `/health`
- Returns JSON: `{"status": "ok"}`
- Use main.py
- Include instructions to run it
```

Generated code:

```python
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="MyApp")

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Run it

```bash
python main.py
# Or
uvicorn main:app --reload
```

### Test it

In browser or REST Client:
```
GET http://127.0.0.1:8000/health
```

Response:
```json
{"status": "ok"}
```

### Commit it

```bash
git add main.py
git commit -m "Add health check endpoint"
```

## Beginner debugging pattern

When something fails, ask four questions **in order**:

### 1. Is this a **setup error**?
The program won't even start.

Examples:
- `ModuleNotFoundError: No module named 'fastapi'` → Package not installed
- `No such file or directory: main.py` → Wrong folder
- `.venv not found` → Didn't activate virtual environment

Fix: Install missing packages, check file paths, activate venv

### 2. Is this a **syntax error**?
The code is invalid Python/JavaScript.

Examples:
- `SyntaxError: invalid syntax` → Missing colon, wrong indent
- `IndentationError` → Wrong spacing
- `ImportError` → Wrong import statement

Fix: Check the error line number, look at examples

### 3. Is this a **logic error**?
The code runs but gives wrong output.

Examples:
- You POST data but get empty response
- Function returns None instead of value
- Wrong calculation result

Fix: Add print statements, use debugger, trace the flow

### 4. Is this a **contract error**?
The frontend and backend disagree on data shape.

Examples:
- Frontend expects `{name: "John"}`, backend returns `{user_name: "John"}`
- Frontend expects status code 200, gets 400
- Frontend sends JSON, backend expects form data

Fix: Align field names, response codes, and data shapes between frontend and backend

### Debugging workflow

```
Error occurs
  ↓
Is the program running at all?
  Yes → Continue
  No → Setup error
       (install package, check path, activate venv)
  ↓
Is the syntax valid?
  python -m py_compile main.py
  Yes → Continue
  No → Fix syntax
  ↓
Does the logic look right?
  Add print() statements
  Yes → Continue
  No → Fix logic
  ↓
Do frontend and backend shapes match?
  Compare request/response
  Yes → All good
  No → Change one side to match
```

## First mini project: Notes API

A tiny but complete backend.

### Requirements:
- Add a note
- List all notes
- Delete a note
- Notes have title and content

### Design:
- Use in-memory storage (list) for simplicity
- Routes handle HTTP
- Pydantic models validate

### Full starter code

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Notes API")

# Data model
class NoteCreate(BaseModel):
    title: str
    content: str

class Note(BaseModel):
    id: int
    title: str
    content: str

# In-memory storage
notes: List[Note] = []
next_id = 1

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/notes")
def list_notes():
    """Get all notes"""
    return notes

@app.post("/notes")
def create_note(note: NoteCreate):
    """Create a new note"""
    global next_id
    new_note = Note(id=next_id, title=note.title, content=note.content)
    notes.append(new_note)
    next_id += 1
    return new_note

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Get a specific note"""
    for note in notes:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """Delete a note"""
    global notes
    notes = [n for n in notes if n.id != note_id]
    return {"message": "Note deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
```

### Run it

```bash
python main.py
```

### Manual test examples

```bash
# Create a note
curl -X POST http://localhost:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "content": "It is great"}'

# List notes
curl http://localhost:8000/notes

# Delete note 1
curl -X DELETE http://localhost:8000/notes/1

# List notes again
curl http://localhost:8000/notes
```

Or use Postman:
1. POST to http://localhost:8000/notes with JSON body
2. GET http://localhost:8000/notes
3. DELETE http://localhost:8000/notes/1

## Testing your endpoints locally

### Using REST Client extension

Install REST Client in VS Code, create `test.http`:

```http
### Health check
GET http://localhost:8000/health

### Create note
POST http://localhost:8000/notes
Content-Type: application/json

{
  "title": "My Note",
  "content": "This is a test"
}

### List all notes
GET http://localhost:8000/notes

### Delete note
DELETE http://localhost:8000/notes/1
```

Then click the "Send Request" link above each request.

## Error handling basics

### What you should return

| Situation | Status Code | Response |
|-----------|------------|----------|
| Success | 200 | The data requested |
| Created | 201 | The new resource |
| Bad input | 400 | Error message explaining what's wrong |
| Not found | 404 | Error message that resource doesn't exist |
| Server error | 500 | Error message (don't expose internals) |

### Example error handling

```python
from fastapi import HTTPException

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note.id == note_id:
            return note
    
    # Not found - return 404
    raise HTTPException(
        status_code=404,
        detail=f"Note {note_id} not found"
    )

@app.post("/notes")
def create_note(note: NoteCreate):
    # Validation happens automatically with Pydantic
    # If required fields missing, FastAPI returns 400
    # If title is empty string, that's allowed but you could add:
    if not note.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )
    # ... rest of create logic
```

## Common beginner mistakes

| Mistake | What happens | Fix |
|---------|-------------|-----|
| Forget to activate venv | "No module named..." | Always activate before coding |
| POST but code expects GET | 405 Method Not Allowed | Check HTTP method matches |
| Wrong JSON field names | Data not received | Trace field names end-to-end |
| Endpoint at `/notes/` not `/notes` | 404 Not Found | Check URL spelling exactly |
| Forgot `return` statement | Returns None | Add `return` statement |
| Validation too strict | Users can't create items | Relax Pydantic constraints or add error message |

## Workflow checklist

For each feature:

- [ ] Feature goal is clear (one sentence)
- [ ] I wrote a prompt with context
- [ ] AI generated the code
- [ ] Code is in one file (for now)
- [ ] I ran the code and verified it starts
- [ ] I tested one successful case manually
- [ ] I tested one failure case manually
- [ ] Errors are clear and helpful
- [ ] I committed to Git

If all checked, you're following the workflow correctly.

## Exercise

### Part 1: Run the notes API
Copy the full code from above. Save as `main.py`.

```bash
python main.py
```

### Part 2: Test all 4 endpoints manually
Create one note, list notes, delete it, list again.

### Part 3: Break it intentionally
Try to POST without a title field. What error do you get?
Try to DELETE a note that doesn't exist. What happens?

### Part 4: Expand it
Add one new endpoint:
- Search notes by title (GET /notes/search?q=learn)
- Mark notes as favorite (PATCH /notes/{id}/favorite)
- Add created_at timestamp to each note

Write a prompt for AI and generate it.

---

## Module 04: Prompt Engineering - EXPANDED

# 04. Prompt Engineering

## Why prompting matters

AI coding quality is 100% determined by the quality of your prompt.

A bad prompt:
```
Build an auth app
```
Result: Generic, probably wrong, not what you wanted

A good prompt:
```
Build a FastAPI JWT auth backend with register, login, and /me endpoints.
Use: Pydantic models, bcrypt for passwords, JWT tokens.
Return only user_id and email, never the password hash.
Keep routers thin, put business logic in services.
```
Result: Targeted, correct structure, what you actually wanted

### The core truth:
**Specificity in → Specificity out**

Vague prompts get vague results. Detailed prompts get targetted results.

## A practical prompt framework

Use this structure every time:

### 1. Role
Who is the AI acting as?
- "Act as a senior FastAPI engineer"
- "Act as a code reviewer"
- "Act as a security expert"

### 2. Goal
What should be built?
- "Build a JWT auth system"
- "Review this code for SQL injection"
- "Design a scalable API"

### 3. Context
What project is this inside?
- "This is a study planning app"
- "We use FastAPI + SQLite"
- "We've already built user models and registration"

### 4. Constraints
What must or must not happen?
- "Use FastAPI only, no Django"
- "Keep functions under 30 lines"
- "Do not use external services"

### 5. Output format
How should the answer be returned?
- "File by file with explanation"
- "Include a data flow diagram"
- "List potential failure modes"
- "Include curl commands to test"

## Weak vs strong prompt: Full examples

### Example 1: Simple endpoint

**Weak:**
```
Build a login endpoint
```

**Strong:**
```
Act as a senior FastAPI engineer.

Goal:
Build a login endpoint that authenticates users and returns JWT tokens.

Context:
- Stack: FastAPI, SQLite, Pydantic
- We have a User model with email and password_hash
- We use python-jose for JWT

Constraints:
- Hash incoming password with bcrypt and compare to stored hash
- Return 401 if credentials invalid (don't say which one failed)
- Token should expire in 24 hours
- Return only the token, not user details

Output:
1. Explain the logic flow
2. Write the endpoint function
3. Show one curl example testing it
4. List security checks you included
```

### Example 2: Refactoring

**Weak:**
```
Make this code better
```

**Strong:**
```
Act as a code reviewer focused on maintainability.

Code:
[paste the code]

Goal:
Improve this code for clarity and performance.

Constraints:
- Preserve the same behavior
- Keep it FastAPI-focused (don't change frameworks)
- Reduce function length to under 30 lines

Issues to consider:
- N+1 database queries?
- Duplicated logic?
- Unclear variable names?

Output:
1. List problems you found
2. Show the refactored version
3. Explain what changed and why
```

### Example 3: Debugging

**Weak:**
```
This is broken, fix it
```

**Strong:**
```
Act as a debugging expert.

Problem:
When I POST to /register with valid email and password, I get a 422 error.

Expected:
User should be created and I should get back the user ID.

Environment:
- FastAPI, SQLite, running locally
- Database is created and working (health check returns 200)

Code:
[paste your register route]

Tasks:
1. Find the root cause
2. Explain why it's happening
3. Provide the minimal fix
4. Show one test case to verify it works
```

## Prompt template you can reuse

Copy and adapt this for every prompt:

```Text
Act as a [role: senior engineer/reviewer/architect/debugger].

Goal:
[What should be built? What should be checked?]

Project context:
- Stack: [Languages, frameworks, databases]
- What's already built: [What exists]
- What needs to happen: [The goal]
- Constraints:
  - [Constraint 1: e.g., use FastAPI only]
  - [Constraint 2: e.g., keep functions under 30 lines]
  - [Constraint 3: e.g., never hardcode secrets]

Output:
1. [Explain the approach]
2. [Generate code/review/design]
3. [Include test examples]
4. [List edge cases or risks]
```

## Prompting by development stage

### Stage 1: Planning
Ask for:
- Architecture diagram
- List of files to create
- Data flow diagram
- Endpoint specifications

Example:
```
Act as a system architect.

Design a task management API with these features:
- Users register and login
- Users create tasks with title, description, due date
- Users see dashboard with completed/incomplete tasks

Questions:
- What entities do we need?
- What endpoints?
- What data flows?
```

### Stage 2: Implementation
Ask for:
- File generation
- One file at a time explanations
- Tests for critical paths

Example:
```
Act as a FastAPI builder.

Build the __init__.py file for the routers package.
Context: We have auth.py and tasks.py router files.
Show how to import them and register with the main app.
```

### Stage 3: Debugging
Ask for:
- Root-cause analysis
- Exact patch to fix
- Explanation of why the bug existed

Example:
```
Act as a debugger.

The /tasks endpoint returns 401 even with a valid token.
Here's the auth middleware and the endpoint.
Find the bug, explain it, and show the fix.
```

### Stage 4: Refactoring
Ask for:
- Code improvements
- Duplication removal
- Complexity reduction with same behavior

Example:
```
Act as a refactor expert.

This function has too many nested ifs and duplicated queries.
Refactor it to be cleaner while keeping the same behavior.
[paste code]
```

## Anti-patterns: Prompts that DON'T work

### Anti-pattern 1: Too vague
```
✗ Build an app
✗ Make it better
✗ Add authentication
```

Rule: Be specific about WHAT, HOW (framework), and CONSTRAINTS

### Anti-pattern 2: Too long
```
✗ [5 pages of rambling description]
```

Rule: 3-5 sentences is ideal. Focus only on what's needed.

### Anti-pattern 3: Contradicting
```
✗ Use FastAPI and also use Django
✗ Keep it simple but also make it production-ready
```

Rule: Pick one. Say "basic version first, production later"

### Anti-pattern 4: No context
```
✗ Build a POST endpoint (but which project? what does it do?)
```

Rule: Always include stack and what's already built

### Anti-pattern 5: Asking for explanation without code
```
✗ Explain how to build authentication
```

Rule: Ask for actual code, not essays

## Iteration loop: Refining prompts

### Round 1: Initial attempt
```
Build a register endpoint for FastAPI.
```
Result: Works but weak validation

### Round 2: Add constraints
```
Build a register endpoint with:
- Email validation  
- Password min 8 chars, 1 uppercase
- Return only user_id and email

## Round 3: Add error handling
```
Same as round 2, plus:
- Return 400 with field-specific error messages
- Return 409 if email already exists
```

### Round 4: Add security
```
Same as round 3, plus:
- Don't reveal whether email exists if you want privacy
- Use bcrypt for password hashing with 12 rounds
- Log failed attempts
```

Each iteration improves the result.

## Common prompting mistakes

| Mistake | Why | Fix |
|---------|-----|-----|
| Asking for too much at once | AI outputs aren't coherent | Break into smaller prompts |
| Not providing context | AI makes random choices | Always include stack and backstory |
| Changing frameworks mid-project | Code conflicts | Decide on stack FIRST, stick with it |
| Not asking for explanations | You don't understand the result | Always ask "explain each file" |
| Being too polite | AI might misunderstand | Be direct: "Generate code" not "Could you maybe try..." |
| Expecting perfection | First draft is rarely production-ready | Plan for iteration |

## Chaining prompts for complex topics

Don't ask for everything at once. Ask in stages:

### Example: Building a complete auth system

**Prompt 1:**
```
Design the data models for a user with JWT auth.
Include User model with email, password_hash, created_at.
Show how tokens work conceptually.
```

**Prompt 2:**
```
Based on the design from above, write the register endpoint.
Hash passwords with bcrypt, validate email format.
```

**Prompt 3:**
```
Based on the design, write the login endpoint.
Return a JWT token that expires in 24 hours.
```

**Prompt 4:**
```
Based on the design, write middleware to verify JWT tokens.
Extract user_id from token and make available to routes.
```

**Prompt 5:**
```
Now show a protected route that uses the middleware.
Example: GET /me returns the current user.
```

Each prompt builds on the previous. Much better than asking for everything once.

## Pro tips for prompt mastery

1. **Use your project brain in every prompt**
   - Share relevant existing code
   - Reference your naming conventions
   - Maintain consistency automatically

2. **Ask for "show your work"**
   - "Explain each step of the algorithm"
   - "Show the data flow"
   - "List edge cases"

3. **Request test examples**
   - "Include one curl command to test this"
   - "Show what happens if I send invalid data"

4. **Use roles strategically**
   - Architect for design decisions
   - Builder for implementation
   - Reviewer for quality checks
   - Debugger for problems

5. **Iterate, don't iterate blindly**
   - Try the first version
   - Find what's wrong
   - Refine the prompt based on problems
   - Regenerate

## Exercise

### Part 1: Weak vs Strong prompts
For "build a login endpoint", write three versions:

1. **Too vague** (like beginners write)
2. **Medium** (better but missing details)
3. **Strong** (complete with all context)

Try each with Claude Code. Compare the results.

### Part 2: Prompt for YOUR project
Pick a feature you want to build: Maybe "create a task" or "list users" or "delete comment"

Write a strong prompt using the template.

Include:
- Role
- Goal
- Stack and context  
- Constraints (3-5)
- Output format

### Part 3: Chain three prompts
Plan "add authentication" for your app as three separate prompts:

1. Prompt for design/models
2. Prompt for register endpoint
3. Prompt for login endpoint

Run them in sequence. Notice how each builds on the last.

### Part 4: Iterate on one prompt
After generating code from your Part 2 prompt:
- Find ONE thing you don't like
- Refine the prompt based on that feedback
- Regenerate
- Compare the results

Notice: iteration improves quality significantly.

---

[Continuing with modules 05-11 in next section...]

