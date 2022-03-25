import os
print(os.getcwd())
path = r"C:\Users\VISHNU\PycharmProjects\First-Commit\files"
os.chdir(path)
print(os.getcwd())

# Steps to perform read operations ---- Here we are having three methods
#  1. read Method -- By default mode will be in read mode
# with open("sample.txt") as file:
        # print(file.read())     # Reads entire data from sample.txt as a single string
#  Here in this method we can specify how many characters we can read...
#     print(file.read(5))     # hello
#     print(file.read(6))     # Continous from after hello --- hello
#  2. readline method -- Reads the single line
#       print(file.readline())
#  3.  readlines Method -- reads the entire text in form of list
#     print(file.readlines())
#     print(file.read())
#     print(file.tell())
#     print(file.seek(0))
#     print(file.tell())

 # write(), writelines()
with open("example.txt", "a") as file:
    print(file.write("Today is Monday\n"))
    print(file.write("Tomorrow is Tuesday"))
    print(file.writelines(["Today is Monday\n", "Tomorrow is Tuesday\n"]))