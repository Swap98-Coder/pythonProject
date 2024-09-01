# Fizz Buzz Program

#if number is multiple of 3 then print fizz
#if number is multiple of 5 then print Buzz
#if number is multiple of 15 then print fizzBuzz

#Logic: first check if the number is multiple of 15 then other two numbers  

for i in range (1, 101):
    if  i%15==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
