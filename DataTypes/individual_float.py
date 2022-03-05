import math

# Float -- Specifies data stored inside the memory location type decimal
# Float can be positive and Negative
# One way of creating float using dynamic memory allocation
a = 3.15     # Dynamic Memory allocation
print(a)    # 3.15
# In order to check the data type we make use of type() function
print(type(a))    # class 'float'
# Another way of creating float using flot constructor
b = float(3.142)
print(b)  # 3.142

# Default values for Float
# One way of creating a default values is by directly assigning 0.0 to variable
c = 0.0
print(c)    # 0.0
# Another way is to creating and assigning float constructor to a variable
d = float()
print(d)   # 0.0

# Operations on float
# Addition with float and float
a = 3.2
b = 4.5
print(a + b)    # 7.7
# Addition with float and int
c = 4
print(a + c)   # 7.2
# Subtraction with float and float
print(a - b)   # -1.2999999999998
# Subtraction with float and int
print(a - c)   # -0.7999999999998
# Multiplication with float and float
print(a * b)   # 14.4
# Multiplication with int and float
print(a * c)   # 12.8
# Division with float and float
print(a / b)  # 0.71111111111111
# Division with float and int
print(a / c)    # 0.8
# Floor division with float and float
print(a // b)   # 0.0
# Floor division with float and int
print(a // c)   # 0.0
# Modulus division with float and float
print(a % b)  # 3.2
# Modulus division with float and int
print(a % c)   #3.2
# DivMod with float and float
print(divmod(a, b))    # (0.0, 3.2)
# DivMod with int and float
print(divmod(a, c))    # (0.0, 3.2)
# abs absolute value negative to positive
print(abs(-3.152))    # 3.152
print(abs(3.152))     # 3.152
# round off -- rounds of the float value based on precision
print(round(3.15245))    # 3
print(round(3.152246, 3))   # 3.152
# math.trunc() removes the decimal part from floating point number
print(math.trunc(3.152224))     # 3



