from fastapi import APIRouter, Depends
from ..schemas.auth import RegisterRequest, LoginRequest
from ..services.auth_service import register_user, login_user, get_public_user_by_id
from ..deps import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(payload: RegisterRequest):
    return register_user(payload.email, payload.password, payload.full_name)

@router.post("/login")
def login(payload: LoginRequest):
    return login_user(payload.email, payload.password)

@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return get_public_user_by_id(current_user["id"])
