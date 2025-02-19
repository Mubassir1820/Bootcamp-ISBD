#main.py
from fastapi import Depends, FastAPI
from core.config import settings
from apis.base import api_router
from db.models.user import User
from repositories.user import UserRepository

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
app.include_router(api_router)

@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI"}

@app.get("/protected")
async def protected_route(current_user: User = Depends(UserRepository.get_current_user)):
   return {"message": f"Hello {current_user.email}, you are authorized!"}