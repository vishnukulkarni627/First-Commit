# To check string is vowel if it is vowel create dict with key as string and value as string length
s = input("Enter the string:")
d = {}
if s[0] in "aeiouAEIOU":
    d[s] = len(s)
print(d)
