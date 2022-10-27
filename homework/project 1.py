#first, I import math, because i need to use sqrt function later in the code
#i then have the user input a,b,c, which are the 3 parts of their quadratic equation they are trying to find the roots for
#then the rest up until the if else is just having it store numbers, and actually solving it.
#originally, I just had it print the second print line, the one in the else statement, but I changed it to give it more depth
#so what we are giving it is two options: one where the roots are the same, because the graph only has one root,
#and the second where its just a normal function where there are two roots.
#a great example for the first one is a,b,c = 1,0,0, which is just the base y=x^2 function, where the vertex is at 0,0
#unfortunately, I didn't see that I also needed to include a for loop, and I'm not quite sure where I can fit one in here
#I sort of picked what to code before thinking about what I needed for said code
#so my idea now is to have a for loop at the start to ask how many roots we want it to find

import math
def quadratic():
    x=eval(input("how many sets of roots do you want to find? "))
    for i in range(x):
        a,b,c = eval(input("if y=ax^2+bx+c, then what are your a,b,c? "))
        filler = math.sqrt(b*b-4*a*c)
        root1 = -b + filler
        root1 = root1/2*a
        root2 = -b - filler
        root2 = root2/2*a
        if root1 == root2:
            print("when y = 0, the graph touches the axis at one point,", root1)
        else:
            print("when y = 0, the graph touches the axis at", root1, "and", root2)

#quadratic()


def height():
    x=eval(input("How many people are in your group? "))
    for i in range(x):
        print("\nperson", i+1)
        feet,inches = eval(input("Enter height in feet and inches, seperated by a comma: "))
        holder = feet*12+inches
        cm = holder * 2.54
        print("height of person", i+1, "in feet and inches:", feet, inches)
        print("height of person", i+1, "in centimeters:", cm)

#height()



def fibonacci():
    a=0
    b=1
    c=0
    array = [0,1]
    print("The first two Fibonacci numbers are 0 and 1.")
    x=eval(input("Enter a positive integer greater than 2 --> "))
    for i in range(x-2):
        c=a+b
        array.append(c)
        print(c)
        a=b
        b=c
    new_array = str(array)[1:-1]
    #credit to python pool for teaching me how to remove brackets for the array (list)
    print("\nThe first", x, "Fibonacci numbers are:", new_array)
    #for this print, I am able to create a bunch of if statements to get the numbers like "10th" and "2nd", but that would be a waste of time, as its not really relevent
    print("So the", x, "Fibonacci number is", c)
    

fibonacci()




