import uvicorn
from fastapi import FastAPI,Request

app = FastAPI()


@app.middleware('http')
async  def  middleware1(request:Request,call_next):

    print("中间件1--正在请求") #3
    response = await call_next(request)#4
    print("中间件1--正在响应") #6
    return response


@app.middleware('http')
async  def  middleware2(request:Request,call_next):

    print("中间件2--正在请求") #1
    response = await call_next(request) #2
    print("中间件2--正在响应")  #7
    return response

@app.get('/')
async  def stus():  #5
    print("函数正在运行")
    return "我是张朝辉，我强的可怕"


if __name__ == '__main__':
    uvicorn.run("3_中间件:app",host='127.0.0.1',port=8020)