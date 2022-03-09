# To check that in a given string ending character is vowel or not
s = input("Enter the string:")
if s[-1].lower() in "aeiou":
    print("String ends with a vowel")
else:
    print("String doesnot ends with a vowel")
