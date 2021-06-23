<<<<<<< HEAD
class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'
=======
class Student(object):    def __init__(self, name, gender, tel):        self.name = name        self.gender = gender        self.tel = tel    def copy(self, old_student):        self.name = old_student.name        self.gender = old_student.gender        self.tel = old_student.tel    def __str__(self):        return f'学员基本信息：{self.name}, {self.gender}, {self.tel}'
>>>>>>> ec656fa1d9a9ecc033070be1ff9796d3c0e5b5f0
