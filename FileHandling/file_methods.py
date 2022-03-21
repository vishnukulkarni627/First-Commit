# popen(file_name, mode): provides a gateway and accesses the file directly
import os

# path = r"C:\Users\VISHNU\PycharmProjects\First-Commit\files\sample.txt"
# os.popen(path)

# Opening the files can be done in two ways
# 1. Without using Context Manager : Here once we open the file we have to close the file manually
# file = open(path)
# print(file.closed)    #False
# file.close()
# print(file.closed)    #True
# 2. With using context Manager : Here no need to close manually closes automatically
path1 = r"C:\Users\VISHNU\PycharmProjects\First-Commit\files"
os.chdir(path1)
print(os.getcwd())

# with open("sample.txt") as file:
    # print(file)   # Prints name,mode,encoding all information-- Returns Object Address
    # print(file.name)   # Prints only the name of the file
    # print(file.mode)   # Prints only the mode of the file
    # print(file.readable())  # True
    # print(file.writable())  # False
# print(file.closed)  # True

###################################################################################################
#  Mode as "Write"
# with open("sample.txt", "w") as file:
#     print(file)   #Returns address
#     print(file.readable())      # Returns False
#     print(file.writable())      # Returns True
#  Mode as "Read"
# with open("sample.txt", "r") as file:
#     print(file) #Returns address
#     print(file.writable())  # Returns False
#     print(file.readable())  # Returns True
# #  Mode as "Append"
# with open ("sample.txt", "a") as file:
#     print(file) #Returns address
#     print(file.writable())      # Returns True
#     print(file.readable())      # Returns False
#  In order to remove the file: os.remove(file_name)  --- Existing sample.txt
# os.remove("sample.txt")
#  Mode as "Create"
with open("sample.txt", "x") as file:
    print(file)
    print(file.writable())  # Returns True
    print(file.readable())  # Returns False



