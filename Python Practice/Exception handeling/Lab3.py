# try, except and finally

try:
    num1 = int(input("Enter a Number 1\n"))
    num2 = int(input("Enter a Number 2\n"))
    result = num1/num2
except ValueError as ve:
    print("Value error is ",ve)
except ZeroDivisionError as zde:
    print("ZeroDivision error is ",zde)
else: # if code runs succesfully [Line no 4,5,6 ] without any exceptions , this part executes.
    print(f'Result is {result}')
finally: # Whatever happens in code , this finally will get executed
    print("I am finally and I will be executed anyhow!!")