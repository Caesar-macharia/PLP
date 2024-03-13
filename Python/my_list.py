#create an empty list
my_list = []

#append these values to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert a value at the second position
my_list.insert(1, 15)

#extend the list
my_list.extend([50, 60, 70])

#remove the last element
my_list.pop()

#sort in ascending order
my_list.sort()

#find the index of a value
index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)

#print the modified my_list
print("Modified my_list:", my_list)