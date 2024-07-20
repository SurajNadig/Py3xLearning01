
try:
    with open('Suraj.txt','r')as file:
        print(file.read())
except FileNotFoundError as ff:
    print("I am not able to find the file, please check again..")
finally:
    print(" Im closing the file")
    file.close() #Close has to be executed

# file can be assigned like below

# try:
#     file= open('Suraj.txt','r')
#     print(file.read())
# except FileNotFoundError as ff:
#     print("I am not able to find the file, please check again..")
# finally:
#     print(" Im closing the file")
#     file.close() #Close has to be executed
#-----------------------------To corrrect the error- We need to import and do -------------------------
# import os.path
#
# try:
#     file = open('example.txt', 'r')
#     print(file.read())
# except FileNotFoundError as fnfe:
#     print("I am not able to find the file, Please check Path")
# finally:
#     print("Executed")
#     try:
#         file.close()  # Close has to be executed
#     except NameError as ne:
#         print(ne)