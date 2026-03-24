from fastapi import  FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List

app=FastAPI()

class Address(BaseModel):
    city:str
    street:str
    community:str

class Stu(BaseModel):
    id:int
    name:str
    age:int
    zhuzhi:List[Address]

class Teacher(BaseModel):
    id:int
    name:str
    salary:int

@app.post('/add_stu')
def add_stu(stu: Stu):

    return stu

if __name__ == '__main__':
    uvicorn.run("0311请求体嵌套:app",host="127.0.0.1",port=8003)