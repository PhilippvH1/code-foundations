#!/usr/bin/env python3

from jinja2 import Template

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def getAge(self):
        return (self.age + 20)

    def getName(self):
        return self.name

    def bark(self):
        return "BORK BORK"


person = Person('Peter', 34)

tm = Template("My name is {{ per.getName() }} and I am {{ per.getAge() }}")
msg = tm.render(per=person)

print(msg)
