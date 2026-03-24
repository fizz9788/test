# #函数
# #有参有返
# def xiangcheng1(a,b):
#     return a*b
#
# print(xiangcheng1(3,5))
#
# #有参无返
#
# def xiangcheng2(a,b):
#     print(a*b)
#
# xiangcheng2(3,5)
# #无参有返
# def xiangcheng3():
#     return 15
#
# print(xiangcheng3())
# #无参无返
#
# def wucanwufan():
#     print("无参无返")
#
# wucanwufan()


# 定义充值函数
# 定义查看所有技师函数
# 点技师函数  （需要定义技师信息）
# 注销用户函数
import random

user1={'userName':'张三','userPassword':'666','userBalance':18888}
user2={'userName':'李四','userPassword':'777','userBalance':1888}
user3={'userName':'王五','userPassword':'888','userBalance':188}
user4={'userName':'赵六','userPassword':'999','userBalance':18}
users=[user1,user2,user3,user4]
engineer1={'id':'8','price':188}
engineer2={'id':'88','price':288}
engineer3={'id':'66','price':388}
engineer4={'id':'99','price':488}
engineers=[engineer1,engineer2,engineer3,engineer4]

login_user=["","",""]
#根据Name去遍历得到
def find_user(Name,users):
    status=False
    user=None
    for i in users:
        if i["userName"]==Name:
            user=i
            status=True
    return user,status
#主界面
def frist_menu():
    print("-----请选择功能-----")
    print("1.登录 2.注册 3.退出 4.充值 5.点技师 6.注销用户" )
    choose=input("请输入你的选择")
    if choose=="1":
        user=denglu_menu()

    elif choose=="2":
        zhuce_menu()
    elif choose=="3":
        print("欢迎下次光临！")
        quit()
    elif choose=="4":
        chongzhi_menu()
    elif choose=="5":
        diancai_menu()
    elif choose=="6":
        zhuxiao_menu()
    else:
        frist_menu()
#登录界面
def denglu_menu():
    count = 0
    while count<3:
        login_Name = input("请输入用户名")
        login_Passworf = input("请输入密码")
        user,status=find_user(login_Name,users)
        if status:
            print("登录成功")
            login_user[0]=user.get('userName')
            login_user[1]=user.get('userPassword')
            login_user[2]=user.get('userBalance')
            # print(login_user)
            break
        else:
            count +=1
            print(f"你还有{3-count}次机会")
            continue
    frist_menu()
#充值页面
def chongzhi_menu():
    if login_user[0] == "":
        print("目前还未登录，请先登录")
        frist_menu()
    else:
        while True:
            try:
                amount = int(input("请输入充值金额"))
                login_user[2] = login_user[2] + amount
                for i in users:
                    if login_user[0] == i["userName"]:
                        i.update({'userName': login_user[0], 'userPassword': login_user[1], 'userBalance': login_user[2]})
                        break
                print(f"充值成功，当前余额为{login_user[2]}元")
                break
            except Exception as e:
                print("请输入正确的金额")
                print(e)
                continue
        frist_menu()
#注册页面
def zhuce_menu():
    usName = input("请输入注册的用户名")
    usPassword = input("请输入注册的密码")
    status1 = 1
    for i in users:
        if usName == i["userName"]:
            status1 = -1
    if status1==-1:
        print("用户名已存在请重新注册")
        zhuce_menu()
    else:
        print("注册成功")
        newUser = {'userName': usName, 'userPassword': usPassword, 'userBalance': 0}
        users.append(newUser)
    frist_menu()
#点技师页面
def diancai_menu():
    if login_user[0] == "":
        print("目前还未登录，请先登录")
        frist_menu()
    else:
        print("点菜界面")
        count = 1
        for i in engineers:
            print(f"{count}.编号{i['id']}，单价{i['price']}")
            count += 1
        count = input("请输入你需要的编号")
        status = False
        money = 0
        for i in engineers:
            if i['id'] == count:
                money = i['price']
                status = True
                break
        if status:
            print(f"点菜成功，编号{count},单价为{money}，剩余余额为{login_user[2] - money}")
            login_user[2]=login_user[2]-money
            for i in users:
                if login_user[0] == i["userName"]:
                    i.update({'userName': login_user[0], 'userPassword': login_user[1],
                              'userBalance': login_user[2]})
                    break
            frist_menu()
        else:
            print(f"你输入的{count}编号不存在，请重新选择")
            diancai_menu()
