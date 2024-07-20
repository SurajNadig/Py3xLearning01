# An exception is an event
# that occurs during the execution of a program
# that disrupts the normal flow of instructions.
print("--------Start of program-------")
try:
    a=int(input("Enter num 1 : "))
    b=int(input("Enter num 2 : "))
    c=a/b

    print("Value of c is " , c)

except  Exception as n: # as n is not mandatory.
    print(n) # Its just printing what error is , without n also exception message will print
    print("Please enter Valid number")

print("--------End of program-------")

#------------------------Errors v/s Exceptions-------------------------------

# Erros are somehting, difficult to recover.
# Errors are more severe issues that typically
# prevent the program from running.
# impossible , Syntax, Identation


# Exceptions (error) -> can be handled.
# Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions
# Program recover can be possible

