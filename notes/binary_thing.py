def binarySearch(my_List, t):
    n = len(my_List)
    mid = n//2
    if my_List == []:
        return False
    else:
        if my_List[mid] == t:
            return True
        elif t > my_List[mid]:
            return binarySearch(my_List[mid+1:n], t)
        else:
            return binarySearch(my_List[0:mid], t)




nums = [10,20,30,40,50,60,70,80,90]
print(binarySearch(nums, 45))
                                
