# Node API App

A small Express CRUD API that helps you compare Node-style backend structure with the FastAPI example.

---

## What this project teaches

- how Express defines routes
- how middleware-based backend setup feels
- how simple CRUD can be structured in JavaScript
- how route parameters and JSON bodies work in Node

---

## Run instructions

```bash
npm install
npm run dev
```

Open:
- `http://localhost:3000/health`

---

## Endpoints

- `GET /health`
- `GET /api/products`
- `POST /api/products`
- `PUT /api/products/:id`
- `DELETE /api/products/:id`

---

## Structure

```text
src/
├── server.js
├── data/
│   └── products.js
└── routes/
    └── products.js
```

---

## Definitions

### Middleware
A function that runs during request processing before the final route logic completes.

### Route parameter
A dynamic value inside a path, such as `:id`.

### JSON body
Structured request data sent by the client.

---

## Why compare this with FastAPI?

Because it helps you see:
- same backend concepts
- different syntax
- different framework ergonomics

That comparison strengthens your understanding.
