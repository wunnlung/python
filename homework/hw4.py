#using % func for the code, as if it returns a 0, then that means the specified number is divisible by the second number
#example, 2000 % 400 = 0, 2000 is divisible by 4

def leapyear():
    year = int(input("Is the current year a leap year? Input here to find out!!!: ")) #user input a year
    if year % 400 == 0: #first, because if it is, its automatically a leap year
        print(year, "is a leap year (divisible by 400)")
    elif year % 4 == 0: #if divisible by 4, there are two options, if it is divisible by 100 or not
        if year % 100 == 0:
            print(year, "is not a leap year (divisible by 4 and 100)")
        else:
            print(year, "is a leap year (divisble by 4 and not by 100)")
    else: #this is if it is not divisible by 4
        print(year, "is not a leap year (not divisble by 4)")
    

leapyear()
