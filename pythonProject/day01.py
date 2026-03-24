

# print("1111111");
# a=10
# print("2222{1}222",1);

# 1. 定义字符串变量 name ，输出 我的名字叫 ⼩明，请多多关照！
# name = '小明'
# print('我的名字叫%s，请多多关照'%name)
# name =input("请输入你的名字")
# print('我的名字叫%s，请多多关照'%name)
# 2. 定义整数变量 student_no ，输出 我的学号是 000001
# student_no = 1234
# print(f'我的学号是{student_no:06d}')
#sno=int(input("请输入你的学号"))
# print('我的学号是%06i'%sno)

# 3. 定义⼩数 price 、 weight 、 money ，输出 苹果单价 9.00 元／⽄，购买了 5.00 ⽄，需要⽀付 45.00 元
# price=9.00
# weight=5.00
# money=price*weight
# print(f'苹果单价{price:.2f}元一斤，购买了{weight:.2f}斤，需要支付{money:.2f}元')
# print('苹果单价%.2f元一斤，购买了%.2f斤，需要支付%.2f元'%(price,weight,money))

# price=float(input('请输入苹果单价'))
# weight=float(input('请输入苹果重量'))
# print('苹果单价%.2f元/斤，购买了%.2f斤，总计%.2f元'%(price,weight,price*weight))
import math
import random
import time

# def sleepTime():
#     for i in range (1,6):
#         print('.',end='')
#         time.sleep(0.3)
#     print('')
#
#
# print('性感张亮在线猜拳')
# print('1.拳头  2.剪刀  3.布')
# p1=int(input('请出拳：'))
# #电脑出拳
# c1=random.randint(1,3)
# sleepTime()
# if p1 == 1 and c1 == 2 or p1 == 2 and c1 == 3 or p1 == 3 and c1 == 1:
#     print('玩家获胜')
# elif p1 == c1:
#     print('平局')
# else:
#     print('性感张亮获胜')


# for i in range (1,10):
#     for j in range (1,i+1):
#         print(f'{j}*{i}={j*i}',end="\t")
#     print("")


#99乘法表下半部分
# i=1
# j=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(f'{i}*{j}={i*j}',end='\t')
#         j+=1
#     print()
#     i+=1

# i = 1
# j = 1
#
# while i <= 9:
#     j=i
#     while j <= 9:
#         print(f'{i}*{j}={i*j}',end="\t")
#         j+=1
#     print()
#     i+=1
#
# import  math


# i=1
# j=1
#
# while i<=9:
#
#     if(i<=5):
#         j=1
#         while j <= i:
#             print('*', end="\t")
#             j += 1
#     else:
#         j=i
#         while j <= 9:
#             print('*', end="\t")
#             j += 1
#     print()
#     i+=1
# a = 0
# b = 0
# print("猜拳游戏三局两胜制")
# print("1.石头 2.剪刀 3.布")
# c=0
# while True:
#     c1 = random.randint(1, 3)
#     print(f"目前玩家{a}胜，电脑{b}胜")
#     p1 = int(input("请出拳"))
#     if p1 == 1 and c1 == 2 or p1 == 2 and c1 == 3 or p1 == 3 and c1 == 1:
#         print("玩家胜")
#         a+=1
#     elif p1 == c1:
#         print("平局")
#     else :
#         print("电脑胜")
#         b+=1
#     if a == 2 or b == 2:
#         break
# print(f'玩家{a}胜，电脑{b}胜')

