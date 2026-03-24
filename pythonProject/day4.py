### 题目1：嵌套列表的多层访问与修改

# 要求：给定嵌套列表`info = [["张三", 20, ["语文", 85]], ["李四", 19, ["数学", 92]], ["王五", 21, ["英语", 78]]]`，完成以下操作：
# 1. 获取李四的年龄；
# 2. 将王五的英语成绩修改为88；
# 3. 给张三添加一门学科"数学"及成绩90，最终输出修改后的完整列表。

#1.


info = [["张三", 20, ["语文", 85]], ["李四", 19, ["数学", 92]], ["王五", 21, ["英语", 78]]]
for i in info:
    if "李四" in i:
        print(f"李四的年龄为{i[1]}")
#2.
for i in info:
    if "王五" in i:
        i[2][1]=88
print(info)
#3.
for i in info:
    if "张三" in i:
        i.append(["数学",90])
print(info)



### 题目2：列表的切片高级应用

# 要求：给定列表`nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`，完成以下操作：
# 1. 截取索引3到8的元素（含3不含8）；
# 2. 截取列表的后5个元素；
# 3. 倒序截取列表（从后往前取所有元素）；
# 4. 每隔2个元素取一个元素（从索引0开始），最终分别输出各步骤结果。

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1、
newNums=nums[2:7:1]
print(newNums)
#2.
newNums=nums[-5::]
print(newNums)
#3.
newNums=nums[::-1]
print(newNums)
#4.
newNums=nums[0::2]
print(newNums)


### 题目3：列表的增删改查综合操作

# 要求：给定空列表`goods = []`，按以下步骤操作：
# 1. 依次添加商品"手机"、"电脑"、"平板"、"耳机"；
# 2. 在"电脑"和"平板"之间插入"手表"；
# 3. 删除索引为3的元素；
# 4. 将"手机"修改为"智能手机"；
# 5. 查找"耳机"的索引位置，最终输出每步操作后的列表及"耳机"的索引。

goods = []
#1.
shangpin=["手机","电脑","平板","耳机"]
for i in shangpin:
    goods.append(i)
print(goods)
#2.
num=goods.index("平板")
goods.insert(num,"手表")
print(goods)
#3.
goods.pop(3)
print(goods)
#4.
num=goods.index("手机")
goods[num]="智能手机"
print(goods)
#5.
num=goods.index("耳机")
print(f"耳机的索引位置是{num}")

### 题目4：列表的排序与反转高级应用

# 要求：给定列表`scores = [85, 92, 78, 95, 88, 76, 90, 82]`，完成以下操作：
# 1. 对列表进行升序排序（不创建新列表）；
# 2. 基于升序列表，获取前3名成绩（降序输出）；
# 3. 对原列表（未排序前）进行反转，最终输出排序后的列表、前3名成绩、反转后的原列表。

scores = [85, 92, 78, 95, 88, 76, 90, 82]
#1.
scores.sort(key=None,reverse=False)
print(scores)
#2.
qiansnaming=scores[0:3:1]
qiansnaming.sort(key=None,reverse=True)
print(qiansnaming)
#3.
scores = [85, 92, 78, 95, 88, 76, 90, 82]
fanzhuan=scores[::-1]
print(fanzhuan)


### 题目5：列表推导式基础应用（筛选与转换）

# 要求：给定列表`nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`，使用列表推导式完成以下操作：
# 1. 筛选出所有偶数；
# 2. 筛选出所有能被3整除的数，并将其乘以2；
# 3. 生成一个新列表，元素为原列表每个元素的平方（仅保留平方大于50的元素），最终输出三个新列表。

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#1.
newNums=[i for i in nums if i%2==0]
print(newNums)
#2.
newNums=[i/2 for i in nums if i%3==0]
print(newNums)
#3.
newNums=[i**2 for i in nums if i**2>50]
print(newNums)


### 题目6：列表的去重与元素统计

# 要求：给定列表`data = [2, 3, 2, 4, 5, 3, 6, 5, 7, 8, 7, 9]`，完成以下操作：
# 1. 对列表进行去重（不使用集合，仅用列表方法）；
# 2. 统计原列表中每个元素出现的次数（用列表方法实现）；
# 3. 找出原列表中出现次数最多的元素，最终输出去重后的列表、元素次数统计结果、出现次数最多的元素。
data = [2, 3, 2, 4, 5, 3, 6, 5, 7, 8, 7, 9]
#1.
newList1=[]
newList2={}
for i in data:
    if i not in newList1:
        newList1.append(i)
print(newList1)

#2.
for i in newList1:
    num=data.count(i)
    newList2[i]=num
print(newList2)

