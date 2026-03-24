import os

import numpy as np

#numpy的属性
# arr=np.arange(12).reshape(3,2,2)
# print(arr)
# print(arr.shape)#结构
# print(arr.ndim)#维度
# print(arr.dtype)#数组元素类型
# print(arr.itemsize)#每个元素占用的字节数
# print(arr.size)#元素个数
# print(type(arr))#数组类型
# np.shape(arr)
# np.ndim(arr)
# np.size(arr)

#numpy的ndarray数组的创建
# a=[[[1,2,3],[4,5,6],[7,8,9]]]
# a=np.array(a)
# print(a)

#数组形成
# a=np.array([1,2,3,4,5,6])
# print(a)
# print(a.dtype)
#
# b=np.array([1.2,2.3,3.4,4.5])
# print(b)
# print(b.dtype)

#zeros、ones、empty

# a=np.zeros((3,4),dtype=np.int64)
# print(a)
# print(a.dtype)
# b=np.ones((3,4))
# print(b)
# print(b.dtype)
# c=np.empty((3,4))
# print(c)
# print(c.dtype)

#arang 创建⼀个⼀维 ndarray 数组。
# a=np.arange(5)#创建1-5的整数ndarray数组
# print(a)
# b=np.arange(1,11,2,dtype=float) #起始，结束，步长，数据类型
# print(b)

#matrix(), 是 ndarray 的⼦类，只能⽣成 2 维的矩阵
# a=np.asmatrix("1 2;3 4") #也可以传入1,2;3,4
# print(a)
# b=np.matrix("1 2;3 4")#也可以传入1,2;3,4
# print(b)

#创建随机数矩阵
# a=np.random.rand(3,4) #创建 0-1区间的 3行4列随机浮点数矩阵
# print(a)
#
# b=np.random.randint(-1,5,size=(3,4))#创建-1-5区间的 3行4列随机整数矩阵
# print(b)
#
# c=np.random.uniform(-1,5,size=(3,4))#创建-1-5区间的 3行4列随机浮点数矩阵
# print(c)

#ndarray的数据类型
# zeros_float_arr=np.zeros((3,4),dtype=np.float64)
# print(zeros_float_arr)
# print(zeros_float_arr.dtype)
#
# zeros_int_arr=zeros_float_arr.astype(np.int64)
# print(zeros_int_arr)
# print(zeros_int_arr.dtype)

#等比数列   创建的是浮点数数组
# a=np.logspace(0,0,10)
# print(a)
# b=np.logspace(0,9,10,base=2)#默认base=10
# print(b)

#等差数列  创建的是浮点数数组
# a=np.linspace(1,10,10)
# print(a)
# b=np.linspace(0,10,5,endpoint=False)#是否包含终止值，默认值为False
# print(b)

#numpy内置函数
# arr=np.array([1.1,2.2,3.3,4.4,5.5,6.6])
# a=np.ceil(arr) #向上取整变成int
# print(a)
# a=np.floor(arr)#向下取整变成int
# print(a)
# a=np.rint(arr)#四舍五入变成int
# print(a)
# a=np.isnan(arr)#判断元素是否为空 最后输出[False False False False False False]
# print(a)
# a=np.multiply(arr,2)#元素相乘,也可以输入两个array
# print(a)
# a=np.divide(arr,2)#元素相除,也可以输入两个array
# print(a)
# a=np.abs(arr)#绝对值
# print(a)
# arr = np.random.randn(2, 3)#生成2行3列的正态分布的数组
# print(arr)
# a=np.where(arr > 0,arr,-1)#筛选元素>0的元素，如果为True则为本身，False则用-1代替
# print(a)

# #统计函数
# arr=np.arange(12).reshape(3,4)
# print(np.mean(arr,axis=0))#平均值
# print(np.max(arr,axis=0))#最大值
# print(np.min(arr,axis=0))#最小值
# print(np.std(arr,axis=0))#标准差
# print(np.argmax(arr,axis=0))#最大值下标
# print(np.argmin(arr,axis=0))#最小值下标
# print(arr)
# print(np.cumsum(arr))#返回一个数组,每个元素是之前元素的总和
# print(np.sum(arr))#所有元素的总和
# print(np.sum(arr,axis=0))#每一列的总和
# print(np.sum(arr,axis=1))#每一行的总和
#
# #比较函数
# arr=np.random.randn(2,3)#用于生成标准正态分布（也叫高斯分布）随机数的函数：均值（μ）= 0，标准差（σ）= 1,数值集中在 0 附近，越远离 0 的数值出现概率越低（符合钟形曲线）
# print(arr)
# print(np.any(arr>0))
# print(np.all(arr>0))
# print(np.all(arr>0,axis=0))
# print(np.all(arr>0,axis=1))
#
# #去重函数
# arr=np.array([[1,2,1],[2,3,4]])
# print(arr)
# print(np.unique(arr))

