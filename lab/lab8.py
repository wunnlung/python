import random

array = []
def main():
    for i in range(9):
        x = random.randrange(1,10)
        while overlap(x):
            x = random.randrange(1,10)
        array.append(x)
    print(array)


def overlap(x):
    for i in array:
        if x == i:
            return True
    return False

#main()


array = []
for i in range(13):
    array.append(0)
x = int(input("how many rolls u wanna do?"))
for i in range(x):
    roll = random.randrange(1,7)
    roll2 = random.randrange(1,7)
    add = roll+roll2
    array[add] = array[add] + 1

for i in range(2,13):

    print(array[i]/x)
