# Construction of list
l = [1, 2, 3, 4]   #Data type with homogenous type of data
print(l)
l1 = [1, 1.2, "hai", [10, 20], 2+3j, (1, 2), {1, 2, 40}]   # Data type with hetrogenous type of data
print(l1)
l2 = list([1, 2, 3])  #Data type with constructor as a list
print(l2)
# Indexing a list
print(l1[6])
print(l1[2])
# Fetching data from list inside a list
print(l1[3][1])
print(l1[5][1])
# Slicing a list
l3 = [1, 1.2, "hai", [10, 20], 2+3j, (1, 2), {1, 2, 40}]
print(l3[0:4:1])
# Merging two list
print(l + l1)
print([*l, *l1])
# Adding the elements to the list 1st Method: Appending the list
l4 = [1, 2]
l4.append([3, 4])   #Appending int data type
# print(l4)
l4.append([1.2, 2.4, 5, "vishnu"])    #Appending the float data type
# print(l4)
l4.append([2+3j, 1.2, 3, True])   #Appending the complex and boolean data type
# print(l4)
# Adding the elements to the list second Method: Extend
l4.extend([9, 8, 5, "vishnu", 2])
# print(l4)
# Adding the elements to the list second Method: Insert
l4.insert(2, (45, 66))
# print(l4)
# Popping the element inside the list 1st method
print(l4.pop(2))
print(l4.pop(8))    # index error occur if we pass out of index value
print(l4)
# Removing the element inside the list 2nd method
# l4.remove(3)
# print(l4)
# Deleting and deallocating memory from iterable
del l4
# Sorting the list
l5 = ['vishnu', 'Vishnu', 'kulkarni']
l5.sort()
print(l5)   # ['Vishnu', 'kulkarni', 'vishnu']
l5.sort(reverse= True)
print(l5)   #['vishnu', 'kulkarni', 'Vishnu']
l5.sort(key=len)
print(l5)   #['vishnu', 'Vishnu', 'kulkarni']
# Index length
print(l5.index('Vishnu'))   #1
# print(l5.index("visu"))   # value error
l6 = ['vishnu', 'kulkarni', 'is', 'vishnu', 'kulkarni' ]
print(l6.count('vishnu'))   # 2
print(l6.count("hello"))    #No value means returns 0




