# Integers : Specifies data stored inside the memory location to be a integer...
# Integers can be positive or negative
# one way of creating integer type of data
a = 10   # Dynamic Memory Allocation
print(a)    # 10
# In order to check the data type, we make use of type() function
print(type(a))    # type of : class 'int'
# Another way of creating integer using int constructor
b = int(15)  # Constructor using explicitly
print(b)    # 15

# Default value for Integer
# way one
c = 0    # Directly Assigning 0 value to the varaible
print(c)    # 0
# way two
d = int()  # Creating and assigning empty int constructor into variable
print(d)    # 0

# Operations on Integer Data type
# Addition
a = 6
b = 5
print(a + b)   # 11
# Subtraction
print(a - b)   # 1
# Multiplication
print(a * b)   #30
# Division
print(a / b)   # 1.2 results in float number
# Floor Division
print(a // b)  # 1 results w.r.t to quotient returns in whole number decimal will be nullified
# Exponent
print(a ** b)  # 7776 ** represents 6^(power)5=7776
# Modulus
print(a % b)  # 1 results will be w.r.t to remainder
# Div mod
print(divmod(a, b))   # (1, 1) represents div and mod
# abs absolute values converts negative value into positive value
print(abs(-5))    # 5
print(abs(5))    # 5