#注销界面
def zhuxiao_menu():
    if login_user[0] == "":
        print("目前还未登录，请先登录")
        frist_menu()
    else:
        print(f"目前余额还剩余{login_user[2]}元")
        if login_user[2] >= 300:
            print(f"按照超过300退50%的规定，已退回{login_user[2]/2}元")
        else:
            print("余额少于300元概不退回")
        for i in users:
            if login_user[0]==i["userName"]:
                users.remove(i)
                break
        print(f"系统已删除{login_user[0]}")
        frist_menu()


frist_menu()


### 题目1：简单计算函数
# 定义一个名为`calculate`的函数，接收两个必选参数`a`和`b`，以及一个可选参数`op`（默认值为"add"）。
# 函数功能：根据`op`的值执行对应运算并返回结果（add：加法，sub：减法，mul：乘法，div：除法，除法需处理除数为0的异常）。
def calculate(a,b,op='add'):
    if op =='add':
        return a+b
    elif op =='sub':
        return a-b
    elif op =='mul':
        return a*b
    elif op =='div':
        if a==0 or b==0:
            print("除法不能传为0的参数，请重新输入")
        else:
            return a/b
print(calculate(2,4))
print(calculate(2,4,'sub'))
print(calculate(2,4,'mul'))
print(calculate(2,4,'div'))
print(calculate(0,4,'div'))

### 题目2.函数返回多个值
# 定义一个名为`analyze_list`的函数，接收一个数字列表`nums`。函数功能：计算列表的最大值、最小值、平均值（保留2位小数），
# 并以元组形式返回这三个值。若列表为空，返回`(None, None, None)`。
def analyze_list(nums):
    if nums !=[]:
        sum=0
        maxValue = max(nums)
        minValue = min(nums)
        for i  in  nums:
            sum += i
        avgValue = sum / len(nums)
        return maxValue, minValue, avgValue
    else:
        return None,None,None

mylist1=[1,2,3,4,5,6,7,8]
mylist2=[]
print(analyze_list(mylist1))
print(analyze_list(mylist2))




### 题目3.简单函数打印
# 定义函数greet，接收一个必选参数name和一个可选参数message（默认值为 "Hello"），返回拼接后的问候语（如调用greet("Tom")返回 "Hello, Tom"，
# 调用greet("Lucy", "Hi")返回 "Hi, Lucy"）。
def greet(name,message="Hello"):
    str= message+","+ name
    return str
print(greet("Tom"))
print(greet("Lucy", "Hi"))


### 题目4.简单函数使用
# 定义函数count_even，接收一个整数列表nums，返回列表中偶数的个数（如count_even([1,2,3,4])返回 2，空列表返回 0）。
def count_even(nums):
    count = 0
    if nums != []:
        for i in nums:
            if i%2==0:
                count += 1

    return count
list1=[1,2,3,4,5,6,7,8]
list2=[]
print(count_even(list1))
print(count_even(list2))



### 题目5.位置参数与关键字参数
# 1.定义函数 calc_total，实现以下功能：
# 2.必选位置参数：price（单价，数字）、count（数量，整数）；
# 3.可变位置参数：discounts（多个折扣值，如 0.1 代表减 10%，每个元素为 0-1 之间的数字）；
# 4.关键字参数：tax（税率，默认 0.09）、shipping（运费，默认 10）；
# 5.计算逻辑：总价 = (单价 × 数量 × (1 - 所有折扣累加和)) + 运费 + (单价 × 数量 × 税率)，结果保留 2 位小数；
# 6.返回最终计算的总价（数字类型）。
def calc_total (price,count,*discounts,tax=0.09,shipping=10):
    zongjia=0
    zongjia=(price*count*(1-sum(discounts)))+shipping+(price*count*tax)
    return round(zongjia,2)

print(calc_total(4,4,0.1,0.1,0.1,0.1))




### 题目6.单词统计
# 定义函数get_word_stats，接收一个字符串s（仅包含字母和空格）。功能：统计字符串中每个单词的出现次数（不区分大小写），
# 返回两个结单果：出现次数最多的词（若有多个，返回第一个）、所有单词的次数字典（如输入 "I love Python love"，返回 ("love", {"i":1, "love":2, "python":1})）；
# 若字符串无有效单词，返回 (None, {})。
def get_word_stats(s):
    s=s.lower()
    a=s.split(" ")
    set_a=set(a)
    maxCount=0
    maxStr=None
    newList={}
    for i in a:
        if i !="":
            cishu = s.count(i)
            newList[i] = cishu
            if maxCount < cishu:
                maxCount = cishu
                maxStr = i
    return maxStr,newList

print(get_word_stats("I love Python love"))
print(get_word_stats(""))