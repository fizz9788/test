from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Stu(BaseModel):
    no: int
    name: str
    age: int
    sex: str

stus=[]

@app.post("/add_stu")
def add_stu(stu:Stu):
    new_stu={'no':stu.no,'name':stu.name,'age':stu.age,'sex':stu.sex}
    stus.append(new_stu)
    return stus

if __name__ == '__main__':
    uvicorn.run('0311请求体:app', host='127.0.0.1', port=8002)