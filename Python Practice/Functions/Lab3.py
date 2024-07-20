# def say_hello(name="Pramod"):
#     print("Hello", name)
#
#
# say_hello()
# say_hello(name="Rajani")
# say_hello("Indu")
# -------------------------------------------

def add(a, b, c):
    print("Value of a & b & c is : ", a, b, c)
    return a + b + c
    # print("Hi") #It wont run bcz print after return  on same function will not work


print("Hi")

# print(add(7,5,2)) #This also will work

res = add(7, 45, 78)  # This also will work
print(res)
# -------------------------------------------