from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def get_users():
    user_a = "Kaleb"
    return [{"username": user_a}, {"username": "Guilherme"}]


@router.get("/me")
async def read_user_me():
    return {"username": "xabliu"}


@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}

