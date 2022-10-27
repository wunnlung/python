s1 = [2,1,4,3,2]
s2 = ["c", "a", "b"]
##print(s1+s2)
##print(3*s1 + 2*s2)
##print(s1[1])
##print(s1[1:3])
##print(s1+s2[-1])

#s1.remove(2)
#s1.sort()
#s1.append([s2.index("b")])
#s2.pop(s1.pop(2))
#s2.insert(s1[0],"d")
#print(s1)
#print(s2.)



def Count(myList, x):
    count = 0
    for i in myList:
        if x == i:
            count +=1
    return count

def Isin(myList, x):
    for i in myList:
        if x == i:
            return True
    return False

def Index(myList, x):
    count = 0
    for i in myList:
        if i != x:
            count += 1
        else:
            return count
    return None

def Reverse(myList):
    newList = []
    while myList != []:
        newList.append(myList[-1])
        myList.pop(-1)
    return newList

#def Sort(myList):
    

def main():
    freq = {}
    infile = open("classlist.txt","r")
    names = infile.read()
    for ch in names: #for each charater in names
        if not (ch in freq):
            freq[ch] = 1 #creates new entry in tuple
        else:
            freq[ch] = freq[ch] + 1 #adds 1 to an already existing tuple
    x = list(freq.items())
    
    x.sort(key=getFreq, reverse=True)

    for i in x:
        string = str(i)
        string = string.replace("(","")
        string = string.replace(")","")
        string = string.replace("'","")
        string = string.replace(","," :")
        print(string)
        
        


def getFreq(key):
    return key[1]


main()

print(Count(s1,3))



