s = "My birth date is 14-12-2000"
i = 0
sum = 0
while i < len(s):
	if "0" <= s[i] <= "9":
		sum = sum+int(s[i])
	i+=1
print(sum)	