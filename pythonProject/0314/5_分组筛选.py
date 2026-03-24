from sqlalchemy import create_engine, Column, Integer, String, and_, not_, case
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



#

# user_age = case(
#     (User.age  < 20,'0-20'),
#     (User.age >= 20,'20+')
# )
#
# result = db.query(User.sex,user_age,func.count(User.id)).group_by(User.sex,user_age).all()
#
# print(result)


# 分组 筛选

# 查询人数超过1人的性别

result = db.query(User.sex).group_by(User.sex).having(func.count(User.id) > 2).all()

print(result)






