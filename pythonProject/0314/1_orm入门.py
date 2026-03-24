from sqlalchemy import create_engine, Column, Integer, String
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



Base.metadata.create_all(bind=engine)
