s = "hello world hello world hi"
s1 = ""
for i in s:
    if s.count(i)>1:
        print(i, end="")
