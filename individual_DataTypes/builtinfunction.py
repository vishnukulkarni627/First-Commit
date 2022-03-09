# id(): This function is used to fetch the address of variable
a = 10
print(a)
print(id(a))

# type(): This function is used to get the type of data
a = 15
print(type(a))
b = 3.142
print(type(b))
c = 3 + 2j
print(type(c))
d = True
print(type(d))

# isinstance(): Returns True if specified object/ value is of specified type, or else false
print(isinstance(5, int))   # True
print(isinstance(3.142, float))    # True
print(isinstance(2+3j, complex))    # True
print(isinstance(True, bool))   # True
print(isinstance(2, bool))    # False
