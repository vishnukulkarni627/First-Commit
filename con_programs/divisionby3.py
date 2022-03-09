# To check first digit of a number is divisible by 3 or not
s = input("Enter a number")
if int(str(s[0])) % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")