#!/usr/bin/env python
import sys
import math
print("Calculator_3.0")

num_1 = input("Enter a number or skip: ")
print("Select an operation: ")
print("1.Addition (+)")
print("2.Subtraction (-)")
print("3.Multiplication (*)")
print("4.Division (/)")
print("5.Power (^)")
print("6.Factorial (!)")
user_input = (input(""))
if user_input == "":
    pass
elif user_input == "1":
    pass
elif user_input == "2":
    pass
elif user_input == "3":
    pass
elif user_input == "4":
    pass
elif user_input == "5":
    pass
elif user_input == "6":
	print(num_1, "!", "=", math.factorial(float(num_1)))
	sys.exit()
elif user_input == "+":
    pass
elif user_input == "-":
    pass
elif user_input == "*":
    pass
elif user_input == "/":
    pass
elif user_input == "^":
    pass
elif user_input == "!":
	print(num_1, "!", "=", math.factorial(float(num_1)))
	sys.exit()
else:
    raise Exception("Invalid input for the first operation.")
num_2 = input("Enter a number or skip: ")
print("Select an operation: ")
print("1.Addition (+)")
print("2.Subtraction (-)")
print("3.Multiplication (*)")
print("4.Division (/)")
print("5.Power (^)")
print("6.Factorial (!)")
user_input_2 = (input(""))
if user_input_2 == "":
    pass
elif user_input_2 == "1":
    pass
elif user_input_2 == "2":
    pass
elif user_input_2 == "3":
    pass
elif user_input_2 == "4":
    pass
elif user_input_2 == "5":
    pass
elif user_input_2 == "6":
	print(num_2, "!", "=",  math.factorial(float(num_2)))
	sys.exit()
elif user_input_2 == "+":
    pass
elif user_input_2 == "-":
    pass
elif user_input_2 == "*":
    pass
elif user_input_2 == "/":
    pass
elif user_input_2 == "^":
    pass
elif user_input_2 == "!":
	print(num_2, "!", "=", math.factorial(float(num_2)))
	sys.exit()
else:
    raise Exception("Invalid input for the first operation.")
num_3 = input("Enter a number or skip: ")
if user_input == "" and user_input_2 == "":
    print("You need an operation for proper use.")
    sys.exit()
if num_1 == "" and num_2 == "" and num_3 == "":
    raise Exception("You need at least two numbers, for a calculation.")
if user_input == "1" and user_input_2 == "":
    print(num_1, "+", num_2, "=", (float(num_1) + float(num_2)))
elif user_input == "+" and user_input_2 == "":
    print(num_1, "+", num_2, "=", (float(num_1) + float(num_2)))
elif user_input == "2" and user_input_2 == "":
    print(num_1, "-", num_2, "=", (float(num_1) - float(num_2)))
elif user_input == "-" and user_input_2 == "":
    print(num_1, "-", num_2, "=", (float(num_1) - float(num_2)))
elif user_input == "3" and user_input_2 == "":
    print(num_1, "*", num_2, "=", (float(num_1) * float(num_2)))
elif user_input == "*" and user_input_2 == "":
    print(num_1, "*", num_2, "=", (float(num_1) * float(num_2)))
elif user_input == "4" and user_input_2 == "":
    print(num_1, "/", num_2, "=", (float(num_1) / float(num_2)))
elif user_input == "/" and user_input_2 == "":
    print(num_1, "/", num_2, "=", (float(num_1) / float(num_2)))
elif user_input == "5" and user_input_2 == "":
    print(num_1, "^", num_2, "=", (float(pow(float(num_1), float(num_2)))))
elif user_input == "^" and user_input_2 == "":
    print(num_1, "^", num_2, "=", float(pow(float(num_1), float(num_2))))
elif user_input == "" and user_input_2 == "1":                                         # Changes here
    print(num_2, "+", num_3, "=", (float(num_2) + float(num_3)))
