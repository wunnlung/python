#Todd Shriber - homework 1
#Chapter 1

print("hello world!")
#very similar syntax to swift. In high school I took 2 years of swift

print(2+3)
#this will just print out what 2 + 3 equals

print("2+3=",2+3)
#this will print out the actual quote, "2+3=", and then right next to it what it actually equals

def hello():
    print("hello")
    print("computers are fun")

hello()
#This is very similar to setting a function in swift, with the function name being hello
#when you call the function, or in this case the def, it will run all the code inside, so it will print "hello" and "computers are fun"

#def greet(person):
#    for i in range(10):
 #       print("hello", person)
  #      print("how are you?", i)

#greet("john")
#greet("Emily")
#because the function greet has a varible inside it, you need you define that variable when you are calling it. this is why it is able to have different names

#greet() (I need to comment this out otherwise the rest wont run)
#we can see that this won't work, because we are leaving a variable undefined

#File: Chaos
#def main():
 #   print("This program illustrates a chaotic function")
  #  x = eval(input("Enter a number between 0 and 1:"))
   # for i in range(10):
    #    x = 3.9 * x * (1 - x)
     #   print(x)
             
#main()

#just going in order, the first thing that will print is the very first print, "this program illustrates a chaotic function"
#the next part is a for in loop. pretty much, for every value in 0-10, i will be called. So it will print x 10 times. We are able to actually add i into this part to give us even more chaos if we want
#we are able to see that it just prints the "enter a number" this is because I think im actually supposed to enter a number here
#for some reason, its not running the for loop.
#so after checking again, i now know that something is wrong with the for in loop. Honestly no idea what is happening, but its just not running
#I feel like this is a problem somewhere 
#so i can see that for loops work in other places. I added a for loop right above to the greet func, and it works perfectly fine
#I can also see that it actually works there, as i am having it print I along with the number of the time that it ran the function.
#this is so weird I did all the error testing I can think of and I have no idea why it isnt running like i want it to
#I am able to get all other for in loops to work, but for some reason just not in this function. It really sucks because the next questions involve changing that for in loop.
#however, I do already know the syntax for this, so i think it should be fine later on

#update: after asking my friend willem, I noticed that I am really dumb. Normally what I have done with swift, we don't interact with what we create, we just watch the code run. So it had never occured to me that I was supposed to put in a number on the print
#so it was always working, I was just being really dumb

#also just found out that all of the above isn't homework, so I'm a little sad that I spent so long doing that
#going to comment a lot of it out so it doesn't clutter up the print space

def main():
    for i in range(10):
        print("Hi!")

main()

#5
def main5():
    for i in range(10):
        print(i)
        print("Hi!")

main5()
#what will happen is before each line of hi! it will print the number from 0-10 that it runs
#so it will look like 0\nHi!\n2\n... all the way to 10 (also curious if \n works in python too or if its only swift (it makes the print go on to the next line))
#after running it, I see that it only goes to 9, and not 10. Not too bad of an error on my guess!

#7
#in order to change how many times it runs, you change the number in the range(x). This can be any number you want it to be, as long as its an integer
#in order to do this part, you will need to have the "Hi!" and i on the same print line. You can do this with the code below:
def main7():
    for i in range(10):
        print("Hi!", i)

main7()

#I can think of a couple ways to have it start from 1 and end at 10. But the one that requires the least amount of changes is below:
def main8():
    for i in range(10):
        print("Hi!", i+1)

main8()
#another idea that I have is setting an array of numbers from 1 to 10, and having it do that. Below:

x = [1,2,3,4,5,6,7,8,9,10]
#print(x)
def main9():
    for i in x:
        print("Hi!",i)
main9()
#While this is not AT ALL practical, its still a way that works. Also really suprised that I still know how to do some of these things as its been like 3 years since I touched swift

