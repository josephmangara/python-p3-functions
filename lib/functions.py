#!/usr/bin/env python3

def greet_programmer():
    return 'Hello, programmer!'
print(greet_programmer())

def greet(name):
    return f"Hello, {name}!"
print(greet("Guido"))

def greet_with_default(name="programmer"):
    return f"Hello, {name}!"
print(greet_with_default("Sunny"))

def add(num1, num2):
    return num1 + num2
print(add(541, 3909))

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2
print(halve(4564))

# def my_function(param):
#     print("Running my function")
#     return param + 1
# my_function_return = my_function(5)
# print(my_function_return)

# def say_hi(name):
#     print(f"Hi there, {name}!")

# print(say_hi("Klopp"))

# def stylish_painter():
#     best_hairstyle = "Bob Ross"
#     return "Jean-Michel Basquiat"
#     return best_hairstyle
#     print(best_hairstyle)

# print(stylish_painter())