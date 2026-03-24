import json
import os

class User_info:

    def __init__(self,login_id,login_psw,level):
        self.login_id=login_id
        self.login_psw=login_psw
        self.__level=level

    def to_dict(self):
        return {"login_id":self.login_id,"login_psw":self.login_psw,"level":self.__level}

#注册
    def Create_user(self):
        self.login_json_exists()
        line=self.get_user()
        statu=0
        for i in line:
            if i["login_id"]==self.login_id:
                statu=1
                break
        if statu==1:
            print("改用户名已存在")
            return False
        else:
            new_dict=self.to_dict()
            line.append(new_dict)
            self.set_user(line)
            print(f"{self.login_id}创建成功")
            return True
#登录
    def Login(self):
        self.login_json_exists()
        line=self.get_user()
        statu=0
        for i in line:
            if i["login_id"]==self.login_id and i["login_psw"]==self.login_psw:
                statu=1
                user_info=i
                break
        if statu==0:
            print("账号密码错误")
            return False
        else:
            print("登陆成功")
            return True,user_info

    def login_json_exists(self):
        if not os.path.exists("Admin.json"):
            with open("Admin.json", "w", encoding="utf-8") as f:
                f.write(json.dumps([]))
                f.close()
    @staticmethod
    def get_user():
        with open("Admin.json", "r+", encoding="utf-8") as f:
            lines=f.readline()
        return json.loads(lines)
    @staticmethod
    def set_user(line):
        with open("Admin.json", "w+", encoding="utf-8") as f:
            json_line = json.dumps(line)
            f.write(json_line)





