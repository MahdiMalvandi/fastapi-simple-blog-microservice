from fastapi import FastAPI, APIRouter
from app.routers import router as blog_app_router


app = FastAPI()


app.include_router(blog_app_router)



