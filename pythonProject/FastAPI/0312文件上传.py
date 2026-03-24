import hashlib

from fastapi import FastAPI, Form, UploadFile, File, HTTPException
from pydantic import BaseModel
import  uvicorn
from typing import List
app= FastAPI()

# #单文件上传
# @app.post('/upload')
# def upload_file(file:UploadFile):
#     concent=file.file.read()
#     with open(f"{file.filename}",'wb') as f:
#         f.write(concent)
#     return "上传成功"


#多文件上传
@app.post('/upload')
def upload_file(file:List[UploadFile]):
    for i in file:
        concent = i.file.read()
        with open(f"{i.filename}", 'wb') as f:
            f.write(concent)

    return "上传成功"



#文件、表单混合上传
users=[]
@app.post('/reg')
def reg_user(
        name:str = Form(),
        sex:str = Form(),
        zhaopian:UploadFile = File()
):
    content=zhaopian.file.read()
    with open(f"{zhaopian.filename}",'wb') as f:
        f.write(content)

    user={"name":name,"sex":sex,"zhaopian":zhaopian.filename}
    users.append(user)
    return {f"注册成功：{user}"}


#md5

# @app.post('/loadFeilf')
# def add_file(file:UploadFile):
#     content=file.file.r   ead()
#     # content 是二进制的文件内容
#     # .md5(参数是一个二进制数据)
#     filename=hashlib.md5(content).hexdigest()
#     with open(f"{filename}.{file.filename.split('.')[1]}",'wb') as f:
#         f.write(content)
#     return "上传完成"


#HTTP异常处理
id=1
class User(BaseModel):
    id:int
    name:str
    age:int
@app.post('/add_user')
def add(user:User):
    if user.id==id:
        raise HTTPException(status_code=409,
                            detail="用户已存在",
                            headers={"aaaa":"bbbb"})
    else:
        return "创建成功"


if __name__ == '__main__':
    uvicorn.run("0312文件上传:app",host="127.0.0.1",port=8000)
