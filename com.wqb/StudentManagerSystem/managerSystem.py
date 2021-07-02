
"""
  需求分析：
    学员信息的增、删、改、查（单个、全量）、存、加载
"""
from student import *
# import os

class StudentManager(object):

    student_list = []
    def run(self):
        # 加载学员信息
        self.load_student()
        # 选择功能
        while True:
            # 展示功能
            self.show_func()
            func = int(input('请输入功能序号：'))
            if func == 1:
                self.add_student()
            elif func == 2:
                self.modify_student()
            elif func == 5:
                self.show_student_info('查询所有学员信息')
            elif func == 6:
                self.save_student()
            if func == 7:
                break

    def load_student(self):
        student_f = open('student-info.data', 'r')
        student_list_str = student_f.read()
        student_load = eval(student_list_str)
        self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in student_load]
        self.show_student_info('加载学员信息')

    def show_func(self):
        print('1新增学员')
        print('2修改学员')
        print('3删除学员')
        print('4查询学员')
        print('5查询所有学员')
        print('6保存学员')
        print('7退出系统')

    def add_student(self):
        name = input('请输入姓名：')
        gender = input('请输入性别：')
        tel = input('请输入手机号：')
        student = Student(name, gender, tel)
        self.student_list.append(student)
        self.show_student_info('新增学员')

    def modify_student(self):
        name = input('请输入需要修改的姓名：')
        for i in self.student_list:
            if i.name == name:
                old_student = Student(i.name, i.gender, i.tel)
                gender = input('请输入性别：')
                tel = input('请输入手机号：')
                i.gender = gender
                i.tel = tel
                print(f'已成功将【学员信息】:[{old_student}] 修改为：[{i}]')
                break
        else:
            print(f'未找到该学员：{name},请核对后重新输入！')

    def save_student(self):
        student_f = open("student-info.data", 'w')
        new_list = [i.__dict__ for i in self.student_list]
        student_f.write(str(new_list))
        student_f.close()
        print('保存了学员信息。')

    def show_student_info(self, func_name):
        student_str = [i.__dict__ for i in self.student_list]
        print(f'{func_name} : {student_str}')
