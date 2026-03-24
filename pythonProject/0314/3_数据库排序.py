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



def  show_all(a):
    for i in a:
        print(i.__dict__)
result = db.query(User).filter(User.id <= 5).order_by(User.age.desc()).all()

show_all(result)

#排序的目的是为了分页查询
#select * from user order by age limit 2

print("_"*30)
result = db.query(User).filter(User.id <= 5).order_by(User.age.desc()).limit(3)
show_all(result)
print("_"*30)
#select * from user order by age limit 2
result = db.query(User).filter(User.id <= 5).order_by(User.age.desc()).offset(1).limit(3)
show_all(result)






