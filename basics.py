#  How to check it is identifier or not
"vishnu".isidentifier()  # True
"True".isidentifier()  # True
# How to check it is keyword or not
import keyword
print(keyword.iskeyword("vishnu"))  # False
print(keyword.iskeyword("True"))   # True
# Variable Declaration
a = 10
print(a)   # 10
x = a
x = 10
print(x)   # 10
# id function used to fetch memory address
# Note: If we are having two references(variable= a,x) ,
# but object is same (values=10) then we get memory address as same...
# Similarly if we are having different values we get different memory address.
print(id(a)) # 2267567358480
print(id(x)) # 2267567358480

# print function prints the value of the passed variable reference, it has end and sep parameteres!!
a = "hai"
b = "hello"
print(a, b)  # hai hello
# Modifying end parameter in print function, By default value will be "\n"(newline).
print(a, end=" ")  # hai hello
print(b)
# Modifying sep parameter in print function, By default value will be whiteSpace!!!
print(a, b, sep="%%%")  # hai%%%hello
# Reads the string from entered input
print(input("Enter a positive number between 1 to 10 : ")) # input 5 # output 5

# Activity 1

v = "vishnu"
w = 15
print("My name is", v)   # My name is vishnu
print("I am", w, "years old")   # I am 15 years old

# Activity 2
print("My name is", v, end=" ", sep="$$")
print("I am", w, "years old", sep="$$")
# Output: My name is$$vishnu I am$$15$$years old
