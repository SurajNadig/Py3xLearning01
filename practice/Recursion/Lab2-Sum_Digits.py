# # To find sum of given digits in normal method 1 for explanation
# n = 12345
# # % is Remainder and // is quotient
# r1 = n % 10  # 5
# q1 = n // 10  # 1234
# print(r1)
# print(q1)
#
# r2 = q1 % 10  # 4
# q2 = q1 // 10  # 123
# print(r2)
# print(q2)
#
# r3 = q2 % 10  # 3
# q3 = q2 // 10  # 12
# print(r3)
# print(q3)
#
# r4 = q3 % 10 # 2
# q4 = q3 // 10 #1
# print(r4)
# print(q4)
#
# r5=q4
# print(f"Total sum is : {r1 + r2 + r3 + r4 + r5}")

# Method 2 using while loop

# num=1234567
# sum_digits=0
# while num>0:
#     sum_digits+=num%10 #Extracting remainder
#     num=num//10 # Extracting quotient
# print(sum_digits)
#
# Method 2 using loop inside function
def total_no(num):
    sum_digits=0
    while num>0:
        sum_digits+=num%10
        num=num//10
    return sum_digits

print(total_no(12345))
print(total_no(4649372553))

