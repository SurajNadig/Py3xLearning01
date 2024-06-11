# PROGRAM TO COMPARE 2 NUMBERS AND PRINT THE GREATER NUMBER

a = int(input("Enter first no : "))
b = int(input("Enter second no : "))

# print(a, "is greater") if (a > b) else print(b, "is greater")

print(a, "is greater") if (a > b) else print(b, "is greater") if (b > a) else print("Both are equal")
