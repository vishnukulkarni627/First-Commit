from collections import defaultdict
# Create a dictionary with character and its count pair from the given string
# s = "hello world"
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = s.count(i)
# print(d)
#  Create a dictionary with word and its length pair from the given string
# s1 = "today is wednesday so programming is very much interesting"
# d = {}
# res = s1.split()
# # print(res)
# for i in res:
#     if i not in d:
#         d[i] = len(i)
# print(d)
# Create a dictionary with word and count pair from the given list
# l1 = ['this', 'python', 'is', 'lovely', 'programming', 'language', 'python', 'is', 'fun']
# d = {}
# for i in l1:
#     if i not in d:
#         d[i] = l1.count(i)
# print(d)
# Create a dictionary with word and length pair from the given list
# l1 = ['this', 'python', 'is', 'lovely', 'programming', 'language', 'python', 'is', 'fun']
# d = {}
# for i in l1:
#     if i not in d:
#         d[i] = len(i)
# print(d)


# WaP to print nth fibonacci numbers
# n = 10
# a = 0
# b = 1
# for i in range(n-1):
#     c = a + b
#     a = b
#     b = c
# print(c)

# wap to count the alphabets and digits in a given string with using inbuilt method
# s = 'hello@world!welcome!!!python$hihowareyou&whereareyou?'
# count = 0
# for i in s:
#     if i.isalpha():
#         count = count+1
#     elif i.isdigit():
#         count = count+1
#     else:
#         continue
# print(count)

# wap to count the alphabets and digits in a given string without using inbuilt method
# s = 'hello@world!welcome2022!!!python$hihowareyou&whereareyou?'
# count1 = 0
# for i in s:
#     if "a" <= i.lower() <= "z":
#         count1 += 1
#     elif "0" <= i <= "9":
#         count1 += 1
#     else:
#         continue
# print(count1)

# Write a pgm to iterate through list and
# build a new dictionary only if the items of the list has even numbers of characters
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {}
# for i in names:
#     if i not in d:
#         if len(i)%2 == 0:
#             d[i] = len(i)
# print(d)

# Write a pgm to iterate through list and
# build a new dictionary only if the items of the list has odd numbers of characters
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# d = {}
# for i in names:
#     if i not in d:
#         if len(i)%2 == 1:
#             d[i] = len(i)
# print(d)

# for i in range(len(names)):
#     if i not in d:
#         if len(names[i]) % 2 == 1:
#             d[names[i]] = len(names[i])
# print(d)

# wap to find the third largest number in list
# num = [10, 20, 50, 30, 40, 45]
#
# for _ in range(len(num)-1):
#     for i in range(len(num)-1):
#         if num[i] > num[i+1]:
#             num[i], num[i+1] = num[i+1], num[i]
# print(num[-3])

# wap to print all numeric values in a list
# items = ['apple', 1.2, 'google', 12.6, 26, 100]
# l = []
# for i in items:
#     if isinstance(i, (int, float)):
#        l.append(i)
# print(l)

# wap to create a dictionary of element and element to the power of its index pair
# a = [1, 2, 3, 4, 5]
# d = {}
# for index, item in enumerate(a):
#     d[item] = item**index
# print(d)

# wap to create a dictionary item and no of occurances of each item in list without in built
names1 = ['apple', 'google', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# d = {}
# for i in names1:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

# dd = defaultdict(int)
# for i in names1:
#     dd[i] += 1
# print(dd)

# wap program to get index of each item
# names2 = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# d1 = {}
# for index, item in enumerate(names2):
#         if item not in d1:
#             d1[item] = [index]
#         else:
#             d1[item] += [index]
# print(d1)
# wap to group files with same extensions
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt']
# d = {}
# for i in files:
#     file, ext = i.split(".")
#     if ext not in d:
#         d[ext] = [file]
#     else:
#         d[ext] += [file]
# print(d)
# write a function to create a dictionary of word and its count pair in given string
# s = 'It is a very good book and reading book is a good habit'
# d = {}
# def func_(string_):
#     words = string_.split()
#     for word in words:
#         if word not in d:
#             d[word] = string_.count(word)
#     return d
# print(func_(s))

# write a function to count the number of elements present in the list without using in built in function
# a = ['hai', 'guys', 'welcome', 'to', 'my', 'channel']
#
# def func_(list_):
#     count = 0
#     for items in list_:
#         count += 1
#     return count
# print(func_(a))

# write a function to return the words starting with vowels
# b = "please like, share and subscribe"
# def func_(string_):
#     l =[]
#     for i in string_.split():
#         if i[0] in "aeiouAEIOU":
#             l.append(i)
#     return l
# print(func_(b))

# write a function to check if the given number is prime or not num = 12
# def prime_(num):
#     for i in range(2, num):
#         if num % i == 0:
#             print("Number is not a prime")
#             break
#     else:
#         print("Number is a prime")
# prime_(12)

# write a function to return nth fibonacci number, n=10
# def fib_(n, a = 0, b = 1):
#     for i in range(n):
#         c = a + b
#         a = b
#         b = c
#     print(a)
# fib_(10)

# write a function to reverse a string without using inbuilt functions
# s = "vishnu"
# def rev(string_):
#     res = ""
#     for i in string_:
#         res = i+res
#     return res
# print(rev(s))

# write a function to return a prime number present after the given number
# if the given no is prime then return the same ,num =12
# def prime_after(num):
#     while num > 1:
#         for i in range (2, num):
#             if num % i == 0:
#                 num +=1
#                 break
#         else:
#             return num
# print(prime_after(24))

# write a function to return a string by converting uppercase to lower case and vice versa
# without using in built functions
# s = "Don't forget to press the bell icon:)"
# def func_(string_):
#     for i in string_:
#         if "a" <= i <= "z":
#            up_=chr(ord(i)-32)
#            print(up_,end="")
#         elif "A" <= i <= "Z":
#             low_ = chr(ord(i)+32)
#             print(low_,end="")
#         else:
#             continue
# func_(s)

# write a function to print the fibonacci series till the user given number
# def func_(num, a = 0, b =1 ):
#     while a <=num:
#         print(a)
#         c = a + b
#         a = b
#         b = c
#
# user_ = int(input("Enter the user number: "))
# func_(user_)

# write a list comprehension to create a list with the items of the list which has even number of characters
# names = ['apple', 'yahoo', 'gmail', 'walmart', 'flipkart', 'facebbook', 'amazon']
#  Normal code
# l =[]
# for i in names:
#     if len(i)%2 == 0:
#         l.append(i)
# print(l)
#  List comprehension
# l1 = [i for i in names if len(i)%2==0]
# print(l1)

# write a list comprehension to get only the duplicate elements in the list
names = ['apple', 'google', 'apple', 'yahoo', 'google']
# Normal code
count = 0
l1=[]
for i in names:
    if names.count(i)>1:
        count+=1
        l1.append(i)

print(l1)