# money = 1000#启动资金
# count = 1 #游戏次数
# fristNumber = 0 #玩家第一次投出来的点数
# while money > 0:
#     count = 1
#     print(f"剩余资金{money}")
#     putinmoney = int(input("请输入下注"))
#     while putinmoney > money:
#         print("你没有那么多钱哦，请重新下注")
#         putinmoney = int(input("请重新输入下注"))
#     while True:
#         time.sleep(1)
#         a = random.randint(1, 6)  # a筛点数
#         b = random.randint(1, 6)  # b筛点数
#         print(f"筛子点数{a}，{b}")
#
#         if count == 1:
#             count += 1
#             fristNumber = a + b
#             if a + b == 11 or a + b == 7:
#                 print("玩家获胜")
#                 money = money+ putinmoney
#                 break
#             elif a + b == 2 or a + b == 3 or a + b == 11:
#                 print("庄家获胜")
#                 money = money - putinmoney
#                 break
#             else :
#                 print("重投一次")
#         else :
#             if a + b == fristNumber:
#                 print("玩家获胜")
#                 money = money+ putinmoney
#                 break
#             elif a + b == 7:
#                 print("庄家获胜")
#                 money = money - putinmoney
#                 break
#             else :
#                 print("重投一次")
# import pdb

# for i in range (1,6):
#     for j in range (1,i+1):
#         print("*",end="")
#     print("")


# mystr = 'apple,orange,banana'
# a=mystr.split(",",2)
# print(a[0])
# try :
#     print(mystr.index("wolin"))
# except Exception as e:
#     print(f"Error{e}")

# 题目1：闰年与世纪闰年判断。
# 要求：输入一个正整数年份，判断该年份是否为闰年。规则：普通闰年是能被4整除但不能被100整除的年份；世纪闰年是能被400整除的年份。
# 若输入非正整数，提示“输入无效，请输入正整数年份”。
# inputYear = 0
# while True:
#     try:
#       inputYear=int(input("请输入一个正整数年份"))
#     except Exception as e:
#         1
#     if inputYear>0 and type(inputYear)==int:
#         break
#     else:
#         print("输入无效，请输入正整数年份")
#         continue
#
# if inputYear % 4 == 0 and inputYear % 100 != 0:
#     print(f"你输入的{inputYear}是闰年")
# elif inputYear % 400 ==0 :
#     print(f"你输入的{inputYear}是世纪闰年")
# else:
#     print(f"你输入的{inputYear}不是闰年也不是世纪闰年")


#题目2：实现用户的注册功能，吧用户数据存储在变量里，然后登录的时候直接对比变量值验证是否登录成功
# userName = ""
# userPassword = ""
# count = 0
#
# while True:
#     print("欢迎进入沃林学员系统")
#     print("1.登录 2.注册 3.退出")
#     operate=input("请输入操作")
#     if operate == "1":
#         if userName =="" and userPassword =="":
#             print("系统暂无用户注册，请先注册")
#             continue
#         else:
#             un=input("请输入用户名")
#             up=input("请输入密码")
#             if un==userName and up == userPassword:
#                 print("成功登录沃林学院系统")
#                 break
#             elif count<3:
#                 count +=1
#                 if count == 3:
#                     print("登录失败，用户被冻结，请找人工！！")
#                     break
#                 print(f"登录失败，还有{3-count}次机会")
#                 continue
#     if operate == "2":
#         print("进入注册用户页面")
#         userName=input("请输入需要注册的账号")
#         userPassword=input("请输入需要注册的密码")
#         print("注册成功")
#         continue
#     else:
#         print("退出功能是假的 还没做捏")



#题目3：用while循环实现猜数字游戏（含次数限制） 要求：程序随机生成一个 1-100之间的整数作为目标数字，用户最多7次机会猜数字的机会。
#每次输入猜想的数字后提示”猜大了“、”猜小了“、”猜对了“ 若7此都未猜对，提示”游戏结束，目标数字是X“
# num=random.randint(1,100)
# print("猜数游戏!")
# for i in range (1,8):
#     a=int(input("请输入一个1-100的整数"))
#     if a>num:
#         print("猜大了")
#     elif a<num:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break
#     if i==7:
#         print(f"游戏结束，目标数字是{num}")
#     else:
#         print(f"还有{7-i}次机会")


#题目4:坐标象限判断（含坐标轴判断）要求：输入平面直角坐标系中一点的横纵坐标（x,y），判断该点位于哪个象限的坐标轴上。
#规则：x=0且y=0为”坐标原点上“;x=0且y≠0为”在Y轴上“;x≠0且y=0为”在X轴上“;x>0且y>0为”第一象限“;x>0且y<0为”第二象限“;
# x<0且y<0为”第三象限“;x<0且y>0为”第四象限“;

