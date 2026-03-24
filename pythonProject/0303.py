# class Stu:
#     schoolname="沃林"
#     def __init__(self,name):
#         self.name=name
#
#     def A(self):
#         print(f"A:{self.schoolname,self.name}")
#
    # @classmethod #----类方法，是一种绑定到类的方法（而非实力），可以不实例化直接调用。函数里的cls是指的类本身，不能访问init里面的属性
    # def B(cls):
    #     print(f"B:{cls.schoolname}")
#
#     @staticmethod #----静态方法，核心特点是没有默认的类 / 实例上下文参数，本质上就是定义在类内部的普通函数，仅为了代码组织而归属到类中。
#     def C():
#         print("C:引用不到schoolname")
#
    # @property
    # def D(self):
#         return self.schoolname,self.name
#
# a=Stu()
# a.A()
# # Stu.A()---报错
# a.B()
# Stu.B()
# a.C()
# Stu.C()
# # print(a.D())---会报错 a.D不能有括号
# print(a.D)

#迭代器

class MyRange:
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step


    def __iter__(self):
        return self

    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        tmp=self.start
        self.start+=self.step
        return tmp


a=MyRange(1,100,5)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
#
# for i in a:
#     print(i)

#斐波那契数列 用迭代器实现

# class Fbl:
#     def __init__(self,n):
#         self.stat=1
#         self.end=n
#         self.now=0
#         self.index=0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index<=1:
#             self.now=1
#             self.stat=1
#             self.index+=1
#             return 1
#         elif self.index<self.end:
#             tmp=self.stat+self.now
#             self.now=self.stat
#             self.stat=tmp
#             self.index+=1
#             return tmp
#         else:
#             pass
#             # raise StopIteration
#
#
# a=Fbl(10)
# newlist=[]
# for i in a:
#     newlist.append(i)
# print(newlist)

#生成器

def sc():
    print("第一步")
    yield 1
    print("第二步")
    yield 2
    print("第三步")
    yield 3
a=sc()#----sc 是生成器函数（不是生成器对象），next() 要求传入「迭代器 / 生成器对象」，而非函数本身；
next(a)
next(a)
next(a)

import time
#模块和包


