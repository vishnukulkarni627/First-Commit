# complex numbers form a+bj a is real b is imaginary
# complex numbers can be positive and negative
# creating a complex number can be done in three ways
# One way is directly assigning complex number to a variable
a = 2+3j
print(a)  # (2+3j)
# Another way is by creating constructor and assigning complex number to a variable
b = complex(2+3j)
print(b)   # (2+3j)
# Another way is by creating constructor and assigning the values in the format (2.3)
c = complex(2, 3)
print(c)  # (2+3j)

# Default values
d = complex(0, 0)
print(d)     # 0j
e = 0 + 0j
print(e)    # 0j
f = complex()
print(f)   # 0j


# Operations on complex numbers
# Additon on complex with complex
a = 2 + 3j
b = 3 + 4j
print(a + b)    # 5 + 7j
# Addition on complex with int
c = 4
print(a + c)    # 6 + 3j
# Addition on complex with float
d = 4.5
print(a + d)   # 6.5 + 3j
# Subtraction with complex and complex
print(a - b)   # -1-1j
# Subtraction with complex with int
print(a - c)   # -2+3j
# Subtraction with complex with float
print(a - d)   # -2.5+3j
# Multiplication with complex and complex
print(a * b)   # -6+17j
# Multiplication with complex and int
print(a * c)  # 8+12j
# Multiplication with complex and float
print(a * d)  # 9+13.5j
# Division with complex and complex
print(a / b)   # 0.72+0.04j
# Division with complex and int
print(a / c)   # 0.5+0.75j
# Division with complex and float
print(a / d)   # 0.4444444444444+0.666666666666j



