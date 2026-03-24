'''
以下内容都由一个.py文件完成

1.定义一个注册功能(表单)，需要用户的id,姓名,密码和头像
注册成功以后，返回 id,姓名,头像地址 （需要响应体验证）

2.定义一个头修改头像的功能，上传成功并且需要修改原本用户的像地址

3.根据用户id修改用户密码，并且进行请求体验证，密码长度不能低于5位，不能超过16位

4.实现一个功能用，通过/show_user 路径直接返回所有户的id和所有用户的姓名(通过响应体模型验证)

5.以上所有内容都需要完成http异常处理

'''

from fastapi import APIRouter, HTTPException,File,UploadFile,Form
import uvicorn
from pydantic import BaseModel
from typing import List

works_0312 = APIRouter()

users=[]

class user_info_output(BaseModel):
    id: int
    name: str
    touxiang:str

class User(BaseModel):
    id: int
    password: str=File(min_length=5,max_length=16)


@works_0312.post('/create_user',response_model=user_info_output)
def create_user(
        id:int=Form(),
        name:str=Form(),
        password:str=Form(min_length=5,max_length=16),
        touxiang:UploadFile=File()
):
    for i in users:
        if i['id'] == id:
            raise HTTPException(status_code=409,detail="该id已存在")

    content=touxiang.file.read()
    if not content:
        raise HTTPException(status_code=400, detail="头像文件为空")
    with open(f"{touxiang.filename}",'wb') as f:
        f.write(content)
    new_user={'id':id,'name':name,'password':password,'touxiang':touxiang.filename}
    users.append(new_user)
    return {'id':id,'name':name,'touxiang':touxiang.filename}


@works_0312.post('/change_touxiang')
def change_toux(
        id:int=Form(),
        touxiang:UploadFile=File()
):
    for i in users:
        if i['id'] == id:
            content=touxiang.file.read()
            with open(f"{touxiang.filename}",'wb') as f:
                f.write(content)
            i['touxiang']=touxiang.filename
            return {"code": 200, "msg": f"{id}头像替换成{touxiang.filename}"}

    raise HTTPException(status_code=404,detail=f"未找到该id:{id}")


@works_0312.post('/change_password')
def change_password(user:User):
    for i in users:
        if i['id'] == user.id:
            i['password']=user.password
            return {'code':200,'msg':f'{user.id}密码修改成功'}
    raise HTTPException(status_code=404,detail=f"未找到id:{user.id}")

class get_user(BaseModel):
    id:int
    name:str

class List_get_user(BaseModel):
    userlist:List[get_user]

@works_0312.get('/show_user',response_model=List_get_user)
def get_user():
    user_list=[{'id':i['id'],'name':i['name']} for i in users]
    if not user_list:
        raise HTTPException(status_code=404,detail="还没有存储任何用户信息")
    return {"userlist":user_list}


if __name__ == '__main__':
    uvicorn.run("0312作业:app",host="127.0.0.1",port=8000)