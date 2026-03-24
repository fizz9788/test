#魔法方法
import copy
import time


# class Stu:
#     """
#     这是
#     一段
#     注释
#     """
#     print("对象即将实例化")
#     def __init__(self,name,age,sex):
#         print("对象开始实例化")
#         self.name=name
#         self.age=age
#         self.sex=sex
#         print("对象实例化完成")
#
#     def __str__(self):
#         return f"这是对象字符串"
#
#     def __del__(self):
#         print("对象已释放")
# #
# a=Stu("a",18,"男")
# print(a)
# print(a.__doc__)
# del a
# time.sleep(5)


#多继承




# #深浅拷贝
# #赋值只复制指针，不会新建地址
# a=[1,2,3,4,5]
# b=a
# b[0]=100
# print(a)
# #copy
# #浅拷贝值拷贝一层，列表多层嵌套的话会copy会失效
# c=[1,2,3,[4,5,6]]
# d=c.copy()
# d[3][0]=100
# print(c)
#
# #deepcopy
# #深拷贝会全部拷贝
# e=[1,2,3,[4,5,6]]
# f=copy.deepcopy(e)
# f[3][0]=100
# print(e)
# print(f)


#闭包
# def outer():
#     a=10
#     def inner():
#         nonlocal a
#         a+=1
#         return a
#     return inner
# outer()
# a=outer()
# print(a())
# print(a())
# print(a())
# print(a())

#装饰器 语法糖

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        strat_time=time.time()
        reslut=func(*args,**kwargs)
        # print(func.__closure__)#判断函数是否为闭包函数
        end_time=time.time()
        times=end_time-strat_time
        print(f"函数：{func.__name__}耗时{times:.4f}秒")
        return reslut
    return wrapper
@timer_decorator #语法糖 相当于sum=timer_decorator(sum)
def sum(a):
    sum=0
    for i in range (0,a+1):
        sum+=i
    return sum

print(sum(10000000))

# def login(a):
#     def inner(*args,**kwargs):
#         print("登陆中。。。")
#         a(*args,**kwargs)
#     return  inner
#
# @login
# def order(id,price):
#     print(f"{id}支付了{price}元")
#
# @login
# def follow():
#     print("关注中。。。")
#
#
# follow()
# order("张三",888)
# a=0.12335
# b=0.12345
# c=0.12355
# print(f"{a:.4f}")
# print(f"{b:.4f}")
# print(f"{c:.4f}")

# from decimal import Decimal,ROUND_HALF_UP
# a=Decimal("0.12335")
# b=Decimal("0.12345")
# c=Decimal("0.12355")
# print(a.quantize(Decimal("0.0000"),rounding=ROUND_HALF_UP))
# print(b.quantize(Decimal("0.0000"),rounding=ROUND_HALF_UP))
# print(c.quantize(Decimal("0.0000"),rounding=ROUND_HALF_UP))

# a=lambda j,k:j+k
# print(a(1,2))