from sqlalchemy import create_engine,Column, Integer, String, and_, not_
from sqlalchemy.orm import  sessionmaker,declarative_base
from sqlalchemy.sql.functions import func

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


#  .scalar 函数仅作用在查询结果只有一个列的聚合函数中
result = db.query(func.count(User.id)).scalar()
print(result)

result = db.query(
    func.count(User.id)
  ,func.sum(User.age)
  ,func.max(User.age)
   ).first()

print(result)

# 分组   求出男生和女生的人数
result = db.query(User.sex,User.id,func.count(User.id)).group_by(User.sex,User.id).all()
print(result)

