from fastapi import HTTPException
from ..db.store import users
from ..core.security import hash_password, verify_password, create_access_token

def register_user(email: str, password: str, full_name: str):
    if any(user["email"] == email for user in users):
        raise HTTPException(status_code=400, detail="Email already registered")

    user = {
        "id": len(users) + 1,
        "email": email,
        "password_hash": hash_password(password),
        "full_name": full_name,
    }
    users.append(user)
    return {"id": user["id"], "email": user["email"], "full_name": user["full_name"]}

def login_user(email: str, password: str):
    user = next((u for u in users if u["email"] == email), None)
    if not user or not verify_password(password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user["id"]), "email": user["email"]})
    return {"access_token": token, "token_type": "bearer"}

def get_public_user_by_id(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user["id"], "email": user["email"], "full_name": user["full_name"]}
