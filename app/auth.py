from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()


# =====================
# USER MODEL
# =====================

class LoginRequest(BaseModel):

    username: str
    password: str


# =====================
# DEMO USERS DATABASE
# =====================

users_db = {

    "admin": {

        "username": "admin",
        "password": "admin123",
        "role": "admin"

    },

    "riya": {

        "username": "riya",
        "password": "riya123",
        "role": "employee"

    }

}


# =====================
# LOGIN API
# =====================

@router.post("/login")

def login(request: LoginRequest):

    user = users_db.get(request.username)

    if not user:

        raise HTTPException(status_code=401, detail="User not found")


    if user["password"] != request.password:

        raise HTTPException(status_code=401, detail="Wrong password")


    return {

        "message": "Login successful",

        "username": user["username"],

        "role": user["role"]

    }