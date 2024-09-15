# Continue Statement
# Continue Statement skips the current iteration of loop and
# Move to the next iteration.
from idlelib.sidebar import EndLineDelegator

for number in range(10):
    if number % 2 == 0:
       continue
    print(number)

# Logic

# |i| |Condition| O/P
# |0| 0 % 2 == 0--> True | Continue O/P = Skip No O/P
# |1| 1 % 2 == 0--> False | O/P = 1
# |2| 2 % 2 == 0--> True | Continue O/P = Skip No O/P
# |3| 3 % 2 == 0--> False | O/P = 1
# |4| 4 % 2 == 0--> True | Continue O/P = Skip No O/P
# |5| 5 % 2 == 0--> False | O/P = 1
# |6| 6 % 2 == 0--> True | Continue O/P = Skip No O/P
# |7| 7 % 2 == 0--> False | O/P = 1
# |8| 8 % 2 == 0--> True | Continue O/P = Skip No O/P
# |9| 9 % 2 == 0--> False | O/P = 1

# Pass - Can be used in the statement, functions , class and Objects

print("\n")

for number in range(10):
    if number % 2 == 0:
       continue
    else:
     print(number)
