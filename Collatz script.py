# Valerie Walsh 10-02-2018
# Topic 3: Conditions, loops and flow control 
# Write a single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement.
# Exercise - Create a Collatz script

# Reference: https://gist.github.com/ecaldwell/5274266
# Reference: https://www.webucator.com/blog/2015/07/collatz-conjecture-in-python/

n = int(input("Please enter an integer:"))
while n > 1:
    if n %2 == 0:
        n = n/2
        print (n)
    else: 
        n = (n*3) + 1
        print (n)
