def greeting():
    greeter = input("hello! whats ur name?")
    print("hello",greeter,"nice to meet you")
    for i in range(10):
        print(str(i+1)+". programming is fun!")


def loops(low, high, step = 1):
    for i in range(low, high, step):
        print(i)

def loops2():
    loops(1,11)
    loops(10,0,-1)
    chosenNumber1 = input("you pick a number!")
    loops(1,int(chosenNumber1)+1)
    chosenNumber2 = input("you pick ANOTHER number!")
    loops(int(chosenNumber2),0,-1)

#greeting()
#loops(0,11)
#loops(6,9)
#loops(1,10,2)
#loops(10,0,-1)
#loops2()

def drivingInGermany():
    kmph = input("what is your speed in kmph?")
    print("that is",str(round(int(kmph)/1.609)),"mph")

#drivingInGermany()

d
