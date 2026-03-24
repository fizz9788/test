#json
import json

import os

# f_path=input("请输入需要创建的文件路径")
# f_list=f_path.split("/")
# new_path=""
# for i in f_list[:-1]:
#     new_path+=i+'/'
# if not os.path.exists(new_path):
#     os.makedirs(new_path)
# with open(f_path,'w',encoding='utf-8') as f:
#     f.write('我是真牛逼')

# with open ('stu.json','r+',encoding='utf-8') as f:
#     lines=f.readline()
#     print(type(lines))
#     new_line=json.loads(lines)
#     print(new_line)
#     print(type(new_line))
#     for i in new_line:
#         if i["name"]=="张亮":
#             i["女朋友"]="迪丽热巴"
#     f.seek(0)
#
#     write_line=json.dumps(new_line,ensure_ascii=False)
#     f.write(write_line)

# with open("aaa.json","r",encoding="utf-8") as f:
#     a=[1,2,3,4,5]
#     # json.dump(a,f)
#     # line=f.readline()
#     b=json.load(f)
#     print(type(b))


#try

# def sum (a,b):
#     return a+b
# try:
#     # with open('ddd.txt','r',encoding='utf-8') as f:
#     #     f.read()
#     sum(aaa)
# except NameError:
#     print("参数名字错误")
#     except FileNotFoundError:
#     print('文件不存在！')
# except TypeError:
#     print("参数不正确")
# except Exception as e:
#     print(str(e))
#     print(type(e).__name__)
# else:
#     print("try没捕获错误会走这")
# finally:
#     print("try是否有错都会走这")
#


#面向对象

# class wolin():
#     class student():
#         def __init__(self, name, age, sex, xueli, school="沃林"):
#             self.name = name
#             self.age = age
#             self.sex = sex
#             self.xueli = xueli
#             self.school = school
#
#         def ziwojieshao(self):
#             print(f"我是{self.school}的{self.sex}同学,我叫{self.name},今年{self.age}岁,学历是{self.xueli}")
#
#     class teach()
#
#
# zl=wolin.student("张亮",18,"男","本科")
# wolin.teach
# zl.ziwojieshao()

# class Car:
#     def __init__(self,name,xinghao,price):
#         self.name=name
#         self.xinghao=xinghao
#         self.price=price
#
#     def xingshi(self):
#         print(f"{self.name}是个{self.xinghao}车型，它的价格是{self.price},他正在行驶")
#
#
# bm=Car("宝马X5","SUV","500000")
# bm.xingshi()


#封装
# class Bank_Card:
#     bank_name="沃林银行"
#     def __init__(self,card_id,yue):
#         self.card_id=card_id
#         self.__yue=yue
#
#     def show_yue(self):
#         print(self.__yue)
#
#     def __modify_yue(self,money):
#         self.__yue += money
#         self.show_yue()
#
#     def add_yue(self,money):
#         self.__modify_yue(money)
#
#
#
#
# a=Bank_Card("1234",1000)
# a.show_yue()
# a.add_yue(300)
# a.add_yue(700)


#继承


# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eat(self):
#         print(f"{self.name}正在吃东西")
#     def sound(self):
#         print(f"{self.name}正在叫")
#
# class dog(Animal):
#     def __init__(self,name,age,pinzhong):
#         super().__init__(name,age)
#         self.pinzhong=pinzhong
#
#
#     def look_door(self):
#         print(f"{self.name}正在看门")
#     def eat(self):                       #父类方法重写
#         print(f"{self.name}边吃边摇尾巴")
#
# class cat(Animal):
#     def catch_mouse(self):
#         print(f"{self.name}正在抓老鼠")
#
#
# dog=dog("旺财",5,"拉布拉多")
# cat=cat("咪咪",3)
# dog.eat()
# dog.look_door()
# dog.sound()
# cat.eat()
# cat.sound()
# cat.catch_mouse()


#多态
# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eat(self):
#         pass
#
# class cat(Animal):
#     def eat(self):
#         print(f"{self.name}正在吃小鱼干")
#
# class dog(Animal):
#     def eat(self):
#         print(f"{self.name}正在啃骨头")
# class chiken(Animal):
#     def eat(self):
#         print(f"{self.name}正在啄米")
#
# def tongyonghanshu(aa):
#     aa.eat()
#
#
# a=cat("咪咪",2)
# b=dog("旺财",3)
# c=chiken("坤坤",4)
#
# tongyonghanshu(a)
# tongyonghanshu(b)
# tongyonghanshu(c)


