# #创建一个新的fastApi文档
# 字段： order_id(订单id),order_price(订单金额), category(品类),user_id(用户)
# 1.实现通过/order 路径 查看所有订单
# 2.通过/order/路径参数  查看指定id的订单 并对路径参数进行长度校验
# 3. 通过/order_info/?个数  完成查询参数的操作，实现分页查询
# 4. 实现添加订单的功能，并进行请求体校验（规则自定义）
# 5. 对添加订单进行枚举类验证，商品类别只能为  家电、服饰、生鲜
# 6. 实现查询所有订单金额总额的接口
# 7. 实现删除某个订单的功能
from fastapi import  FastAPI,Path,Query,HTTPException
import uvicorn
from pydantic import BaseModel, Field, field_validator
from typing import List
from enum import Enum

app = FastAPI()
order1={'order_id':1,'order_price':500,'category':'家电','user_id':1}
order2={'order_id':2,'order_price':80,'category':'服饰','user_id':1}
order3={'order_id':3,'order_price':25,'category':'生鲜','user_id':1}
order4={'order_id':4,'order_price':600,'category':'家电','user_id':2}
order5={'order_id':5,'order_price':66,'category':'服饰','user_id':2}
order6={'order_id':6,'order_price':15,'category':'生鲜','user_id':2}
order7={'order_id':7,'order_price':788,'category':'家电','user_id':3}
order8={'order_id':8,'order_price':68,'category':'服饰','user_id':3}
order9={'order_id':9,'order_price':16,'category':'生鲜','user_id':3}


orders=[order1,order2,order3,order4,order5,order6,order7,order8,order9]

class Order_Category(str,Enum):
    jiadian='家电'
    fushi='服饰'
    shengxian='生鲜'


class order(BaseModel):
    order_id:int=Field(le=1000,ge=1)
    order_price:float=Field(le=10000,ge=0)
    category:Order_Category
    user_id:int=Field(le=1000,ge=1)

    # 自定义请求体验证（对order_id）
    @field_validator('order_id')
    def check_id(cls, v):
        order_ids = [i['order_id'] for i in orders]
        if v in order_ids:
            raise ValueError(f"对不起，订单id已经存在")
        return v

@app.get('/order')
def get_allorder():
    return orders

@app.get('/order/{order_id}')
def get_order(order_id:int=Path(le=1000,ge=1)):
    for i in orders:
        if i['order_id']==order_id:
            return i
    return "未找到该订单"

@app.get('/order_info')
def get_order_info(y:int=Query(le=3,ge=1),h:int=Query(le=5,ge=1)):
    start=(y-1)*5
    end=start+h
    if start >= len(orders):
        return {"code": 200, "msg": "暂无更多数据", "data": []}
    return orders[start:end]



@app.post('/add_order')
def add_order(neworder:order):
    order_dict = neworder.model_dump()#因为order继承了BaseModel，所以要用用model_dump()将Pydantic对象转为字典
    orders.append(order_dict)
    return orders

@app.get('/sum_order_price')
def sum_order_price():
    allprice=0
    for i in orders:
        allprice+=i['order_price']
        break
    return allprice

@app.delete('/delete_order/{delete_order_id}')
def delete_order(delete_order_id:int=Path(le=1000,ge=1)):
    target_order=None
    for i in orders:
        if i['order_id']==delete_order_id:
            target_order=i
    if not target_order:
        raise HTTPException(status_code=404, detail=f"订单ID {delete_order_id} 不存在，无法删除")
    orders.remove(target_order)
    return orders

if __name__ == '__main__':
    uvicorn.run('0311作业:app', host='127.0.0.1', port=8002)
