from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .core.security import decode_token

bearer_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    try:
        payload = decode_token(token)
        return {"id": int(payload["sub"]), "email": payload["email"]}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
