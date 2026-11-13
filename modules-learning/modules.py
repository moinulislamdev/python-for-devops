# We can keep in this file for define
# Like : function, class, variables

def greet(name):
    return f"Hello, {name}! Welcome to Python Modules."


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculate_square(number):
    return number ** 2


def get_user_info(name, age, city):
    return f"Name: {name}\nAge: {age}\nCity: {city}"




class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old."

    def get_department(self):
        return f"My department is {self.department}"


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
