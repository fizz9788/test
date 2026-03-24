from fastapi import FastAPI,Path,Query
from pydantic import BaseModel,Field
import uvicorn
app=FastAPI()

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

class Order_out(BaseModel):
    order_id: int
    user_id: int


@app.get("/order/{order_id}",response_model=Order_out)
def get_order(order_id: int):
    for i in orders:
        if i["order_id"] == order_id:
            return {'order_id':i['order_id'],'user_id':i['user_id']}
    return "没找到"



if __name__ == '__main__':
    uvicorn.run("0312响应体:app",host='127.0.0.1',port=8003)