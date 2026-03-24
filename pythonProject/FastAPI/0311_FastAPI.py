from fastapi import FastAPI,Path,Query
import uvicorn
import asyncio

app=FastAPI(title="大标题",
description="整体描述信息",
version="0.1.0",
contact={
"name": "Luke Lu",
"email": "luke@example.com",
},
license_info={
"name": "MIT",},)

stu1={'stu_no':1,'name':'张亮','age':19}
stu2={'stu_no':2,'name':'张三','age':19}
stu3={'stu_no':3,'name':'李四','age':21}
stu4={'stu_no':4,'name':'王五','age':21}
stu=[stu1,stu2,stu3,stu4]

# @app.get("/",description="这是一个简单的首页")
# def func ():
#     return stu
#
# @app.get('/stus/{stu_id}')
# def get_stu_id(stu_id:int=Path(ge=1,le=6)):
#     for i in stu:
#         if i['stu_no'] == stu_id:
#             return i
#     return "没找到"
#
# @app.get("/users")
# async def get_users():
#     return {'name':'张三','age':23}
# # uvicorn main:app
#
# @app.get("/items/",tags=["itmes"])
# async def read_itmes():
#     return [{"name": "Item 1"}]
#
# @app.get("/users/",tags=["users"])
# async def read_users():
#     return [{"username": "johndoe"}]

# @app.get('/stu_all')
# def get_all_stu(a):
#     stua=[]
#     for i in stu:
#         if str(i["stu_no"])==a or i["name"]== a or str(i['age'])==a:
#             stua.append(i)
#     if len(stua)!=0:
#         return stua
#     else:
#         return "啥也没有"

#实现分页查询，两个查询参数，一个传第几页，一个传看几行，默认一页五行
txt=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
@app.get("/select")
def select(y:int,h:int):
    s_txt=[]
    for i in range((y-1)*5,(y-1)*5+h):
        s_txt.append(txt[i])
    return s_txt






if __name__ == '__main__':
    uvicorn.run('0311_FastAPI:app', host='127.0.0.1', port=8001)
