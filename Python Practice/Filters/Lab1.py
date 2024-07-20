# Filter in Python
# The filter() function in Python is a built-in function
# Filters - function only return true or false
# allows you to filter elements in the list, tuple, set.

numbers=[10,25,30,45,50,65,70,85,90,105]
#To extract even or odd , usually we can use for loop as below

# even_num=[]
# for i in numbers:
#     if i%2==0:
#         even_num.append(i)
# print(f"Even nos are :  {even_num}")
#
# odd_num=[]
# for i in numbers:
#     if i%2!=0:
#         odd_num.append(i)
# print(f"Even nos are :  {odd_num}")

#It can be extracted using filter function also like below

def even_num(num):
    return num%2==0

new_even_num=filter(even_num,numbers)
print(list(new_even_num))

def odd_num(num):
    return num%2!=0

new_odd_num=filter(odd_num,numbers)
print(list(new_odd_num))

