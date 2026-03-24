from sqlalchemy import create_engine, Integer, Column, String, and_, or_, not_, func, case
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

DATABASE_URL="mysql+pymysql://root:123456@127.0.0.1:3306/test"
engine = create_engine(DATABASE_URL,pool_size=5)
db_senssin=sessionmaker(bind=engine)
db=db_senssin()
#映射对象
Base=declarative_base()
class User(Base):
    __tablename__ ="user"
    id=Column(Integer,primary_key=True,comment="用户ID")
    name=Column(String(20),nullable=False,comment="用户姓名")
    sex=Column(String(10),nullable=False,comment="用户性别")
    age=Column(Integer,nullable=False,comment="用户年龄")


Base.metadata.create_all(bind=engine)

#数据的增删改查

#给user表添加一条数据
# user=User(id=1,name="张三",sex='男',age=18)
# db.add(user)
#事务的隔离性 每次操作完要commit
# db.commit()
#一次添加多条数据
# user1=User(id=2,name="李四",sex='男',age=20)
# user2=User(id=3,name="王五",sex='女',age=22)
# user3=User(id=4,name="赵六",sex='男',age=24)
# user4=User(id=5,name="张一",sex='女',age=26)
# user5=User(id=6,name="张二",sex='男',age=31)
# user6=User(id=7,name="张四",sex='女',age=41)
# db.add_all([user1,user2,user3,user4,user5,user6])
# db.commit()

#查看数据
def  show_all(a):
    for i in a:
        print(i.__dict__)

#query查询函数
# result=db.query(User).all()
# show_all(result)
#查看首行
# result = db.query(User).first()
#条件查询
# result=db.query(User).filter(User.age>=24).all()
# show_all(result)
#多条件查询
#and_
# result=db.query(User).filter(and_(User.name=='张三',User.sex=='男')).all()
# show_all(result)
#or_
# result=db.query(User).filter(or_(User.name=="张三",User.sex=='女')).all()
# show_all(result)
#not_
# result=db.query(User).filter(not_(User.name=='张三')).all()
# show_all(result)
#查询24岁以上女性
# result=db.query(User).filter(User.age>24,User.sex=='女')
# show_all(result)
#查询25到35岁的
# result = db.query(User).filter(User.age.between(25,35)).all()
# show_all(result)
#查询2，3，4号id
# result= db.query(User).filter(User.id.in_([2,3,4])).all()
# show_all(result)

#排序order_by(desc())
# result = db.query(User).filter(User.id <= 5).order_by(User.age.desc()).all()
#
# show_all(result)

#排序的目的是为了分页查询
#select * from user order by age limit 2

# print("_"*30)
# result = db.query(User).filter(User.id <= 5).order_by(User.age.desc()).limit(3)
# show_all(result)
# print("_"*30)
#select * from user order by age limit 2
# result = db.query(User).filter(User.id <= 5).order_by(User.age.desc()).offset(1).limit(3)
# show_all(result)


#聚合函数

#  .scalar 函数仅作用在查询结果只有一个列的聚合函数中
# result = db.query(func.count(User.id)).scalar()
# print(result)

# result = db.query(
#     func.count(User.id)
#   ,func.sum(User.age)
#   ,func.max(User.age)
#    ).first()
#
# print(result)

#分组

# db.query(分组字段, 聚合函数)  # 1. 指定要查的字段（分组字段+统计字段）
#    .group_by(分组字段)        # 2. 按指定字段分组
#    .having(筛选条件)          # 可选：过滤分组结果（如 count > 1）
#    .all()                    # 3. 执行查询，返回所有结果

# result = db.query(User.sex,User.id,func.count(User.id)).group_by(User.sex,User.id).all()
# print(result)

#分组筛选

# user_age=case((User.age<20,'0-20'),
#               (User.age>=20,'20+'))
# result=db.query(User.sex,user_age,func.count(User.id)).group_by(User.sex,user_age).all()
# print(result)

#查询性别人数大于3的性别
result=db.query(User.sex).group_by(User.sex).having(func.count(User.id)>3).all()
print(result)













