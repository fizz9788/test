from fastapi import  FastAPI,Form
from pydantic import BaseModel
import  uvicorn
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

stu1 = {"id":1,"name":"张亮","age":21,'sex':'男'}
stu2 = {"id":2,"name":"张迪","age":20,'sex':'男'}
stu3 = {"id":3,"name":"董俊","age":8,'sex':'男'}
stu4 = {"id":4,"name":"昂多","age":18,'sex':'女'}
stu5 = {"id":5,"name":"丽莎","age":19,'sex':'女'}
stu6 = {"id":6,"name":"张朝辉","age":18,'sex':'男'}
stus = [stu1,stu2,stu3,stu4,stu5,stu6]
app = FastAPI()

app.mount("/files",StaticFiles(directory='.'),name = 'static')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # 允许所有域名（开发环境用，生产环境指定具体域名）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有请求方法（GET/POST等）
    allow_headers=["*"],
)

@app.post('/create_user1')
def create_user1(id:int = Form(),
                 name:str= Form(),
                 age:int =Form(),
                 sex:str =Form()):
    no = {"id": id, "name": name, "age": age, "sex":sex}
    stus.append(no)
    return stus

if __name__ == '__main__':
    uvicorn.run("0313跨域:app",host='127.0.0.1',port=8010)