#排列函数
# arr=np.array([1,4,6,9,2,5,7,2.4,2])
# arr=np.sort(arr)#直接返回升序排列好后的数组
# print(arr)
# arr=np.sort(arr)[::-1]#反转
# print(arr)
#
# arr=np.array([5,3,1,2,4])
# new_arr_sy=np.argsort(arr)#仅仅返回升序排列的索引值，而非排列好后的数组
# print(new_arr_sy)
# new_arr=arr[new_arr_sy]#用索引重新排列
# print(new_arr)

#二维数组排列
# arr=np.array([[3,6,5],
#               [4,1,9]])
#
#
# a=np.sort(arr,axis=0)
# b=np.sort(arr,axis=1)
# print(a)
# print(b)
#
# arr_sy0=np.argsort(arr,axis=0)
# arr_sy1=np.argsort(arr,axis=1)
# print(arr_sy0)
# print(arr_sy1)
# new_arr=np.take_along_axis(arr,arr_sy0,axis=0)
# print(new_arr)
# new_arr=np.take_along_axis(arr,arr_sy1,axis=1) #np.take_along_axis(数组,排列表，排列规则行/列)
# print(new_arr)
#两者相同，用argsort更灵活


# arr=np.random.randint(40,100,size=(10,5))
# print(arr)
# print("取出每个同学的最高分")
# print(np.max(arr,axis=1))
# print("取出每个科目的最低分")
# print(np.min(arr,axis=0))
# print("取出每个同学的总分")
# print(np.sum(arr,axis=1))
# print("取出前3-5位同学的总分")
# print(np.sort(np.sum(arr,axis=1))[-3::])
# print("取出每个同学的前三个成绩")
# print(np.sort(arr,axis=1)[:,2::])
# arr=np.array([[1,2,3],[4,5,6]])
# new_arr=arr[:,1:3]
# print(new_arr)




## 练习1：闭包实现简易计算器

# 要求：用闭包实现一个计算器，支持连续的加法、减法操作（如：calc = calculator(10) → calc('+',5) → 15，calc('-',3) → 12）
def calculator(a):
    sum=a
    def inner(str,b):
        nonlocal sum
        if str=='+':
            sum+=b
        elif str=='-':
            sum-=b
        else:
            pass
        return sum
    return inner

calc = calculator(10)
print(calc('+',5))
print(calc('-',3))

## 练习2：装饰器实现权限校验

# 要求：编写一个装饰器，对函数进行权限校验，只有当用户角色为"admin"时才能执行函数，否则提示"权限不足"。

def check(name):
    def outer(func):
        def inner():
            if name =="admin":
                print("当前用户为admin")
                func()
            else:
                print("权限不足")
        return inner
    return outer

@check("admin")
def admin_run():
    print("程序执行")
@check("user")
def user_run():
    print("程序执行")

admin_run()
user_run()




## 练习3：迭代器实现质数生成器

# 要求：自定义一个迭代器，生成小于100的所有质数。
class Find_Prime_num:
    def __init__(self,end):
        self.end=end
        self.now=1

    def __iter__(self):
        return self

    def __next__(self):
        tmp = 0
        while True:
            if self.now>self.end:
                raise StopIteration
            elif self.now==1:
                self.now+=1
                continue
            elif self.now==2:
                self.now+=1
                return 2
            elif self.now%2==0:
                self.now+=1
                continue
            else:
                statu=True
                for i in range(3,int(self.now**0.5)+1,2):
                    if self.now%i==0:
                        statu=False
                        break
                if statu:
                    tmp=self.now
                    self.now+=1
                    break
                else:
                    self.now+=1
                    continue
        return tmp

a=Find_Prime_num(100)
while True:
    try:
        print(a.__next__())
    except StopIteration:
        break

## 练习4：生成器处理大文件

# 要求：编写一个生成器函数，如果读取一个超大文本文件（如10GB），每次返回一行内容，避免一次性加载文件到内存，要怎么做？

def read_txt(txt_name):
    if not os.path.exists(txt_name):
        with open(txt_name,'w',encoding='utf-8') as f:
            pass
    try:
        with open(txt_name, 'r', encoding='utf-8') as f:
            for i in f:
                yield i.rstrip('\n')
    except StopIteration:
        print("文件读取完毕")

a=read_txt("a.txt")

try:
    while True:
        line = next(a)
        print("读取到：", line)
except StopIteration:
    print("文件读取完毕")


