s = input("Enter the character:")
if "a" <= s <= "z":
    upp = chr(ord(s) -32)
    print(upp)
elif "A" <= s <= "Z":
    low = chr(ord(s) +32)
    print(low)
else:
    print("not a alphabet")
