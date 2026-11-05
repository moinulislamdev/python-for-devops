# def sum():
#     a = 20
#     b = 10
#     return a + b

# print(f"The result is : {sum()}")

# def sum(num1, num2):
#     num1 = num1
#     num2 = num2
#     print(num1 * num2)

# sum(5,2)
# sum(6,2)
# sum(7,2)


# def sum(num1, num2):
#     num1 = num1
#     num2 = num2
#     return num1 * num2

# print(f"The multiplication is : {sum(5,1)}")
# print(f"The multiplication is : {sum(5,2)}")
# print(f"The multiplication is : {sum(5,3)}")
# print(f"The multiplication is : {sum(5,4)}")


# def user_info(name, age, email):
#     print(f"User info is : \nName = {name}\nAge = {age}\nEmail = {email}")

# user_info("Md. Moinul Islam", 25, "mdmoinul@gmail.com")
# user_info("Kobita", 30, "shoron@gmail.com")


# def user_info(name, age, email):
#     return f"\nUser name : {name}\nUser email : {email}\nUser age : {age}"
# print("User Details : ")
# print(user_info("Shoron", 27, "shoron@gmail.com"))
# print(user_info("Mohan", 25, "mohan@gmail.com"))



# A proper Example


# # For customer 1
# amount1 = 1000
# city1 = "Rang"

# if city1 == "Raj":
#     tax_rates1 = 1.4
# elif city1 == "Dh":
#     tax_rates1 = 1.8
# else:
#     tax_rates1 = 1.2

# print(f"Customer1 Payable amount = {amount1 * tax_rates1}")


# # For customer 2
# amount2 = 2000
# city2 = "Dh"

# if city2 == "Raj":
#     tax_rates2 = 1.4
# elif city2 == "Dh":
#     tax_rates2 = 1.8
# else:
#     tax_rates2 = 1.2

# print(f"Customer2 Payable amount = {amount2 * tax_rates2}")


# # For customer 3
# amount3 = 5000
# city3 = "Raj"

# if city3 == "Raj":
#     tax_rates3 = 1.4
# elif city3 == "Dh":
#     tax_rates3 = 1.8
# else:
#     tax_rates3 = 1.2

# print(f"Customer3 Payable amount = {amount3 * tax_rates3}")




def tax_calculation(amount, city):
    if city == "Raj":
        tax_rates = 1.4
    elif city == "Dh":
        tax_rates = 1.8
    else:
        tax_rates = 1.2
    
    return amount * tax_rates

print(f"Customer1 payable amount = {tax_calculation(2000, 'Dh')}TK.")
print(f"Customer2 payable amount = {tax_calculation(1000, 'Rang')}TK.")
print(f"Customer3 payable amount = {tax_calculation(3000, 'Raj')}TK.")