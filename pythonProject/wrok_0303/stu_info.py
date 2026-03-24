import json
import  os
class Student:
    def __init__(self,stu_id,stu_name,stu_sex):
        self.stu_id=stu_id
        self.stu_name=stu_name
        self.stu_sex=stu_sex
    def to_dict(self):
        return {"stu_id":self.stu_id,"stu_name":self.stu_name,"stu_sex":self.stu_sex}
#增
    def add_stu_info(self):
        self.stu_json_exists()
        line=self.get_stu_info()
        status=0
        for i in line:
            if i["stu_id"]==self.stu_id:
                status=1
                break
        if status == 1:
            print("学生id重复请重新输入")
            return False
        else:
            line.append(self.to_dict())
            self.set_stu_info(line)
            print(f"已写入{self.to_dict()}")
            return True
    @staticmethod
    def stu_json_exists():
        if not os.path.exists("Studen.json"):
            with open("Studen.json", "w", encoding="utf-8") as f:
                f.write(json.dumps([]))
                pass
    @staticmethod
    def get_stu_info():
        with open ("Studen.json", "r+", encoding="utf-8") as f:
            lines=f.readline()
        return json.loads(lines)
    @staticmethod
    def set_stu_info(stu_info):
        json_str=json.dumps(stu_info)
        with open("Studen.json", "w+", encoding="utf-8") as f:
            f.write(json_str)






#删
def del_stu_info(stu_id):
    Student.stu_json_exists()
    lines=Student.get_stu_info()
    statu=0
    for i in lines:
        if i["stu_id"]==stu_id:
            del_stu_info=i
            statu=1
            break
    if statu==1:
        lines.remove(del_stu_info)
        Student.set_stu_info(lines)
        print(f"{stu_id}已删除")
        return True
    else:
        print("未找到对应id")
        return False
#查
def find_stu_info(stu_id):
    Student.stu_json_exists()
    line = Student.get_stu_info()
    statu=0
    stu_info="学生信息为空"
    for i in line:
        if i["stu_id"]==stu_id:
            statu=1
            stu_info=i
            break
    if statu==1:
        print(f"查到学生id{stu_id}的信息为：{stu_info}")
        return True
    else:
        print(f"未找到id为{stu_id}的学生")
        return False
#改
def revise_stu_info(stu_id):
    Student.stu_json_exists()
    line = Student.get_stu_info()
    statu=0
    old_info_str=""
    new_info_str=""
    info_list=[]
    for i in line:
        if i["stu_id"]==stu_id:
            print(f"根据{stu_id}查到的学生信息为{i}")
            old_info_str=i
            new_info_str=input("请依次输入该学生更改后的学生信息（如：学生id,学生姓名，学生性别 用逗号隔开）")
            info_list=new_info_str.split(",")
            i["stu_id"]=info_list[0]
            i["stu_name"] = info_list[1]
            i["stu_sex"] = info_list[2]
            statu=1
            break
    if statu==1:
        print(f"更改成功，已从{old_info_str}改成{new_info_str}")
        Student.set_stu_info(line)
        return True
    else:
        print(f"改函数：未找到id为{stu_id}的学生")
        return False

