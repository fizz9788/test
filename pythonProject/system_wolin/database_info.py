from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

URL_emp="mysql+pymysql://root:123456@localhost:3306/wolin_system"
engine=create_engine(URL_emp,pool_size=5)
Session=sessionmaker(bind=engine)
Base=declarative_base()



def get_db():
    try:
        db=Session()
        yield db
    finally:
        db.close()