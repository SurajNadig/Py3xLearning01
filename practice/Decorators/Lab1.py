# Decorators
# What is a Decorator?
# A decorator is essentially a function that takes another function as an argument
# returns a new function that usually extends the behavior

def my_decorator(func):
    def my_wrapper():
        print("******Starting******")
        func()
        print("******Ending******")
        print("               ")
    return my_wrapper()

@my_decorator
def Hello(): #No need to call the fucntion because @mydecorator itself call the function
    print("Hi , How are you doing ?")  # We need to do decoration for this fucntion, so will create a other fucntion

@my_decorator
def rcb(): #No need to call the fucntion because @mydecorator itself call the function
    print("RCB")
