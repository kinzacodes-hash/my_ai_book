from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    progress: dict = {}
    background_profile: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    progress: dict = {}
    background_profile: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Placeholder for user database
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "hashed_password": "fakehashedpassword",
        "email": "test@example.com",
        "full_name": "Test User",
        "disabled": False,
        "progress": {},
        "background_profile": "student"
    }
}

def get_user(db, username: str):
    if username in db:
        return UserInDB(**db[username])
    return None

async def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    # In a real app, hash and compare passwords
    if password != "testpassword": # Placeholder for password verification
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real app, decode JWT and get user from DB
    user = get_user(fake_users_db, "testuser") # Use fake_users_db for now
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return User(**user.dict())

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # In a real app, generate a JWT
    access_token = "fake-access-token" # Placeholder
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

