# To check that a given string is palindrome or not
s = input("Enter a string:")
if s[::-1] == s:
    print("String is a palindrome")
else:
    print("String is not a palindrome")