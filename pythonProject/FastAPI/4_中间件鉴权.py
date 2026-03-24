import uvicorn
from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse
app = FastAPI()


@app.middleware('http')
async  def  middleware1(request:Request,call_next):

    if not request.client.host =='127.0.0.1':
        return  JSONResponse(status_code=404,
                             content= {"result":"对不起，你不是我本机"})
    if not request.headers.get("sec-ch-ua-platform") == '\"Windows\"':
        return JSONResponse(status_code=401,
                            content={"result": "对不起，你不是尊贵的Windows机主"})
    response = await call_next(request)  # 4
    print("中间件1--正在响应") #6
    return response



@app.get('/info')
async  def stus():  #5
    print("函数正在运行")
    return "我是张朝辉，我强的可怕"

@app.get('/onfo')
async  def stus():  #5
    print("函数正在运行")
    return "我是张朝辉，我强的可怕"


if __name__ == '__main__':
    uvicorn.run("4_中间件鉴权:app",host='127.0.0.1',port=8020)