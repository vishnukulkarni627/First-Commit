# To check string if even length create dict with string as key and value as ascii
# if string length is odd add string as key and value as string length
s = input("Enter the string:")
d = {}
if len(s) % 2 == 0:
    d[s] = ord(s[0])
else:
    d[s] = len(s)
print(d)

