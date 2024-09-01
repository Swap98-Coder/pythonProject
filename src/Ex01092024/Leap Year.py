# Leap year program

for year in range(1800, 3000):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f"{year} is not a leap year")
