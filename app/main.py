from fastapi import FastAPI

from app.api.routers import users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])


@app.get("/app")
def get_app():
    return {"message": "Hello pets!!!"}
