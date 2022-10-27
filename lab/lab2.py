import math
def main():
    x=eval(input("print the number you want a multiple of: "))
    n=eval(input("how many times do you want the number to have a multiple? "))
    number = 0
    for i in range(n):
        number = number + x
        print(number)

#main()

def pizza():
    small,large = eval(input("What is the price of the small and large pizzas? "))
    spizza = 25 * math.pi #inches
    lpizza = 64 * math.pi #inches
    sprice = round(small/spizza, 2)
    lprice = round(large/lpizza, 2)
    print("The small pizza costs", sprice, "per square inch.")
    print("The large pizza costs", lprice, "per square inch.")
    if sprice == lprice:
        print("they cost the same!!")
    else:
        if sprice > lprice:
            a = round(sprice/lprice,2)
            print("the small pizza costs", a, "times more than the large pizza!")
        else:
            b = round(lprice/sprice,2)
            print("the large pizza costs", b, "times more than the small pizza!")

#pizza()


def name():
    name = input("Enter your name: ")
    for c in name:
        print(c)
#name()


#for item in [0,1,2,"hello", 4.5, [7,8,9],"goodbye"]:
#	print(item)
#	print(type(item))



def nameFlip():
    i=0
    name=input("enter name: ")
    for char in name:
        i=i+1
        print(i,char)

#nameFlip()


s1 = "spam"
s2 = "ni!"

print("The knights who say", s2)
print(3 * s1 + 2 * s2)
print(s1[1])
print(s1[1:3])
print(s1+s2[-1])
print(s1[2] + s2[:2])
print(s1.upper())
print(s2.upper().rjust(10) * 3)
print("\n")
print(s2[0:2].upper())
print(s2+s1 + s2[0:3])
s = ""
toadd = s1[0].upper() + s1[1:4] + " " + s2[0].upper() + s2[1:3]
print(toadd)
for i in range(3):
    s = s + " " + toadd
print(s)
print(s1)
print([s1[0:2], s1[3]])
print(s1[0:2] + s1[3])
print((s1.capitalize() + " " + s2.capitalize() + " ") * 3)


def char():
    x=input("enter scentence: ")
    a=0
    for i in x:
        a = a+1
    print(a)
#char()

def bonus():
    x=input("enter scentence: ")
    a=0
    y = x.replace(" ", "")
    for i in y:
        a = a+1
    print(a)
#bonus()

for item in ["this","one","is","trickier"]:
    for i in item:
        print(i)
