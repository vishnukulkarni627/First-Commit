# 1. Print numbers from 0 to 4 (upto 5 but not including 5)
# for i in range(0, 5):
#     print(i)
# 2. Print numbers from 0 to 4 (num starts from zero if start index is omitted)
# for i in range(0, 4):
#     print(i)
# 3. Print every alterante numbers starting zero to Ten
# for i in range(0,11,2):
#     print(i)
# 4. Print number from 10 to 1
# for i in range(10, 0, -1):
#     print(i)
# 5. Print number form 10 to 0
# for i in range(10, -1, -1):
#     print(i)
# 6. Print alternate numbers from 10 to 0.
# for i in range(10, -1, -2):
#     print(i)
# 7. Print "Python is awesome!!" 5 times
# for i in range(0,5):
#     print("Python is awesome")
# 8. Print numbers from -10 to -1
# for i in range(-10,0,1):
#     print(i)
# 9. Print numbers from 10 to -1
# for i in range(10, -2, -1):
#     print(i)
# 10. Print even numbers
# for i in range(0,101):
#     if i%2==0:
#         print(i)
# 11. Print odd  numbers
# for i in range(0,101):
#     if i%2==1:
#         print(i)
# ****************************** Strings *****************************
# 1. Iterate over string using range function. s = ""hello world"""
# s = 'hello world'
# for i in range(len(s)):
#     print(s[i], end=" ")
# 2. Iterate over a string in reversed direction
# s = 'hello world'
# res = ""
# for i in range(len(s)):
#     res = s[i] + res
# print(res)
# 3. Print Index and Character using range function
# s = 'hello world'
# for i in range(len(s)):
#     print(i, s[i])
# 4. Iterate over multiple string objects simultaneously
# 5. Print alternate characters of the string
# s = 'hello world'
# res = s[::2]
# print(res)
# 6. Program to count the number of digits and alphabets in the string "hai 1234 python23"
# s = "hai 1234 python23"
# count = 0
# for i in s:
#     if i.isalpha():
#         count += 1
#     elif i.isdigit():
#         count += 1
# print(count)
# 7. Program to count the number of capital and small letters in the string "HelLo WORld"
# s = "HelLo WORld"
# cap_count = 0
# small_count = 0
# for i in s:
#     if i.isupper():
#         cap_count += 1
#     elif i.islower():
#         small_count += 1
# print("capital count:" , cap_count)
# print("small count:", small_count)
# ****************************** Lists *****************************
# 1. Print the item and its corresponding index in the list
# l = ['apple', 'google', 'banana', 'kiwi']
# for index, item in enumerate(l):
#     print(item, index)
# 2. Printing alternate items of the list
# l = ['apple', 'google', 'banana', 'kiwi', 'grapes', 'dragonfruit']
# res = l[::2]
# print(res)
# 3. Iterate over multiple lists simultaneously

# 4. Iterate through multiple list with un-equal lengths using zip function

# 5. Program to print filenames ending with pdf.
# files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']
# for i in files:
#     if i.endswith('f'):
#         print(i.rstrip(".pdf"))
# 6. Print the extension of each file name in the list
# files = ['youtube.txt', 'yahoo.pdf', 'microsoft.doc', 'apple.xls', 'amazon.xml']
# l = []
# for i in files:
#     res = i.split(".")[1]
#     l.append(res)
# print(l)
# 7. Program to print the length of each word in the list
# l = ['apple', 'google', 'banana', 'kiwi', 'grapes', 'dragonfruit']
# l1 = []
# for i in l:
#     res =([i, len(i)])
#     l1.append(res)
# print(l1)

# ****************************** Dictionary *****************************
# 1. Print only key's of the dictionary
# d = {"a":1213, "b": 4678, "c": 98745}
# for key,value in d.items():
#     print(key)
# 2. Print Values of the dictionary
# d = {"a":1213, "b": 4678, "c": 98745}
# for key, value in d.items():
#     print(value)
# 3. Print index and item of the dictionary
# d = {"a":1213, "b": 4678, "c": 98745}
# for index,item in enumerate(d):
#     print(index, item)
# 4. Count number of words in a sentence using get method
# sentence = 'hello world hello world welcome to python'
# d ={}
# words = sentence.split()
# for word in words:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)
# 5. Counting number of characters in a string
# s = 'abracadabraca'
# count = 0
# for i in s:
#     count+=1
# print(count)
# 6. Counting number of vowels in a string
# s = 'vishnukulkarni'
# for i in s:
#     if i in "aeiouAEIOU":
#         print(i)
# 7. Counting occurrences of word in the string
# sentence = "hello world welcome to python hello hi hello hello"
# d ={}
# words = sentence.split()
# for word in words:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)
# 9. Create a dictionary for the below list
cities = [('India', 'Bangalore'),
          ('India', 'Chennai'),
          ('India', 'Delhi'),
          ('India', 'Kolkata'),
          ('USA', 'Dallas'),
          ('USA', 'New York'),
          ('USA', 'Chicago'),
          ('China', 'Beijing'),
          ('China', 'Shainghai')
          ]
d={}
# 10. Adding items of two lists corresponding to their indices
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c =[]
for a, b in zip(a,b):
    c.append(a + b)
print(c)


