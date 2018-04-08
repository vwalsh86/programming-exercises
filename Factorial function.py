# Valerie Walsh 13-03-2018
# Topic 6: Functions 
# Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial. You should, in your script, test the function by calling it with the values 5, 7, and 10.


# Resource: https://stackoverflow.com/questions/5136447/function-for-factorial-in-python

def factorial(i):
    num = 1
    while i >= 1:
        num = num * i
        i = i - 1
    return num


print("The factorial of 5 is", factorial(5))
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10), "\n")


# I thought the above could be condensed further into a shorter fuction and continued to research, I discovered this method
# Resource: https://www.quora.com/How-would-you-define-a-factorial-function-in-Python

def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)

        
print("The factorial of 5 is", factorial(5))
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10))
