d={"Bangalore":"Traffic", "Mysore":"palace","Dharwad":"peda"}
res = sorted(d.items(),key=lambda items : items[1][0])
print(dict(res))