from fastapi import APIRouter

stu=APIRouter()
@stu.get("/stu")
def stus():
    return "这是学生界面"