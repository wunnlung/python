def isPrime(num):
    for i in range(2,num - 1):
        if (num % i) == 0:
            return False
    return True

#print(isPrime(10))
#print(isPrime(9))
#print(isPrime(25))

def main():
    array = []
    x = int(input("what number do you want to check prime? (I cant grammar): "))
    for i in range(2,x+1):
        prime = isPrime(i)
        if prime == True:
            array.append(i)
    print(array)

main()

        
