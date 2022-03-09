# TypeCasting for individual data types
# process where one data type is converted to another data type

# Integer to other data types
# Integer can be converted to Float,Complex Number,Boolean
x = 10
b = float(x)
print(b)   # 10.0
c = complex(x)
print(c)    # 10+0j
d = bool(x)
print(d)    # True

# Float to other data types
# Float can be converted into int, complex,Boolean
y = 3.142
e = int(y)
print(e)  # 3
f = complex(y)
print(f)   # 3.142+0j
g = bool(y)
print(g)    # True

# Complex number to other datatypes
# complex number can be converted into Boolean not to int and float it occurs Type Error
# z = 2 + 3j
# h = int(z)
# print(h)    # Typeerror
# i = float(z)
# print(i)  # Typeerror
# j = bool(z)
# print(j)    # True

# Boolean to other datatype
a = True
b = False
k = int(a)
l = int(b)
print(k)    # 1
print(l)    # 0
m = float(a)
print(m)    # 1.0
n = float(b)
print(n)    # 0.0
o = complex(a)
print(o)    # 1+ 0j
p = complex(b)
print(p)    # 0j