elif user_input == "" and user_input_2 == "+":
    print(num_2, "+", num_3, "=", (float(num_2) + float(num_3)))
elif user_input == "" and user_input_2 == "2":
    print(num_2, "-", num_3, "=", (float(num_2) - float(num_3)))
elif user_input == "" and user_input_2 == "-":
    print(num_2, "-", num_3, "=", (float(num_2) - float(num_3)))
elif user_input == "" and user_input_2 == "3":
    print(num_2, "*", num_3, "=", (float(num_2) * float(num_3)))
elif user_input == "" and user_input_2 == "*":
    print(num_2, "*", num_3, "=", (float(num_2) * float(num_3)))
elif user_input == "" and user_input_2 == "4":
    print(num_2, "/", num_3, "=", (float(num_2) / float(num_3)))
elif user_input == "" and user_input_2 == "/":
    print(num_2, "/", num_3, "=", (float(num_2) / float(num_3)))
elif user_input == "" and user_input_2 == "5":
    print(num_2, "^", num_3, "=", (pow(float(num_2), float(num_3))))
elif user_input == "" and user_input_2 == "^":
    print(num_2, "^", num_3, "=", (pow(float(num_2), float(num_3))))
elif user_input == "1" and user_input_2 == "1":                                    # Addition - Addition
    print(num_1, "+", num_2, "+", num_3, "=", (float(num_1) + float(num_2) + float(num_3)))
elif user_input == "1" and user_input_2 == "+":
    print(num_1, "+", num_2, "+", num_3, "=", (float(num_1) + float(num_2) + float(num_3)))
elif user_input == "+" and user_input_2 == "1":
    print(num_1, "+", num_2, "+", num_3, "=", (float(num_1) + float(num_2) + float(num_3)))
elif user_input == "+" and user_input_2 == "+":
    print(num_1, "+", num_2, "+", num_3, "=", (float(num_1) + float(num_2) + float(num_3)))
elif user_input == "1" and user_input_2 == "2":                                    # Addition - Subtraction
    print(num_1, "+", num_2, "-", num_3, "=", (float(num_1) + float(num_2) - float(num_3)))
elif user_input == "1" and user_input_2 == "-":
    print(num_1, "+", num_2, "-", num_3, "=", (float(num_1) + float(num_2) - float(num_3)))
elif user_input == "+" and user_input_2 == "2":
    print(num_1, "+", num_2, "-", num_3, "=", (float(num_1) + float(num_2) - float(num_3)))
elif user_input == "+" and user_input_2 == "-":
    print(num_1, "+", num_2, "-", num_3, "=", (float(num_1) + float(num_2) - float(num_3)))
elif user_input == "1" and user_input_2 == "3":                                    # Addition - Multiplication
    print(num_1, "+", num_2, "*", num_3, "=", (float(num_1) + float(num_2) * float(num_3)))
elif user_input == "1" and user_input_2 == "*":
    print(num_1, "+", num_2, "*", num_3, "=", (float(num_1) + float(num_2) * float(num_3)))
elif user_input == "+" and user_input_2 == "3":
    print(num_1, "+", num_2, "*", num_3, "=", (float(num_1) + float(num_2) * float(num_3)))
elif user_input == "+" and user_input_2 == "*":
    print(num_1, "+", num_2, "*", num_3, "=", (float(num_1) + float(num_2) * float(num_3)))
elif user_input == "1" and user_input_2 == "4":                                    # Addition - Division
    print(num_1, "+", num_2, "/", num_3, "=", (float(num_1) + float(num_2) / float(num_3)))
elif user_input == "1" and user_input_2 == "/":
    print(num_1, "+", num_2, "/", num_3, "=", (float(num_1) + float(num_2) / float(num_3)))
elif user_input == "+" and user_input_2 == "4":
    print(num_1, "+", num_2, "/", num_3, "=", (float(num_1) + float(num_2) / float(num_3)))
