def height():
    x,y = eval(input("how tall are you in feet and inches? "))
    z = 12 * int(x) + int(y)
    print(str(x), "feet and", str(y), "inches tall is equivelant to", str(z), "inches")

height()
