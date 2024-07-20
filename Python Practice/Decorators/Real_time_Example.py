# To print the logs of the time taken :
import time


def time_taken(func):
    def my_wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time taken is ", end_time - start_time)

    return my_wrapper() # If u r not using () in return time , call the function that is logs()

@time_taken
def logs():
    time.sleep(4)
    print("Print logs of time taken : ")

@time_taken
def report():
    time.sleep(6)
    print("Print Report of time : ")