elif user_input == "+" and user_input_2 == "/":
    print(num_1, "+", num_2, "/", num_3, "=", (float(num_1) + float(num_2) / float(num_3)))
elif user_input == "1" and user_input_2 == "5":                                    # Addition - Power
    print(num_1, "+", num_2, "^", num_3, "=", (float(num_1) + (pow(float(num_2), float(num_3)))))
elif user_input == "1" and user_input_2 == "^":
    print(num_1, "+", num_2, "^", num_3, "=", (float(num_1) + pow(float(num_2), float(num_3))))
elif user_input == "+" and user_input_2 == "5":
    print(num_1, "+", num_2, "^", num_3, "=", (float(num_1) + pow(float(num_2), float(num_3))))
elif user_input == "+" and user_input_2 == "^":
    print(num_1, "+", num_2, "^", num_3, "=", (float(num_1) + pow(float(num_2), float(num_3))))
elif user_input == "2" and user_input_2 == "1":                                    # Subtraction - Addition
    print(num_1, "-", num_2, "+", num_3, "=", (float(num_1) - float(num_2) + float(num_3)))
elif user_input == "2" and user_input_2 == "+":
    print(num_1, "-", num_2, "+", num_3, "=", (float(num_1) - float(num_2) + float(num_3)))
elif user_input == "-" and user_input_2 == "1":
    print(num_1, "-", num_2, "+", num_3, "=", (float(num_1) - float(num_2) + float(num_3)))
elif user_input == "-" and user_input_2 == "+":
    print(num_1, "-", num_2, "+", num_3, "=", (float(num_1) - float(num_2) + float(num_3)))
elif user_input == "2" and user_input_2 == "2":                                    # Subtraction - Subtraction
    print(num_1, "-", num_2, "-", num_3, "=", (float(num_1) - float(num_2) - float(num_3)))
elif user_input == "2" and user_input_2 == "-":
    print(num_1, "-", num_2, "-", num_3, "=", (float(num_1) - float(num_2) - float(num_3)))
elif user_input == "-" and user_input_2 == "2":
    print(num_1, "-", num_2, "-", num_3, "=", (float(num_1) - float(num_2) - float(num_3)))
elif user_input == "-" and user_input_2 == "-":
    print(num_1, "-", num_2, "-", num_3, "=", (float(num_1) - float(num_2) - float(num_3)))
elif user_input == "2" and user_input_2 == "3":                                    # Subtraction - Multiplication
    print(num_1, "-", num_2, "*", num_3, "=", (float(num_1) - float(num_2) * float(num_3)))
elif user_input == "2" and user_input_2 == "*":
    print(num_1, "-", num_2, "*", num_3, "=", (float(num_1) - float(num_2) * float(num_3)))
elif user_input == "-" and user_input_2 == "3":
    print(num_1, "-", num_2, "*", num_3, "=", (float(num_1) - float(num_2) * float(num_3)))
elif user_input == "-" and user_input_2 == "*":
    print(num_1, "-", num_2, "*", num_3, "=", (float(num_1) - float(num_2) * float(num_3)))
elif user_input == "2" and user_input_2 == "4":                                    # Subtraction - Division
    print(num_1, "-", num_2, "/", num_3, "=", (float(num_1) - float(num_2) / float(num_3)))
elif user_input == "2" and user_input_2 == "/":
    print(num_1, "-", num_2, "/", num_3, "=", (float(num_1) - float(num_2) / float(num_3)))
elif user_input == "-" and user_input_2 == "4":
    print(num_1, "-", num_2, "/", num_3, "=", (float(num_1) - float(num_2) / float(num_3)))
elif user_input == "-" and user_input_2 == "/":
    print(num_1, "-", num_2, "/", num_3, "=", (float(num_1) - float(num_2) / float(num_3)))
