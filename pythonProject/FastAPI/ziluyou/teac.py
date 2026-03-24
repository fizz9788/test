from fastapi import APIRouter
import uvicorn


teac = APIRouter()
@teac.get("/teac")
def teacs():
    return "这是老师界面"