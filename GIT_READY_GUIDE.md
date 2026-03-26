# Git Ready Guide

This file explains how to turn this ZIP into a normal Git repository.

## Step 1: Extract the ZIP
Extract the archive into a folder on your computer.

## Step 2: Open the folder in VS Code
Open the folder named `claude_code_course_repo`.

## Step 3: Initialize Git
```bash
git init
```

## Step 4: Create your first commit
```bash
git add .
git commit -m "Initial expanded Claude Code course repo"
```

## Step 5: Create a GitHub repository
Create a new empty repository on GitHub.

## Step 6: Connect your local repo to GitHub
```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git branch -M main
git push -u origin main
```

## Step 7: Keep learning in commits
Good commit ideas:
- `add fastapi auth improvements`
- `expand prompt engineering notes`
- `add line by line project explanations`
- `document jwt authentication flow`

## Best practices
- commit after each stable improvement
- do not commit secrets
- write clear commit messages
- keep README files updated when code changes
