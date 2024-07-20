# 2 methods of factorial no :

# Method 1

# number=int(input('Enter the number : '))
#
# fact=1
# for i in range(1,number+1):
#     fact=fact*i
# print(f"Factorial of {number} is {fact}")

# Method 2 using def
# def factorial(n):
#     fact = 1  # Set initial value of fact to 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact
#
# print(factorial(5))

# Method 3 using Recursion:

# Recursion
# Recursion is a programming technique where a function
# calls itself in order to solve a problem.

# Key Concepts
# 1. Base Case
# 2. Recursive Case

# Factorial

def factorial(n):
    #Base Case
    if n == 0 or n == 1:
        return 1
    #Recursive case
    else:
        return n * factorial(n - 1)


print(factorial(5))
