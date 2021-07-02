from student import *
import os


class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_student()
        while True:
            self.show_menu()
            func_index = input('请输入功能序号：')
            if func_index == 1:
                self.add_student()
                break
            elif func_index == 2:
                self.delete_student()
                break
            elif func_index == 3:
                self.modify_student()
                break
            elif func_index == 4:
                self.query_student()
                break
            elif func_index == 5:
                self.show_all_student()
                break
            elif func_index == 6:
                self.save_student()
                break
            elif func_index == 7:
                self.exit_system()
                break

    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1.添加学员：')
        print('2.删除学员：')
        print('3.修改学员信息：')
        print('4.查询学员信息：')
        print('5.显示所有学员信息：')
        print('6.保存学员信息：')
        print('7.退出系统：')

    def add_student(self):
        # 采集学员信息
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的手机号：')
        # 创建学员对象
        student = Student(name, gender, tel)
        # 将学员对象添加到学员列表
        self.student_list.append(student)
        print(self.student_list)
        # 保存用户信息
        self.save_student()

    def delete_student(self):
        del_name = input('请输入要删除的学员姓名：')
        for s in self.student_list:
            if s.name == del_name:
                self.student_list.remove(s)
                print(f"已移除 学员：{s}")
                # 保存用户信息
                self.save_student()
                break
        else:
            print("查无此学员！")

    def modify_student(self):
        modify_name = input('请输入要修改的学员姓名：')
        for s in self.student_list:
            if s.name == modify_name:
                tel = input('请输入要修改的学员手机号：')
                s.tel = tel
                print(f"已修改 学员：{s}")
                # 保存用户信息
                self.save_student()
                break
        else:
            print("查无此学员！")

    def query_student(self):
        query_name = input('请输入要查询的学员姓名：')
        for s in self.student_list:
            if s.name == query_name:
                print(f"已查询到 学员：{s}")
                break
        else:
            print("查无此学员！")

    def show_all_student(self):
        print(f'所有学员信息{self.student_list}')

    def save_student(self):
        f_student = os.open('student.txt', 'wb')
        f_student.write(self.student_list)
        f_student.close()

    def exit_system(self):
        return