elif user_input == "2" and user_input_2 == "5":                                    # Subtraction - Power
    print(num_1, "-", num_2, "^", num_3, "=", (float(num_1) - pow(float(num_2), float(num_3))))
elif user_input == "2" and user_input_2 == "^":
    print(num_1, "-", num_2, "^", num_3, "=", (float(num_1) - pow(float(num_2), float(num_3))))
elif user_input == "-" and user_input_2 == "5":
    print(num_1, "-", num_2, "^", num_3, "=", (float(num_1) - pow(float(num_2), float(num_3))))
elif user_input == "-" and user_input_2 == "^":
    print(num_1, "-", num_2, "^", num_3, "=", (float(num_1) - pow(float(num_2), float(num_3))))
elif user_input == "3" and user_input_2 == "1":                                    # Multiplication - Addition
    print(num_1, "*", num_2, "+", num_3, "=", (float(num_1) * float(num_2) + float(num_3)))
elif user_input == "3" and user_input_2 == "+":
    print(num_1, "*", num_2, "+", num_3, "=", (float(num_1) * float(num_2) + float(num_3)))
elif user_input == "*" and user_input_2 == "1":
    print(num_1, "*", num_2, "+", num_3, "=", (float(num_1) * float(num_2) + float(num_3)))
elif user_input == "*" and user_input_2 == "+":
    print(num_1, "*", num_2, "+", num_3, "=", (float(num_1) * float(num_2) + float(num_3)))
elif user_input == "3" and user_input_2 == "2":                                    # Multiplication - Subtraction
    print(num_1, "*", num_2, "-", num_3, "=", (float(num_1) * float(num_2) - float(num_3)))
elif user_input == "3" and user_input_2 == "-":
    print(num_1, "*", num_2, "-", num_3, "=", (float(num_1) * float(num_2) - float(num_3)))
elif user_input == "*" and user_input_2 == "2":
    print(num_1, "*", num_2, "-", num_3, "=", (float(num_1) * float(num_2) - float(num_3)))
elif user_input == "*" and user_input_2 == "-":
    print(num_1, "*", num_2, "-", num_3, "=", (float(num_1) * float(num_2) - float(num_3)))
elif user_input == "3" and user_input_2 == "3":                                    # Multiplication - Multiplication
    print(num_1, "*", num_2, "*", num_3, "=", (float(num_1) * float(num_2) * float(num_3)))
elif user_input == "3" and user_input_2 == "*":
    print(num_1, "*", num_2, "*", num_3, "=", (float(num_1) * float(num_2) * float(num_3)))
elif user_input == "*" and user_input_2 == "3":
    print(num_1, "*", num_2, "*", num_3, "=", (float(num_1) * float(num_2) * float(num_3)))
elif user_input == "*" and user_input_2 == "*":
    print(num_1, "*", num_2, "*", num_3, "=", (float(num_1) * float(num_2) * float(num_3)))
elif user_input == "3" and user_input_2 == "4":                                    # Multiplication - Division
    print(num_1, "*", num_2, "/", num_3, "=", (float(num_1) * float(num_2) / float(num_3)))
elif user_input == "3" and user_input_2 == "/":
    print(num_1, "*", num_2, "/", num_3, "=", (float(num_1) * float(num_2) / float(num_3)))
elif user_input == "*" and user_input_2 == "4":
    print(num_1, "*", num_2, "/", num_3, "=", (float(num_1) * float(num_2) / float(num_3)))
elif user_input == "*" and user_input_2 == "/":
    print(num_1, "*", num_2, "/", num_3, "=", (float(num_1) * float(num_2) / float(num_3)))
elif user_input == "3" and user_input_2 == "5":                                    # Multiplication - Power
    print(num_1, "*", num_2, "^", num_3, "=", (float(num_1) * pow(float(num_2), float(num_3))))
elif user_input == "3" and user_input_2 == "^":
    print(num_1, "*", num_2, "^", num_3, "=", (float(num_1) * pow(float(num_2), float(num_3))))
