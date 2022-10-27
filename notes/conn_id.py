#this program will generate a user id from the inputted name
def main():
   x=input("whats ur name: ")
   split = x.split()
   print(x[0].lower()+split[1].lower())

   inputfile = open("classlist.txt", "r")
   hehe2 = inputfile.readlines()
   for name in hehe2:
       split = name.split()
       print("\nyour email is: " + name[0].lower()+split[1].lower() + "@conncoll.edu")
 
#main()


def nameflip():
    i=0
    name=input("enter name: ")
    numChars = 0
    for c in name:
        i=i+1
        #print(i,c)
        if c != " ":
            print(numChars+1, c)

    if numChars < 6:
        print("your name is shorter than average")
    elif numChars == 6:
        print("your name is average in length")
    else:
        print("your name is longer than average")

nameflip()
