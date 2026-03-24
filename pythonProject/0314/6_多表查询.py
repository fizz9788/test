from sqlalchemy import create_engine, text,Column, Integer, String, and_, not_, case, ForeignKey, Date, Float
from sqlalchemy.orm import  sessionmaker,declarative_base
from sqlalchemy.sql.functions import func

DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/wolin"
engine = create_engine(DATABASE_URL,pool_size=5)
db_session  = sessionmaker(bind=engine)
db = db_session()
#映射对象
Base = declarative_base()


class Locations(Base):
    __tablename__ = "locations"  # 对应数据库表名

    # 字段映射（与MySQL表字段一一对应）
    location_id = Column(Integer, primary_key=True, comment="位置ID")
    street_address = Column(String(40), nullable=True, comment="街道地址")
    postal_code = Column(String(12), nullable=True, comment="邮政编码")
    city = Column(String(30), nullable=False, comment="城市")
    state_province = Column(String(25), nullable=True, comment="省/州")
    country_id = Column(String(2), nullable=True, comment="国家ID")



# ② departments表（关联locations表）
class Departments(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, comment="部门ID")
    department_name = Column(String(30), nullable=True, comment="部门名称")
    manager_id = Column(Integer, nullable=True, comment="部门经理ID")
    location_id = Column(Integer, ForeignKey("locations.location_id"), nullable=True, comment="位置ID")



# ③ employees表（关联departments表）
class Employees(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, comment="员工ID")
    first_name = Column(String(20), nullable=True, comment="名")
    last_name = Column(String(25), nullable=True, comment="姓")
    email = Column(String(25), nullable=True, comment="邮箱")
    phone_number = Column(String(20), nullable=True, comment="电话号码")
    hire_date = Column(Date, nullable=True, comment="入职日期")
    job_id = Column(String(10), nullable=True, comment="职位ID")
    salary = Column(Integer, nullable=True, comment="薪资")
    commission_pct = Column(Float(precision=(5, 2)), nullable=True, comment="佣金比例")
    manager_id = Column(Integer, nullable=True, comment="经理ID")
    department_id = Column(Integer, ForeignKey("departments.department_id"), nullable=True, comment="部门ID")




result = db.query(Employees.employee_id,Employees.department_id,Departments.department_id).join(Employees).all()

print(result)

print(len(result))

result = db.query(Employees,Departments,Locations)\
    .select_from(Employees).\
    join(Departments).\
    join(Locations)\
    .where(
            and_(
                Employees.department_id == Departments.department_id
                ,Departments.location_id == Locations.location_id
                )
            ).all()

print(result)

# 返璞归真

# query_sql = "select * from employees"
# result = db.execute(text(query_sql))
#
# for i in result:
#     print(i)


