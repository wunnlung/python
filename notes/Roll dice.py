#roll dice
import random

array = []
for i in range(7):
    array.append(0)
x = int(input("how many rolls u wanna do?"))
for i in range(x):
    roll = random.randrange(1,7)
    array[roll] = array[roll] + 1

for i in range(1,7):
    print(array[i]/x)