# while True:
#     try:
#         zuobiao = input("请输入坐标")
#         zuobiaostr=zuobiao.split(",")
#         x = float(zuobiaostr[0])
#         y = float(zuobiaostr[1])
#         break
#     except Exception as e:
#         print("输入的数字不符合格式请重新输入")
#         continue
# if x==0 and y == 0:
#     print("坐标在坐标原点上")
# elif x==0 and y!=0:
#     print("坐标在Y轴上")
# elif x!=0 and y == 0:
#     print("坐标在X轴上")
# elif x>0 and y>0:
#     print("坐标在第一象限")
# elif x < 0 and y > 0:
#     print("坐标在第二象限")
# elif x < 0 and y < 0:
#     print("坐标在第三象限")
# elif x > 0 and y < 0:
#     print("坐标在第四象限")


#题目5三角形类型判断（含合法性校验）要求：输入三个正整数作为三角形的三条边长，先判断这三条边能不能能否构成三角形
#（任意两边之和大于第三边），若不能则提示”不能构成三角形“；如果能，判断是否是直角三角形（a方+b方=c方） 否则为普通三角形
# i=1
# while i<4:
#     try:
#         if i == 1:
#             a=int(input("请输入第一条边"))
#             if a>0:
#                 i+=1
#             else:
#                 print("请输入正整数")
#                 i=1
#                 continue
#         elif i == 2:
#             b = int(input("请输入第二条边"))
#             if b > 0:
#                 i+=1
#             else:
#                 print("请输入正整数")
#                 i = 1
#                 continue
#         else:
#                 c = int(input("请输入第三条边"))
#                 if c > 0:
#                     i+=1
#                 else:
#                     print("请输入正整数")
#                     i = 1
#                     continue
#     except Exception as e:
#         print("请输入正整数")
#         i = 1
#         continue
# if a+b>c and a+c>b and b+c>a:
#     if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能构成三角形")


#题目6：
# for i in range(1,10):
#     j=i
#     for j in range(j,10):
#         print(f"{i}*{j}={i*j}",end="\t")
#     print("")


#题目7：循环实现累加器（含终止条件）要求：实现一个累加器，不断接受用户输入的数字（支持整数和小数），并实时显示当前的累加和。
#当用户输入”q“或”Q“时，种植程序并输出最终的累加和。若输入非数字且不为”q”或“Q”，提示“输入无效，请输入数字或q/Q终止“

# sum=0
# status=True
# asd=""
#
# while True:
#     try:
#         if status:
#             asd=input("请输入数字或者”q”或“Q”退出累加")
#             if asd == "q" or asd == "Q":
#                 print(f"累加退出，当前累加值为{sum}")
#                 break
#             else:
#                 sum=sum+float(asd)
#                 print(f"当前累加值为{sum}")
#             continue
#         else:
#             asd = input("输入无效，请输入数字或q/Q终止")
#             if asd == "q" or asd == "Q":
#                 print(f"累加退出，当前累加值为{sum}")
#                 break
#             else:
#                 sum=sum+float(asd)
#                 print(f"当前累加值为{sum}")
#             continue
#         continue
#
#     except Exception as  e:
#         status=False
#         continue


# #新增
# a=list("")
# a.append('111')
# b=['222']
# a.extend(b)
# b='222'
# a.extend(b)
# a.insert(0,'333')
# print(a)
# #查询
# print(a.index('333',0,4))#查询字符，开始下标，结束下表
# print('333' in a) #返回bool值 存在为True
# print('333' not in a) #返回bool值 不存在为True
# print(a.count('2'))#查询里面有几个’2‘
# #删除
# del a[0] #删除下标为0的
# print(a)
# a.pop(1)
# print(a)
# a.remove('2')
# print(a)
# a.clear()
# print(a)


#添加用户注册功能
#添加用户充值功能
#添加用户注销功能（低于300的余额不退回，余额超过300的用户5折退回）

