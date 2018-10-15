#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# @file: demo_mixin.py
# @author: YaoS
# @contact: yao.sai@hotmail.com
# @time: 18/10/15 0:52
# @desc: Mixin练习


class Person():
    name = "yaosai"
    age = 18

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    def drink(self):
        print("drink")


class Teacher(Person):
    def work(self):
        print("work")


class Student(Person):
    def study(self):
        print("study")


class Tutor(Teacher, Student):
    pass


t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print()
print("#" * 30)
print()


class TeacherMixin():
    def work(self):
        print("work")


class StudentMixin():
    def study(self):
        print("study")


class TutorMixin(Person, TeacherMixin, StudentMixin):
    pass


tt = TutorMixin()
print(TutorMixin.__mro__)
print(tt.__dict__)
print(TutorMixin.__dict__)

help(setattr)
