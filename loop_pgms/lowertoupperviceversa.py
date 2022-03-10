s = "Today IS 10th my Day"
res = ""
for i in s:
    if "a" <= i <= "z":
        res = res+chr(ord(i)-32)
    elif "A" <= i <= "Z":
        res = res+chr(ord(i)+32)
    else:
        res+=i
print(res)