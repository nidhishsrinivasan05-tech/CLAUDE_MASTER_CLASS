# 02. Setup and Tooling

## Definition: Development environment

A **development environment** is the collection of tools, runtimes, editors, settings, and terminal commands you use to create software.
If your environment is unstable, even good code becomes hard to build.

That is why environment setup is not a boring side step.
It is the floor your entire workflow stands on.

---

## Main tools in this course

### Python
Python is the language used for the FastAPI examples in this repository.

**Why Python is used here**
- simple syntax
- huge ecosystem
- excellent for APIs, automation, AI, and scripting
- easy to teach and read

### Node.js
Node.js lets you run JavaScript on the server.

**Why Node is included**
- many developers use JavaScript on both frontend and backend
- it is common in web APIs
- it helps you understand a second backend style

### VS Code
VS Code is the editor used most often in beginner to intermediate workflows.

**Why it matters**
- extension support
- integrated terminal
- Git integration
- easy project navigation

### Git
Git is version control.

**Definition**
Version control is a system that records changes over time so you can:
- go back to earlier states
- compare work
- collaborate safely
- avoid losing progress

### Terminal / CLI
CLI means **command-line interface**.

You use it to:
- run scripts
- install dependencies
- start servers
- inspect folders
- control Git

---

## Recommended minimum setup

### Python
Check version:
```bash
python --version
```

### Node.js
Check version:
```bash
node -v
npm -v
```

### Git
Check version:
```bash
git --version
```

### VS Code
Install and open your project folder directly inside it.

---

## Python environment setup explained

### What is a virtual environment?

A virtual environment is an isolated Python space for one project.
It prevents dependency clashes between projects.

**Why beginners should care**
Without it, one project can accidentally break another.

### Create a virtual environment
```bash
python -m venv .venv
```

### Activate on Windows PowerShell
```bash
.venv\Scripts\Activate.ps1
```

### Activate on macOS/Linux
```bash
source .venv/bin/activate
```

When activated, your terminal usually shows `(.venv)`.

---

## Installing backend dependencies

```bash
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] pydantic[email]
```

### What each package does

- `fastapi`: backend framework
- `uvicorn`: ASGI server used to run FastAPI
- `python-jose`: handles JWT token encoding and decoding
- `passlib[bcrypt]`: password hashing
- `pydantic[email]`: request validation, including email types

---

## Node.js setup explained

### Initialize project
```bash
npm init -y
```

This creates `package.json`, the file that records:
- project name
- scripts
- dependencies
- metadata

### Install dependencies
```bash
npm install express jsonwebtoken bcryptjs cors dotenv
```

### Install development dependency
```bash
npm install -D nodemon
```

### What they do

- `express`: minimal Node web framework
- `jsonwebtoken`: token generation and verification
- `bcryptjs`: password hashing
- `cors`: cross-origin request support
- `dotenv`: loads environment variables from `.env`
- `nodemon`: restarts your app automatically during development

---

## VS Code extensions and why they help

- **Python**: language support and execution
- **Pylance**: better Python analysis
- **ESLint**: helps catch JavaScript issues
- **Prettier**: code formatting
- **GitLens**: improved Git visibility
- **Error Lens**: makes errors more visible in editor
- **Thunder Client / REST Client**: quick API testing

---

## Folder hygiene

A good project folder usually contains:
```text
project-name/
├── app/ or src/
├── tests/
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt or package.json
└── notes/
```

**Definition: `.gitignore`**
A file telling Git which files should not be tracked.

Typical ignored files:
- virtual environments
- `node_modules`
- logs
- OS-generated junk files
- real secret environment files

Example:
```gitignore
.venv/
node_modules/
__pycache__/
.env
```

---

## Best practices

- keep one project per folder
- keep README instructions close to the code
- create `.env.example` for variable names
- avoid hardcoding secrets
- verify setup before generating more code

---

## Common mistakes

- forgetting to activate the virtual environment
- running commands from the wrong folder
- installing packages but not recording them
- copying code without understanding how to run it
- mixing incompatible versions

---

## Manual exercise

Create a clean folder from scratch:
1. `mkdir my-fastapi-lab`
2. create `.venv`
3. install FastAPI
4. create `main.py`
5. run it
6. create `README.md` with run instructions

When you can do this without guessing, your setup skill is becoming reliable.