elif user_input == "*" and user_input_2 == "5":
    print(num_1, "*", num_2, "^", num_3, "=", (float(num_1) * pow(float(num_2), float(num_3))))
elif user_input == "*" and user_input_2 == "^":
    print(num_1, "*", num_2, "^", num_3, "=", (float(num_1) * pow(float(num_2), float(num_3))))
elif user_input == "4" and user_input_2 == "1":                                    # Division - Addition
    print(num_1, "/", num_2, "+", num_3, "=", (float(num_1) / float(num_2) + float(num_3)))
elif user_input == "4" and user_input_2 == "+":
    print(num_1, "/", num_2, "+", num_3, "=", (float(num_1) / float(num_2) + float(num_3)))
elif user_input == "/" and user_input_2 == "1":
    print(num_1, "/", num_2, "+", num_3, "=", (float(num_1) / float(num_2) + float(num_3)))
elif user_input == "/" and user_input_2 == "+":
    print(num_1, "/", num_2, "+", num_3, "=", (float(num_1) / float(num_2) + float(num_3)))
elif user_input == "4" and user_input_2 == "2":                                    # Division - Subtraction
    print(num_1, "/", num_2, "-", num_3, "=", (float(num_1) / float(num_2) - float(num_3)))
elif user_input == "4" and user_input_2 == "-":
    print(num_1, "/", num_2, "-", num_3, "=", (float(num_1) / float(num_2) - float(num_3)))
elif user_input == "/" and user_input_2 == "2":
    print(num_1, "/", num_2, "-", num_3, "=", (float(num_1) / float(num_2) - float(num_3)))
elif user_input == "/" and user_input_2 == "-":
    print(num_1, "/", num_2, "-", num_3, "=", (float(num_1) / float(num_2) - float(num_3)))
elif user_input == "4" and user_input_2 == "3":                                    # Division - Multiplication
    print(num_1, "/", num_2, "*", num_3, "=", (float(num_1) / float(num_2) * float(num_3)))
elif user_input == "4" and user_input_2 == "*":
    print(num_1, "/", num_2, "*", num_3, "=", (float(num_1) / float(num_2) * float(num_3)))
elif user_input == "/" and user_input_2 == "3":
    print(num_1, "/", num_2, "*", num_3, "=", (float(num_1) / float(num_2) * float(num_3)))
elif user_input == "/" and user_input_2 == "*":
    print(num_1, "/", num_2, "*", num_3, "=", (float(num_1) / float(num_2) * float(num_3)))
elif user_input == "4" and user_input_2 == "4":                                    # Division - Division
    print(num_1, "/", num_2, "/", num_3, "=", (float(num_1) / float(num_2) / float(num_3)))
elif user_input == "4" and user_input_2 == "/":
    print(num_1, "/", num_2, "/", num_3, "=", (float(num_1) / float(num_2) / float(num_3)))
elif user_input == "/" and user_input_2 == "4":
    print(num_1, "/", num_2, "/", num_3, "=", (float(num_1) / float(num_2) / float(num_3)))
elif user_input == "/" and user_input_2 == "/":
    print(num_1, "/", num_2, "/", num_3, "=", (float(num_1) / float(num_2) / float(num_3)))
elif user_input == "4" and user_input_2 == "5":                                    # Division - Power
    print(num_1, "/", num_2, "^", num_3, "=", (float(num_1) / pow(float(num_2), float(num_3))))
elif user_input == "4" and user_input_2 == "^":
    print(num_1, "/", num_2, "^", num_3, "=", (float(num_1) / pow(float(num_2), float(num_3))))
elif user_input == "/" and user_input_2 == "5":
    print(num_1, "/", num_2, "^", num_3, "=", (float(num_1) / pow(float(num_2), float(num_3))))
elif user_input == "/" and user_input_2 == "^":
    print(num_1, "/", num_2, "^", num_3, "=", (float(num_1) / pow(float(num_2), float(num_3))))
