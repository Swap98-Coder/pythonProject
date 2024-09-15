# Match Statement
# Switch in JAVA
# Match the O/P and Execute
# This concept will work Version > 3.10


# Syntax:
# Match Variable:
#   case pattern1:
        #code block
#   case pattern2:
        #code block
#   case _:           # _ is the default if no other case matches
        #code block


# Write a program to ask the user which browser he want to run automation
browser_name = input("Enter the name of the browser \n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox Code")
    case "chrome":
        print("Execute the chrome Code")
    case "edge":
        print("Execute the edge Code")
    case "safari":
        print("Execute the safari Code")
    case _:
        print("Browser not found")
