# FastAPI Auth App

A small but real learning backend showing:
- registration
- login
- JWT token creation
- protected `/me` route
- task CRUD linked to the logged-in user

This project is intentionally small enough to study and modify, but structured enough to teach good habits.

---

## Learning goals

By studying this project, you should understand:
- how FastAPI organizes routes
- what request schemas do
- why services help separate logic
- how JWT tokens are created and verified
- how protected routes identify the current user

---

## Run instructions

```bash
python -m venv .venv
# activate the venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- `http://127.0.0.1:8000/docs`

That Swagger UI page lets you test endpoints visually.

---

## Endpoint overview

### Auth
- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`

### Tasks
- `GET /tasks`
- `POST /tasks`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

### Utility
- `GET /health`

---

## Important definition: Protected route

A protected route is an endpoint that requires a valid authenticated identity before it can be used.

In this project, `/tasks` and `/auth/me` are protected through the dependency in `deps.py`.

---

## Project structure

```text
app/
├── main.py
├── core/
│   └── security.py
├── db/
│   └── store.py
├── deps.py
├── routers/
│   ├── auth.py
│   └── tasks.py
├── schemas/
│   ├── auth.py
│   └── task.py
└── services/
    ├── auth_service.py
    └── task_service.py
```

---

## Study order

Read files in this order:
1. `main.py`
2. `schemas/*`
3. `core/security.py`
4. `deps.py`
5. `services/*`
6. `routers/*`

That order helps the system make sense faster.

---

## Notes

This project uses in-memory storage.
That means data disappears after restart.

That is acceptable for learning, but the next growth step would be replacing `db/store.py` with a real database layer.
