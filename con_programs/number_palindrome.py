# To check that number is a palindrome or not
a = input("Enter the number:")
if str(a)[::-1] == str(a):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")