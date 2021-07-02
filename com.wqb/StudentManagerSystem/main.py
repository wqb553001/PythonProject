"""
 入口类：
 （1） 创建运行类对象实例
 （2）通过实例，调用 适当的方法，执行应用
"""
from managerSystem import *

if __name__ == '__main__':
    studentManager = StudentManager()
    studentManager.run()
