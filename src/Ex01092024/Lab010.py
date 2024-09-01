# Program to find the max between 3 numbers

# Logic building

# User input - num1, num2, num3, -> int
# O/p-> int or string with max number

# Logic ? If else - 1 condition
# more 1 condition -> if elif else

# syntax

# if condition 1:
#   print("do 1")
# elif condition 2:
#  print("do 2")
#else:
# print("do 3")

# if condition 1:
#   print("do 1")
# elif condition 2:
#  print("do 2")
#elif condition 3:
#  print ("do 3")
#else:
# print("do 4")

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))

if num1 > num2 and num1 > num3:
    print(f"Num1 is greater -> {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Num2 is greater -> {num2}")
else:
    print(f"Num3 is greater -> {num3}")

if num1 > num2 and num1 > num3:
    print(f"Max is -> {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Max is -> {num2}")
else:
    print(f"Max is -> {num3}")

result= max(num1,num2,num3)
print(result)
