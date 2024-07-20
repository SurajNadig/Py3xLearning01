# Sum of digits using recursive function
def sum_digit(n):
    #Base case
    while n<10:
        return n
    #Recusrsive case
    else:
        return n%10+sum_digit(n//10)

print(sum_digit(1234))