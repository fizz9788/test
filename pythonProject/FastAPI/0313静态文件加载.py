import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/files',StaticFiles(directory=r"C:\Users\Windows\PycharmProjects\pythonProject\FastAPI"),name="static")


@app.get('/')
async  def  first_menu():
    return "你好，我是张朝辉"


if __name__ == '__main__':
    uvicorn.run("0313静态文件加载:app",host="127.0.0.1",port=8001)