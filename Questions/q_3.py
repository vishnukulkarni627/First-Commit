# Using loop   0 to 50 alternate numbers
# for i in range(0, 51, 2):
#     print(i, end=" ")

# Using function
# def alter_(n, i=0):
#     for i in range(i,n,2):
#         print(i,end=" ")
# alter_(51)

# Using recursion
def alter_rec(n,i=0):
    if i<=n:
        if n%2==0:
           print(i,end=" ")
            i+=1
            alter_rec(n,i)
alter_rec(51)

