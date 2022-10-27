#I created a def called height. Pretty much what happens is 
def height():
    size = eval(input("how many people are in your family?: "))
    for i in range(size):
        x,y = eval(input("how tall is person number "+str(i+1)+ " in feet and inches? "))
        z = 12 * int(x) + int(y)
        print("person number", str(i+1), "is", str(z), "inches tall")

height()
