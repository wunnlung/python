inputfile = open("collosus.txt", "r")
a=0
for line in inputfile:
    if line == "\n":
        print(line)
    else:
        a=a+1
        print(a, line)

inputfile = open("collosus.txt", "r")
listOfLines = inputfile.readlines()
print(listOfLines)
