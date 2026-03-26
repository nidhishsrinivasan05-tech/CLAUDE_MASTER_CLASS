# FastAPI Auth App File Explanations

## `app/main.py`
Creates the FastAPI app and includes routers.
This is the entry point of the backend.

## `app/core/security.py`
Contains password hashing and JWT creation/decoding logic.
This file centralizes security operations.

## `app/db/store.py`
Simple in-memory lists for users and tasks.
Used only to keep the learning example lightweight.

## `app/deps.py`
Defines `get_current_user`.
This dependency extracts the bearer token, decodes it, and returns the current user identity.

## `app/schemas/auth.py`
Defines request and response models for auth-related operations.

## `app/schemas/task.py`
Defines task creation and task update body shapes.

## `app/services/auth_service.py`
Contains registration and login logic.
This keeps business logic out of routers.

## `app/services/task_service.py`
Contains task CRUD logic for the logged-in user.

## `app/routers/auth.py`
Exposes auth endpoints and connects request bodies to service functions.

## `app/routers/tasks.py`
Exposes task endpoints and applies user authentication through dependencies.
