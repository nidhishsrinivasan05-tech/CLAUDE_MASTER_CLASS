# 08. Elite System Design

## Definition: System design

System design is the process of deciding how the major parts of an application fit together and behave under real conditions.

It includes:
- entities
- services
- APIs
- data flow
- security boundaries
- scalability concerns
- deployment assumptions

At elite level, the question is no longer:
> can I write this route?

It becomes:
> what kind of system should this become, and why?

---

## The elite shift

Beginner:
- thinks in files

Intermediate:
- thinks in modules

Elite:
- thinks in systems, contracts, constraints, and growth paths

---

## Four elite lenses

### 1. Product lens
What is the real user problem?

### 2. Architecture lens
How should the app be structured so features stay manageable?

### 3. Reliability lens
How will the system behave when something goes wrong?

### 4. Growth lens
How will the system handle more users, more data, and more features?

---

## Definitions you must know

### Domain
The problem area the software belongs to, such as e-commerce or study planning.

### Entity
A core data object in the domain, such as User, Task, Product, or Order.

### Contract
A clear agreement about how parts of the system interact, such as an API request and response format.

### Boundary
A place where one responsibility ends and another begins.

### Scalability
The ability of a system to handle growth without collapsing in performance or maintainability.

### Observability
The ability to understand what the system is doing through logs, metrics, and traces.

---

## Design from contracts first

Before building, define:
- main entities
- endpoint list
- auth requirements
- response shapes
- failure shapes

This reduces rework dramatically.

---

## Example: study planner SaaS

### Users
- student
- mentor
- admin

### Entities
- User
- StudyPlan
- Session
- Reminder

### Core flows
- user registers
- user creates study plan
- sessions appear on dashboard
- reminders notify the user

### Architecture layers
- React frontend
- FastAPI backend
- auth service
- data storage
- reminder job worker

---

## Elite performance thinking

Do not optimize everything.
Optimize the parts that create real pressure.

Common categories:
- pagination for large lists
- caching repeated reads
- reducing repeated queries
- async handling for slow background tasks
- smaller response payloads

---

## Security thinking

Ask:
- where does auth happen?
- which routes are public?
- which data is sensitive?
- what should never be returned?
- how are secrets stored?

---

## Best practices

- define the smallest valuable version first
- prefer clear contracts over vague “smart behavior”
- design for maintainability, not just speed of first draft
- use AI to compare multiple possible architectures before choosing one

---

## Common mistakes

- overengineering too early
- no clear entity design
- mixing concerns everywhere
- building features before contracts are clear
- ignoring failure cases

---

## Exercise

Design a mini SaaS in one page:
- user type
- main problem
- entities
- main routes
- security needs
- monetization idea
