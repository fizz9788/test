import uvicorn
from zuoye0311 import works_0311
from zuoye0312 import works_0312
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
app = FastAPI()
app.include_router(works_0311,prefix="/1",tags=['0311作业'])
app.include_router(works_0312,prefix="/2",tags=['0312作业'])

@app.middleware('http')
async def middleware1(request: Request, call_next):
    if not request.client.host=="127.0.0.1":
        return JSONResponse(status_code=401,content= {"result":"对不起，你的ip不为127.0.0.1"})

    response = await call_next(request)
    return response


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)