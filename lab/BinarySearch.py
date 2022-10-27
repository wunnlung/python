#recursive divide and conquer
#only works if list is already sorted
#returns true if found and false if not
def binarySearch(my_list, low, high, t):
    n = len(my_list)
    mid = n//2
    if my_list == []:
        return False
    else:
        if my_list[low] == t:
            return low
        elif my_list[high] == t:
            return high
        elif my_list[low] < t and my_list[high] > t:
            return binarySearch(my_list, low+1, high-1, t)
        
##        if my_list[mid] == t:
##            return True
##        elif t > my_list[mid]:
##            return binarySearch(my_list[mid+1:n], t)
##        else:
##            return binarySearch(my_list[0:mid],t)



def binarySearch2(my_list, low, high, t):
    if my_list == []:
        return False
    else:
        while my_list[high] != t:
            low = low + 1
            high = high - 1
            if high <= 0:
                return False
    if my_list[low] == t:
        return low
    elif my_list[high] == t:
        return high

print(binarySearch2([1,3,5,9,13], 0, 4, 9))
print(binarySearch2([2,4,10,15,16,20], 0, 5, 3))


#print(binarySearch([1,3,5,9,13], 9))
#print(binarySearch([2,4,10,15,16,20], 3))


#step 1: find the min position among sorted value
#move it to the top/ front of the remaining unsorted values

def selectionSort(my_list):
    n = len(my_list)
    for i in range(n-1):
        minPos = i
        for j in range(i+1,n):
            minPos = j
