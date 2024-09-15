# write a program to take a user age and let him know if he can go the club.
# 21
# F = string formating

# logic building
# 1. user input - data type -->
# o/p -> String -> user if he can go or not.

# 2. Rough logic
# age > 21 -> print can go
# age < 21 -> print cant go

# 3. write the logic

age = int(input("Enter your age\n "))
age = int(age)

if age >= 21:
    print(f"Can go club -> {age}")
else:
    print(f"Cant go with this age -> {age}")



