#print("lab 11")

def isPalindrome(inputString):
    if len(inputString) == 1 or len(inputString) == 0:
        print("Your string is a palindrome! :D")
    elif inputString[0] == inputString[-1]:
        #newString = inputString.pop[0]
        #newString = newString.pop[-1]
        isPalindrome(inputString[1:-1])
    else:
        print("Your string is not a palindrome D:")
        


isPalindrome("mom")
isPalindrome("racecar")
isPalindrome("roadcar")
isPalindrome("kook")
