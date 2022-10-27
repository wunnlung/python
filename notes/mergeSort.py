def mergeSort(someList):
    n = len(someList)
    if n>1:
        mid = n//2
        firstHalf = someList[0:mid]
        mergeSort(firstHalf)
        sendHalf = someList[mid:n]
        mergeSort(secondHalf)
        merge(firstHalf, secondHalf, someList)


def bubbleSort(aList):
    n = len(aList)
    for i in range(n):
        for j in range(n-1):
            if aList[j] > aList[j+1]:
                print(hi)
