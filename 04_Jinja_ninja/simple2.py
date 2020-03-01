#!/usr/bin/env python3

from jinja2 import Template

first_name = input("Enter your Fname: ")
last_name = input("Enter your Lname: ")

tm = Template("Hello {{ firstname }} {{ lastname }} ")
msg = tm.render(firstname=first_name, lastname=last_name)

print(msg)
