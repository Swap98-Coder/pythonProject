# Grade Calculator:
# Write a program that calculate and displays the letter grade
# for a given numerical score( e.g A, B, C, or F)
# based on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# logix building formula

numerical_score = int(input("Enter your numberical score"))
if numerical_score >=90 and numerical_score <= 100:
    print("Your Grade is A")
elif numerical_score >=80 and numerical_score <=89:
    print("Your Grade is B")
elif numerical_score >=70 and numerical_score <=79:
    print("Your Grade is C")
elif numerical_score >=60 and numerical_score <=69:
    print("Your Grade is D")
elif numerical_score >100:
    print("Enter Valid score")
else:
    print("Your Grade is F")

numerical_score = int(input("Enter your numberical score"))
if 90 <= numerical_score <= 100:
    print("Your Grade is A")
elif 80 <= numerical_score <= 89:
    print("Your Grade is B")
elif 70 <= numerical_score <= 79:
    print("Your Grade is C")
elif 60 <= numerical_score <= 69:
    print("Your Grade is D")
elif 100 < numerical_score <= 0:
    print("Enter Valid score")
else:
    print("Your Grade is F")
