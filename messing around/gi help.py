lst = [1,3,2,5,4,6,8,7,9]
lst.sort()
print(lst)


data_list = [100,1,3,2,5,4,7,6,9,8,11,202]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print (new_list)
