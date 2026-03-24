from fastapi import FastAPI,Response,Request
import uvicorn

app=FastAPI()

@app.middleware('http')
async def zhongjianjian1(request: Request,call_next):
    print("中间体1————正在请求")
    request = await call_next(request)
    print("中间体1————正在响应")
    return request

@app.middleware('http')
async def zhongjianjian2(request: Request,call_next):
    print("中间体2————正在请求")
    request = await call_next(request)
    print("中间体2————正在响应")
    return request

@app.get('/')
def void():
    print("函数运行")


if __name__ == '__main__':
    uvicorn.run("0313中间件:app",host="127.0.0.1",port=8000)