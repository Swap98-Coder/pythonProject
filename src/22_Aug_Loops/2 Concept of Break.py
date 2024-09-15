#break - based on the condition, exit the loop

for i in range(0, 10): # output = 0 1 2 3 4 5
    if i == 5:
        break
    print(i)
# Logic |i| |Condition| O/P
# |0| 0 == 5 --> False | O/P = 0
# |1| 1 == 5 --> False | O/P = 1
# |2| 2 == 5 --> False | O/P = 2
# |3| 3 == 5 --> False | O/P = 3
# |4| 4 == 5 --> False | O/P = 4
# |5| 5 == 5 --> True -> break | O/P = 0

print("\n")

for i in range(0, 10, 1):
    if i == 6:
        print(i)
    else:
        print("No O/P")

# |0| 0 == 6 --> False | O/P = No O/P
# |1| 1 == 6 --> False | O/P = No O/P
# |2| 2 == 6 --> False | O/P = No O/P
# |3| 3 == 6 --> False | O/P = No O/P
# |4| 4 == 6 --> False | O/P = No O/P
# |5| 5 == 6 --> False | O/P = No O/P
# |6| 6 == 6 --> True | O/P = 6
# |7| 7 == 6 --> False | O/P = No O/P
# |8| 8 == 6 --> False | O/P = No O/P
# |9| 9 == 6 --> False | O/P = No O/P

print("\n")

# Pass Condition = Nothing, Ignore, Go Above dont do anything.

for k in range(0, 10, 1):
    if k == 6 or k == 5:
        print(k)
    else:
        pass

print("\n")

for i in range(0, 10, 1):
    if i == 6:
        print(i)
    else:
        pass # Pass its used to "Pass"