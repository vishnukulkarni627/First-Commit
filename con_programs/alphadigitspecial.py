# To check whether character is alphabet,digit,specialcharacter
a = input("Enter the character:")
if "a" <= a <= "z" or "A" <= a <= "Z":
    print("Character is an alphabet")
elif "0" <= a <= "9":
    print("character is a number")
else:
    print("Character is a special character")