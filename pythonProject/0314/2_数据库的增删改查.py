#
from operator import or_

from sqlalchemy import create_engine,Column, Integer, String, and_, not_
from sqlalchemy.orm import  sessionmaker,declarative_base
DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/test"
engine = create_engine(DATABASE_URL,pool_size=5)
db_session  = sessionmaker(bind=engine)
db = db_session()
#映射对象
Base = declarative_base()

class  User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, comment="用户id")
    name = Column(String(20), nullable=False, comment="用户姓名")
    sex = Column(String(10),nullable=False)
    age = Column(Integer, nullable=False)

# #给user表添加一条数据
# user1 = User(id = 1,name = '张亮',sex = '男',age = 20)
# db.add(user1)
#
# # 因为有事务
# # 所以要commit
# db.commit()

# 一次添加多条数据
# user1 = User(id = 2,name = '张三',sex = '男',age = 20)
# user2 = User(id = 3,name = '李四',sex = '女',age = 22)
# user3 = User(id = 4,name = '王五',sex = '女',age = 25)
# user4 = User(id = 5,name = '赵六',sex = '女',age = 35)
#
# db.add_all([user1,user2,user3,user4])
# db.commit()

#查看数据

def  show_all(a):
    for i in a:
        print(i.__dict__)

result = db.query(User).all()

for i in result:
    print(i.__dict__.get('id'))

print("_"*30)

result1 = db.query(User).first()
print(result1.__dict__)
print("_"*30)
#查看数据
result2 = db.query(User).filter(User.age>30).all()

for i in result2:
    print(i.__dict__)



# 多条件查询
print("查询年龄大于等于25岁并且性别= 女的信息")

result3 = db.query(User).filter(and_(User.sex == '女',User.age >=25)).all()
for i in result3:
    print(i.__dict__)

print("查询叫张亮或者女孩")
result4 = db.query(User).filter(or_(User.name == '张亮',User.sex =='女')).all()

for i in result4:
    print(i.__dict__)

print("查询不是张亮的人")
result5 = db.query(User).filter(not_(User.name=='张亮')).all()
show_all(result5)

print("查询不是张亮的人")
result5 = db.query(User).filter(User.name != '张亮').all()
show_all(result5)


print("查询年龄大于25并且性别为女的信息")
result3 = db.query(User).filter(User.sex == '女',User.age >=25).all()
for i in result3:
    print(i.__dict__)



print("查询年龄在25到35之间的信息")

result = db.query(User).filter(User.age <=35 ,User.age >= 25).all()
show_all(result)


print("查询年龄在25到35之间的信息 between and")
result = db.query(User).filter(User.age.between(25,35)).all()
show_all(result)


print("查询2，3，4号id")
result= db.query(User).filter(User.id.in_([2,3,4])).all()
show_all(result)



print("查询姓张的， 模糊查询版")

result = db.query(User.id,User.age,User.name,User.sex).filter(User.name.like('张%')).all()

for  i in result:
    print(i)
    print(type(i))

# 删除5号员工

db.query(User).filter(User.id ==5).delete()
db.commit()

#修改张亮的年龄为60

db.query(User).filter(User.name == '张亮').update({User.age:60})
db.commit()


# 修改女孩的年龄为18

db.query(User).filter(User.sex == '女').update({User.age:18})
db.commit()

