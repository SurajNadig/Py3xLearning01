#File I/O
#Opening the file

with open('Suraj.txt','r') as file: # r is reading mode
    print(file.read())
    file.close() #Always close the file after opening. Bcz it will be stored in python memory if we dont close it.