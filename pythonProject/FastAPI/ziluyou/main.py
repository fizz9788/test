import uvicorn
from stu import stu
from teac import teac
from fastapi import FastAPI

app=FastAPI()
app.include_router(stu, prefix='/stu', tags=['这是我的学生系统'])
app.include_router(teac, prefix='/teac', tags=['这是我的老师系统'])

@app.get("/")
def frist_mune():
    return "学生系统首页"

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000)