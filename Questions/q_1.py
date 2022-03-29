# Using Loop 0 t0 4 printing
# for i in range(5):
#     print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
    # print(i, end=" ")  #  0 1 2 3 4

# Using functions  #Printing using functions from 0 to 4
# def ztof(n):
#     for i in range(n):
#         print(i)
# ztof(5)

# Using recursion
def ztofrec(n, i=0):
    if i <= n:
        print(i)
        i += 1
        ztofrec(n, i)
    else:
        return
ztofrec(4)
