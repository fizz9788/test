import Login
import stu_info
from fastapi import FastAPI

def Home_UI():
    print("欢迎进入学生管理系统")
    print("请输入你的选择")
    choise=input("1.登录 2.注册 3.退出")
    return choise

def Func_UI():
    print("功能菜单界面")
    choise=input("请选择你需要的功能：1.新增学生信息 2.删除学生信息 3.查找学生信息 4.修改学生信息 5.退出")
    return choise

def main_run():
    while True:
        user_choise=Home_UI()
        if user_choise=="1":#登录
            print("登录界面")
            login_id=input("请输入用户名")
            login_psw=input("请输入密码")
            user=Login.User_info(login_id,login_psw,"Admin")
            if user.Login():
                while True:
                    user_choise=Func_UI()
                    if user_choise=="1":#增加学生信息
                        new_stu_id=input("请输入需要新增的学生id")
                        new_stu_name = input("请输入需要新增的学生名字")
                        new_stu_sex = input("请输入需要新增的学生性别")
                        new_stu_info=stu_info.Student(new_stu_id,new_stu_name,new_stu_sex)
                        new_stu_info.add_stu_info()
                        continue
                    elif user_choise=="2":#删
                        del_stu_id=input("请输入需要删除的学生id")
                        stu_info.del_stu_info(del_stu_id)
                        continue
                    elif user_choise=="3":#查
                        find_stu_id = input("请输入需要查询的学生id")
                        stu_info.find_stu_info(find_stu_id)
                        continue
                    elif user_choise=="4":#改
                        revise_stu_id=input("请输入需要修改的学生id")
                        stu_info.revise_stu_info(revise_stu_id)
                        continue
                    elif user_choise=="5":#退出
                        break
                    else:
                        print("输入有误请重新输入")
                        continue
            else:
                continue
        elif user_choise=="2":#注册
            print("注册界面")
            create_id=input("请输入需要注册的用户名")
            create_psw = input("请输入需要注册的密码")
            user = Login.User_info(create_id, create_psw, "Admin")
            if user.Create_user():
                continue
            else:
                continue
        elif user_choise=="3":#退出
            quit()
        else:
            print("输入有误请重新输入")
            continue

main_run()