#so what I did here was I set up a def main. The first thing I did was set my variables, x and b, which I will get into why I did that later.
#I then made a for in loop, which originally was set at 1000, but I made it have user input, which is n.
#inside of the for loop, I am setting x to equal x+1. Pretty much, every time the for loop runs, it is adding 1 every single time. It sets x as the value plus one, then goes through again.
#then, I set b equal to b+x. What this does, is it saves the value of x inside of b, and adds it to the next number in the loop.
#because we are overriding the var x every single time, this is the only way to save and add the numbers that I could come up with.
#then, I have the print(x) commented out, because it takes a very long time for it to load, but it will list the numbers in order from 1 to n (user input)
#after, I have it print the single number, b, after the for loop finishes.
#there are two reasons why I needed to define x and b outside of the for loop. The first one is because if it was inside of the for loop, it woldn't work.
#instead of actually adding the numbers together, it would just reset the value of both x and b every time it goes through the loop.
#the second reason that I have it outside is because I wanted to print b outside of the for loop
#basic syntax in swift for some reason doesn't let you print variables defined inside of a for loop. So, I have to define it outside first, so I can continue using it outside.
#and that is pretty much it.

def main():
    x=0
    b=0
    n=eval(input("add / list numbers from 1 to ? "))
    for i in range(n):
        x=x+1
        b=b+x
        #print(x)
    print(b)
main()