elif user_input == "5" and user_input_2 == "1":                                    # Power - Addition
    print(num_1, "^", num_2, "+", num_3, "=", (pow(float(num_1), float(num_2)) + float(num_3)))
elif user_input == "5" and user_input_2 == "+":
    print(num_1, "^", num_2, "+", num_3, "=", (pow(float(num_1), float(num_2)) + float(num_3)))
elif user_input == "^" and user_input_2 == "1":
    print(num_1, "^", num_2, "+", num_3, "=", (pow(float(num_1), float(num_2) + float(num_3))))
elif user_input == "^" and user_input_2 == "+":
    print(num_1, "^", num_2, "+", num_3, "=", (pow(float(num_1), float(num_2)) + float(num_3)))
elif user_input == "5" and user_input_2 == "2":                                    # Power - Subtraction
    print(num_1, "^", num_2, "-", num_3, "=", (pow(float(num_1), float(num_2)) - float(num_3)))
elif user_input == "5" and user_input_2 == "-":
    print(num_1, "^", num_2, "-", num_3, "=", (pow(float(num_1), float(num_2)) - float(num_3)))
elif user_input == "^" and user_input_2 == "2":
    print(num_1, "^", num_2, "-", num_3, "=", (pow(float(num_1), float(num_2)) - float(num_3)))
elif user_input == "^" and user_input_2 == "-":
    print(num_1, "^", num_2, "-", num_3, "=", (pow(float(num_1), float(num_2)) - float(num_3)))
elif user_input == "5" and user_input_2 == "3":                                    # Power - Multiplication
    print(num_1, "^", num_2, "*", num_3, "=", (pow(float(num_1), float(num_2)) * float(num_3)))
elif user_input == "5" and user_input_2 == "*":
    print(num_1, "^", num_2, "*", num_3, "=", (pow(float(num_1), float(num_2)) * float(num_3)))
elif user_input == "^" and user_input_2 == "3":
    print(num_1, "^", num_2, "*", num_3, "=", (pow(float(num_1), float(num_2)) * float(num_3)))
elif user_input == "^" and user_input_2 == "*":
    print(num_1, "^", num_2, "*", num_3, "=", (pow(float(num_1), float(num_2)) * float(num_3)))
elif user_input == "5" and user_input_2 == "4":                                    # Power - Division
    print(num_1, "^", num_2, "/", num_3, "=", (pow(float(num_1), float(num_2)) / float(num_3)))
elif user_input == "5" and user_input_2 == "/":
    print(num_1, "^", num_2, "/", num_3, "=", (pow(float(num_1), float(num_2)) / float(num_3)))
elif user_input == "^" and user_input_2 == "4":
    print(num_1, "^", num_2, "/", num_3, "=", (pow(float(num_1), float(num_2)) / float(num_3)))
elif user_input == "^" and user_input_2 == "/":
    print(num_1, "^", num_2, "/", num_3, "=", (pow(float(num_1), float(num_2)) / float(num_3)))
elif user_input == "5" and user_input_2 == "5":
    action = pow(float(num_1), float(num_2))                                         # Power - Power
    print(num_1, "^", num_2, "^", num_3, "=", (pow(float(action), float(num_3))))
elif user_input == "5" and user_input_2 == "^":
    action = pow(float(num_1), float(num_2))
    print(num_1, "^", num_2, "^", num_3, "=", (pow(float(action), float(num_3))))
elif user_input == "^" and user_input_2 == "5":
    action = pow(float(num_1), float(num_2))
    print(num_1, "^", num_2, "^", num_3, "=", (pow(float(action), float(num_3))))
elif user_input == "^" and user_input_2 == "^":
    action = pow(float(num_1), float(num_2))
    print(num_1, "^", num_2, "^", num_3, "=", (pow(float(action), float(num_3))))
else:
    raise Exception("An error has occured.")