
# Use of OS modules are if want to read a file, first we need to check tht file exist are not .
# In API or Selenium automation, we may need to check file exists and sometimes we may also need to remove some files

import os

size=os.path.getsize('TestData')
print(size)

if size!=0:
    print("File exists and has some content")
else:
    print("File don't exists")

mtime=os.path.getmtime('TestData')
print("Modification time is " , mtime) #Time will come in UTC Unicode time , EPCHO time