# loginName=""
# loginPassword=""
# usyue=""
# user1={'userName':'张三','userPassword':'666','userBalance':18888}
# user2={'userName':'李四','userPassword':'777','userBalance':1888}
# user3={'userName':'王五','userPassword':'888','userBalance':188}
# user4={'userName':'赵六','userPassword':'999','userBalance':18}
# users=[user1,user2,user3,user4]
#
#
# print("欢迎进入会员登录系统")
#
# while True:
#     print("首页：")
#     print("1.注册 2.登录 3.退出 4.充值 5，注销用户")
#     operate = input("请操作")
#     if operate == "1":#注册
#         print("注册页面")
#         usName=input("请输入注册的用户名")
#         usPassword = input("请输入注册的密码")
#         status1=1
#         for i in users:
#             if usName==i["userName"]:
#                 status1=-1
#         if status1 == 1:
#             print("注册成功")
#             newUser={'userName':usName,'userPassword':usPassword,'userBalance':0}
#             users.append(newUser)
#         else:
#             print("你输入的用户名已存在！")
#             continue
#     if operate == "2":#登录
#         if loginName=="":
#             for count in range(1, 4):
#                 print("登录界面")
#                 loginName = input("请输入用户名")
#                 loginPassword = input("请输入密码")
#                 status2 = -1
#                 for i in users:
#                     if loginName == i["userName"] and loginPassword == i["userPassword"]:
#                         status2 = 1
#                         usyue = i["userBalance"]
#                 if status2 == 1:
#                     print(f"欢迎光临{loginName}")
#                     print(f"登录成功，您的余额还有{usyue}元")
#                     operate = 0
#                     break
#                 else:
#                     print(f"登录失败，还有{3 - count}次机会，请重新登录")
#                     continue
#             continue
#         else:
#             print("你已登录")
#             continue
#
#     if operate == "3":#退出
#         break
#     if operate == "4":#充值
#         if loginName=="":
#             print("目前还未登录，请先登录")
#         else:
#             while True:
#                 try:
#                     amount = int(input("请输入充值金额"))
#                     usyue = usyue+amount
#                     for i in users:
#                         if loginName == i["userName"]:
#                             i.update({'userName':loginName,'userPassword':loginPassword,'userBalance':usyue})
#                             break
#                     print(f"充值成功，当前余额为{usyue}元")
#                     break
#                 except Exception as e:
#                     print("请输入正确的金额")
#                     print(e)
#                     continue
#             continue
#
#     if operate == "5":  # 注销用户
#         if loginName=="":
#             print("目前还未登录，请先登录")
#         else:
#             print(f"目前余额还剩余{usyue}元")
#             if usyue >= 300:
#                 print(f"按照超过300退50%的规定，已退回{usyue/2}元")
#             else:
#                 print("余额少于300元概不退回")

#             loginName=""
#             loginPassword=""
#             usyue=0
#             operate=0
#             continue

# my_list = {1,1,1,2,2,2,3,3,3,4,4,4,5,5,5}
# my_list=set(my_list)
# my_list.add(1)
# print(my_list)
# my_list=list(my_list)
# my_list.append(1)
# print(my_list)

# list1 = ['name', 'age', 'gender']
# list2 = ['Tom', 20, 'man']
#
# list3={list1[i]:list2[i] for i in range (len(list1))}
# print(list3)

# 现在有一个无序列表
# 请你为这个列表排序，升序 (禁止使用sort排序)
# 冒泡排序
# a = [3,1,4,6,2,7,5]
# lena = len(a)
# for i in range (0,lena-1):#0 1 2 3 4 5
#     for j in range (0,lena-1-i):#i=0:0 1 2 3 4 5 i=1:0 1 2 3 4
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# 选择排序
# a = [3,1,4,6,2,7,5]
# lena = len(a)
# for i in range (0,lena-1):#0 1 2 3 4 5
#      for j in range (i,lena): # 0 1 2 3 4 5 6
#          if a[i]>a[j]:
#              a[i],a[j]=a[j],a[i]
# print(a)


name_list=["张三","李四","王五"]
# del name_list[0]
# name_list.pop(0)
name_list.remove("张三")
print(name_list)