#3.
newList3=[]
value=newList2.values()
maxValue=max(value)
for i in newList2.keys():
    if newList2[i]==maxValue:
        newList3.append(i)
print(f"出现次数最多的元素有{newList3}")



### 题目7：嵌套列表的遍历与数据提取

# 要求：给定嵌套列表`student_scores = [["小明", [85, 90, 88]], ["小红", [92, 89, 95]], ["小刚", [78, 85, 80]], ["小丽", [90, 91, 89]]]`，完成以下操作：
# 1. 遍历列表，提取每个学生的姓名和平均分；
# 2. 筛选出平均分大于85的学生，组成新的列表，最终输出每个学生的姓名及平均分、筛选后的列表。
#1.
student_scores = [["小明", [85, 90, 88]], ["小红", [92, 89, 95]], ["小刚", [78, 85, 80]], ["小丽", [90, 91, 89]]]
for i in student_scores:
    lens=len(i[1])
    sum=0
    for j in range(0,lens):
        sum+=i[1][j]
    avg=round(sum/lens,2)
    print(f"{i[0]}的平均分为{avg}")
#2.
student_scores = [["小明", [85, 90, 88]], ["小红", [92, 89, 95]], ["小刚", [78, 85, 80]], ["小丽", [90, 91, 89]]]
for i in student_scores:
    lens=len(i[1])
    sum=0
    for j in range(0,lens):
        sum+=i[1][j]
    avg=round(sum/lens,2)
    if avg<85:
        student_scores.remove(i)
print(student_scores)


### 题目8：列表的拼接与复制高级应用

# 要求：给定列表`a = [1, 2, 3]`和`b = [4, 5, 6]`，完成以下操作：
# 1. 用两种方法将a和b拼接为新列表；
# 2. 将a列表复制一份，命名为c，修改c的第1个元素为10，观察a是否变化；
# 3. 将a列表的切片复制一份命名为d，修改d的第2个元素为20，观察a是否变化，最终输出拼接后的列表、修改后的c和a、修改后的d和a。
a = [1, 2, 3]
b = [4, 5, 6]
#1
newab=a+b
print(newab)
#2
c=a.copy()
c[0]=10
print(a)
print(c)
#3
d=a[::]
d[1]=20
print(a)
print(d)


### 题目9：字典的增删改查综合操作

# 要求：给定空字典`product = {}`，按以下步骤操作：
# 1. 添加商品信息："id": 101, "name": "手机", "price": 5999, "stock": 100；
# 2. 修改商品价格为5799；
# 3. 删除“stock”键值对；
# 4. 查找“name”键对应的值，若不存在输出“无此键”；
# 5. 查找“brand”键对应的值，若不存在则添加该键，值为“华为”，最终输出每步操作后的字典。
product = {}
#1.
product.update({"id": 101, "name": "手机", "price": 5999, "stock": 100})
print(product)
#2.
product.update({"id": 101, "name": "手机", "price": 5999, "stock": 100})
product["price"]=5799
print(product)
#3.
product.update({"id": 101, "name": "手机", "price": 5999, "stock": 100})
del product["stock"]
print(product)
#4
product.update({"id": 101, "name": "手机", "price": 5999, "stock": 100})
print(product.get('name','不存在'))
#5.
product.update({"id": 101, "name": "手机", "price": 5999, "stock": 100})
result=product.get("brand")
if result==None:
    product["brand"]="华为"
    print(product)
else:
    print(result)

### 题目10：字典的遍历
# 已知字典 fruit_price = {"apple": 5.9, "banana": 3.5, "orange": 4.2, "grape": 8.8}，完成以下操作：
# 1.遍历字典，打印所有水果的名称和价格（格式：苹果：5.9 元）；
# 2.找出价格最高的水果名称和价格并打印；
# 3.提取字典中所有的水果名称，组成一个列表并打印；
# 4.判断 pear 是否在字典中，若不在则添加 {"pear": 6.5}；
# 5.清空字典中所有键值对，打印清空后的字典。
fruit_price = {"apple": 5.9, "banana": 3.5, "orange": 4.2, "grape": 8.8}
#1.
for i in fruit_price.keys():
    price=fruit_price.get(i)
    print(f"{i}:{price}元")
#2.
maxPrice=max(fruit_price.values())
for i in fruit_price.keys():
    price=fruit_price.get(i)
    if maxPrice==price:
        print(f"{i}为{price}元，最贵")
#3.
name=[]
for i in fruit_price.keys():
    name.append(i)
print(name)
#4.
name=[]
for i in fruit_price.keys():
    name.append(i)
if 'pear' not in name:
    fruit_price["pear"]=6.5
print(fruit_price)
#5.
fruit_price.clear()
print(fruit_price)



