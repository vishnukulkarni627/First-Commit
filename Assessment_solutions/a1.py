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
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
d = {}
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
# numbers = [10, 20, 30, 40, 50]
# for _ in range(len(numbers-1)):
#     for i in range(len(numbers-1)):
#         if numbers[i] > numbers[i+1]:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
# print(numbers[2])

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
names2 = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
d1 = {}
for index, item in enumerate(names2):
    d1[item] =
print(d1)











