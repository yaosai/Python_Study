#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: demo_class.py.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/11 15:33
# @desc: OOP练习


# 定义一个对象
class Student():
    pass


# 定义一个对象
yaosai = Student()


class PythonStudent():
    name = None
    age = 18
    course = "python"

    # self表示方法本身
    def doHomeWord(self):
        print("做作业")
        return None


steve = PythonStudent()
print(steve.name)
print(steve.age)
steve.doHomeWord()

# __dict__方法进行对象成员检查
print(Student.__dict__)

print("#" * 50)


class Teacher():
    name = "nana"
    age = 19

    # self参数不是关键字！代表对象本身！
    def say(self):
        self.name = "yaoyao"
        self.age = 20
        print(self.name, "  ", self.age, "  ", __class__.age)

    def sayAgain():
        print(__class__.name)
        print("hahaha")


t = Teacher()
t.say()
# 因为未传self！t.sayAgain()会报类型错误！
# t.sayAgain()
Teacher.sayAgain()
