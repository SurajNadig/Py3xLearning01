#Doubling the element in list :

list1=[1,2,3,4,5]

temp_list=[] #Creating the temporary List to store the doubled values
for i in list1:
    temp=i*2
    temp_list.append(temp)
print(temp_list)

# ------------------------------------------------------

# Doubling the items using MAP function :
# Map() :
# 1. Takes Each item from the list
# 2. execute the function on it.
# 3. Return same number of elements ( list)
# def double_item(num):
#     return num*2 # Multiplying or doubling 2
#
# double_list=list(map(double_item,list1))
# print(double_list)

# def double_item1(num1):
#     return num1+2 # Adding 2
#
# double_list1=list(map(double_item1,list1))
# print(double_list1)