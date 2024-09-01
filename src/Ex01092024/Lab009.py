a = 10
if a == 10:
    print("Hello world")
else:
    print("Not Hello")

a = 10
if a == 25:
    print("Hello world")
else:
    print("Not Hello")

# write a program  to find the max between two

# Logic Building Formula
#1. user input -> two integers
# 2. o/p -> int which ever is greater max number it will return.
# 3. - input method

num1 = float(input("Enter a num1\n"))
num2 = float(input("Enter a num2\n"))

if num1 > num2:
    print("max is ", num1)
else:
    print("max is ", num2)

if num1 > num2:
    print(f"max is {num1}")
else:
    print(f"max is {num2}")
