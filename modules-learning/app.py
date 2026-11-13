# import modules
# print(modules.greet("Moinul"))
# print("Addition:", modules.add(20, 10))
# print("Subtraction:", modules.subtract(20, 10))
# print("Multiplication:", modules.multiply(20, 10))
# print("Division:", modules.divide(20, 10))
# print("Square:", modules.calculate_square(5))
# print(modules.get_user_info("Moinul", 26, "Dhaka"))

# import modules as m
# print(m.greet("Moinul"))
# print("Addition:", m.add(20, 10))
# print("Subtraction:", m.subtract(20, 10))
# print("Multiplication:", m.multiply(20, 10))
# print("Division:", m.divide(20, 10))
# print("Square:", m.calculate_square(5))
# print(m.get_user_info("Moinul", 26, "Dhaka"))


# from modules import get_user_info, divide, calculate_square
# print("Division:", divide(20, 10))
# print("Square:", calculate_square(5))
# print(get_user_info("Moinul", 26, "Dhaka"))


from modules import Student, Calculator
# student1 = Student("Moinul", 26, "Computer Science")
# print(student1.introduce())
# print(student1.get_department())

calculator = Calculator()
print("Addition:", calculator.add(20, 10))
print("Subtraction:", calculator.subtract(20, 10))
print("Multiplication:", calculator.multiply(20, 10))
print("Division:", calculator.divide(20, 10))