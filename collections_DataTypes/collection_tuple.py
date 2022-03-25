# Tuple : accepts homogenous and heterogenous type of data
# Should be seperated by comma
# Denoted by ()
# It is an immutable data type
# Here for tuples indexing and slicing can be done
# Creation of tuples -- 1st Method
t = ()
# Creation of tuples -- using constructor --- 2nd Method
t = tuple()

# Eg1: Creating a tuple containing single tuple
t = (1,)
print(t)         # (1,)
# Eg2: Creating a tuple containing int data type
t1 = (1, 2, 3, 4)
print(t1)       # (1, 2, 3, 4)
# Eg3: Creating a tuple containing float data type
t2 = (1.1, 1.2, 1.3, 1.5)
print(t2)       # (1.1, 1.2, 1.3, 1.5)
# Eg4: Creating a tuple containing complex number
t3 = (2+3j, 3+5j, 6+9j)
print(t3)   # ((2+3j), (3+5j), (6+9j))
t4 = (10, 1.25, 'hello', [1, 2, 3, 'hai'], 4+6j, 10)
print(t4[-2])   # 4+6j
print(t4)   # (10, 1.25, 'hello', [1, 2, 3, 'hai'], (4+6j), 10)
print(t4[3][2])     # 3
# Count : returns number of times specified value occurs in a tuple
print(t4.count(10))     # 2
# Index : returns the first occurance of the element specified
# If we pass value if it is not present value error occurs
print(t4.index(10))  # 0

#  Data types like tuple,list,strings can be indexed and sliced
#  Here datatypes are ordered, sequenced
#  All sequences are iterables, but not all iterables are sequences
#  (sets and dictionaries are iterables, but not sequences)

