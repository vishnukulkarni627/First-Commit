# # Strings
# # String is a immutable data type
# # Immutable: Once declared cannot be modified in origin, takes a copy and modification can be done
# # Creating a String
# #  #1 String using single quotes
# a = 'hello world'
# print(a)
# #  #2 String using double quotes
# b = "hello world"
# print(b)
# #  #3 String using triple single quotes
# c = '''hello world'''
# print(c)
# #  #4 String using triple double quotes
# d = """hello world"""
# print(d)
#
#
# # Another ways to create a string
# # one way
# e = str('hello world')
# print(e)
# # Creating a empty string
# f = str()
# print(f)
# g = ""
# print(g)
#
#
#
# # Regular String: Here in the below string \n -- takes new line and \t -- takes a single tabspace ,
# # In order to overcome Regular String problem,we go for raw string
# h ="vishnu\n kulkarn\ti"
# print(h)    #vishnu
#              # kulkarn	i
# # Raw String one way
# # Before the string we have to insert 'r' literal so that \n ,\t will be printed as it is..
# i = r"vishnu\n kulkarn\ti"
# print(i)    # vishnu\n kulkarn\ti
# # Another way to avoid '\n','\t' is to put backslash against it
# j = "vishnu\\n kulkarn\\ti"
# print(j)    # vishnu\n kulkarn\ti
#
# print(id(a))    # Memory Adress of the string 'a'
#
# # Indexing a String
# # Process of extracting single character at a time
# # It can be done via Positive begins with 0 and Negative begins with -1
# k = "vishnu kulkarni"
# print(k[4])     # n
# print(k[-4])    # a
#
# # Slicing a String
# # Process of extracting the multiple characters at a time / Simultaneously
# # var: variable Name[start index: end index : step value]
# # start index: positive or negative index
# # end index: positive or negative index (index+1)
# # step value: positive or negative value to fetch alternative characters
# # Extracting string from a given string
# l = "python selenium"
# print(l[0:6:1])         # python -- extracting by positive type
# print(l[-16:-9:1])      # python-- extracting by negative type
# # For below string extract first two characters
# l1 = "python is a easy language to learn"
# print(l1[0:2:1])    # py
# # For above string extract last character from each word
# l2 = l1.split(" ")
# print(l2)   #['python', 'is', 'a', 'easy', 'language', 'to', 'learn']
# # For l1 string extract last two characters
# print(l1[-1:-3:-1])   # nr
# # For l1 string extract them in reverse format # Using negative indexing
# print(l1[-1:-36:-1])    # Using negative indexing   # nrael ot egaugnal ysae a si nohtyp
# # For l1 string extract them in reverse format  #Using positive indexing
# print(l1[35:0:1])       # Using positive indexing    # nrael ot egaugnal ysae a si nohtyp
# # For l1 string extract characters in forward way with respect to alternate characters.
# print(l1[0:35:2])       # Using positive indexing  # Alternate character extracting # pto saes agaet er
# # For l1 string extract characters in Negative way with respect to alternate characters.
# print(l1[-36:-1:2])     # pto saes agaet er
#
# # Formatting string literals
# # Here we gonna place outside variable directly inside string instead of passing the arguments
# a = 24
# b = "day"
# # Here what happens means direct statement prints
# message = "There are {a} hours in a {b}"
# print(message)  # There are {a} hours in a {b}
# # If we add 'f' prefix then a and b value get update inside the given string
# message1 = f"There are {a} hours in a {b}"
# print(message1)     # There are 24 hours in a day
#
# # String Methods
# #  First Method --- lower()
# first = "VISHNU KULKARNI"
# print(first.lower())    # vishnu kulkarni  # Here new object will be created
# print(first)       # VISHNU KULKARNI # Prints in upper case because ,
# # string is immutable it cant modify the original variable value
# # Second Method --- upper()
# second = "vishnu kulkarni"
# print(second.upper())   # VISHNU KULKARNI # Here new object will be created
# print(second)   #vishnu kulkarni # prints in lower case because,
# # string is immutable it cant modify the original variable value
# #  Third Method --- count()  Here returns the number of occurances of a substring in original string
# third = "Welcome to my world Welcome to my python"
# print(third.count("Welcome"))   # 2 # In above statement Welcome word is repeated twice ,
# # hence count is returning value 2
# #  Fourth Method --- find() and rfind()  # Searches string for specified value
# #  returns the position where it has found
# # Find Method --- Finds first occurance of the specified value
# # If given value is not found, result will be -1
# fourth = "I love python"
# print(fourth.find('l'))    # 2  # Result will be 2 because position of l is 2 in original string
# print(fourth.find('ove'))    # 3  # Result will be 3 because position of o and first occurance  is 3 in original string
# print(fourth.find('w'))    # -1  # Result will be -1 because position of w is not there hence  -1 in original string
# # rfind() --- searches string for specified value return the last position where it was found
# print(fourth.rfind('on'))  # 11 # Result will be 11 because position of o is 11 in original string last occurance
# #  index() and rindex() -- Searches the string for specified value returns position where it was found
# print(fourth.index('l'))    # 2  # Result will be 2 because position of l is 2 in original string
# print(fourth.index('ove'))    # 3  # Result will be 3 because position of o and first occurance  is 3 in original string
# # print(fourth.index('w'))    # -1  # Result will be -1 because position of w is not there hence  -1 in original string
# #  r index --- searches string for a specified value returns position where it was found
# # print(fourth.rindex('w'))   #Returns value error...
# print(fourth.rindex('o'))   # 11 will return
# #  Fifth Method --- replace() --- replaces specified value with another specified phrase
# fifth = 'simplish'
# print(fifth.replace("simp", "eng"))   # english will be replaced...
# # Sixth Method---Starts with() --- returns true if string starts with specified value..
# sixth = 'vishnu kulkarni'
# print(sixth.startswith('vishnu'))    # True because vishnu is the starting word
# print(sixth.startswith('kulkarni'))  # False because kulkarni is succesive word...hence false
# # Seventh Method --- Enda with() --- returns false if string ends with specified value
# seventh = 'vishnu jssate'
# print(seventh.endswith('jssate'))    # True because vishnu is the starting word
# print(seventh.endswith('vishnu'))    # False because kulkarni is succesive word...hence false
# # Eighth Method --- spilt() --- string specified separator and returns list
# eighth = 'vishnu loves python very much'
# print(eighth.split(" "))    # ['vishnu', 'loves', 'python', 'very', 'much']
# print(eighth.split('h'))    # ['vis', 'nu loves pyt', 'on very muc', '']
# #  rspilt() --- spilts from right side of the string
# print(eighth.rsplit('y'))   # ['vishnu loves p', 'thon ver', ' much']
# #  where in spilt function will take input as string and output will be in form of list
# # Ninth Method ---Joins--- joins the element of an iterable using the string specified
# # First is:
# ninth = "vishnu"
# print("-".join(ninth))
# # Tenth Method is Strip() --- removes the leading (Beginning spaces) and tailing(End spaces) characters
# # Note: Space is the default leading character to remove
# tenth = "----------vishnu----------"
# print(tenth.strip("-"))
# # lstrip()---- strips left side of the string
# print(tenth.lstrip("-"))
# # rstrip()----- strips right side of the string
# print(tenth.rstrip("-"))
# # isalnum() ---
# string_ = "hellohai123"
# print(string_.isalnum())
# # isalpha()
# string__ = "hellohai"
# print(string__.isalpha())
# # isdigit()
# string_num = "9916956137"
# print(string_num.isdigit())
# # isnumeric()
# string__numeric = "123456"
# print(string__numeric.isnumeric())
# # islower()
# string__low = "vishnu"
# print(string__low.islower())
# # isupper()
# string__upper = "VISHNU"
# print(string__upper.isupper())

# Iterating through a string using range and length functions(i.e In Built functions)
# w = 'welcome to my world'
# t = len(w)
# # print(t)
# for i in range(t):
#     print(w[i], end="")
# print("")
#
# # Iterating through a string using range and length functions reverse(i.e In Built functions)
# for i in range(t-1, -1, -1):
#     print(w[i], end="")
#
# print("")
#
# # Iterating through a string directly without using length and range function
# for i in w:
#     print(i, end="")
# print("")

# Converting a string to lower without using inbuilt function
# w1 = "WELCOME TO MY WORLD"
# for i in w1:
#         low_ = chr(ord(i)+32)
#         low1_=low_.replace('@', " ")
#         print(low1_, end="")

# String to extract vowels in a given string
w1 = "vishnu kulkarni"
i = 0
while i< len(w1):
        if w1[i] in "aeiou":
                print(w1[i],end="")
        i+=1

