# 09. Debugging and Optimization

## Definition: Debugging

Debugging is the process of identifying, understanding, and fixing the real cause of a problem in software.

Good debugging is not random trial and error.
It is structured investigation.

---

## Definition: Optimization

Optimization is the process of improving software quality in areas like:
- speed
- memory use
- maintainability
- clarity
- scalability

Optimization does not always mean “make it faster”.
Sometimes the best optimization is making code easier to understand and safer to change.

---

## The professional debugging loop

### 1. Reproduce
Can you trigger the bug consistently?

### 2. Isolate
Which layer is actually failing?

### 3. Inspect
Look at code, logs, payloads, and assumptions.

### 4. Patch
Apply the smallest fix that addresses the root cause.

### 5. Verify
Retest the original issue and a nearby edge case.

---

## Types of bugs

### Syntax bug
The code will not run.

### Runtime bug
The code starts, but crashes during execution.

### Logic bug
The program runs, but the result is wrong.

### Contract bug
Different parts of the system disagree about shapes or behavior.

### Performance bug
The result is correct, but too slow or too heavy.

---

## Example: auth bug

Problem:
- login returns a token
- protected route returns 401

Potential causes:
- token not sent correctly
- wrong `Bearer` format
- decode secret mismatch
- expired token
- dependency extracting user incorrectly

This example teaches why debugging should start with the actual contract.

---

## Optimization checklist

### Backend
- keep responses small
- avoid repeated work
- validate early
- paginate long lists
- separate slow jobs from request path

### Frontend
- avoid unnecessary rerenders
- load only what the page needs
- split large bundles when useful

### Code quality
- remove dead code
- simplify long condition chains
- rename unclear variables
- reduce duplication

---

## AI debugging prompt template

```text
Act as a senior debugger.

Bug:
[exact bug]

Expected behavior:
[what should happen]

Current behavior:
[what actually happens]

Relevant code:
[paste the relevant code]

Tasks:
1. identify root cause
2. explain it clearly
3. return a minimal patch
4. suggest one test to prevent recurrence
```

---

## Best practices

- fix one cause at a time
- keep notes while debugging
- verify before and after
- prefer evidence over guesswork

---

## Common mistakes

- changing too many things at once
- calling something “fixed” without retesting
- optimizing before measuring any real bottleneck
- trusting AI fixes without understanding what changed

---

## Exercise

Take one project from `projects/`.
Introduce:
- one bug
- one inefficient pattern

Then document:
- how you found each issue
- what evidence helped
- how you fixed it
