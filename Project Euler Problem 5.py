# Valerie Walsh 2018.02.25

# Topic 4: Lists 
# Write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.
# I found this extremely difficult and got to the stage where I had the below layout apart from the correct formulas and also the 'break'
# Referenced student work for clarification, found online solutions too complex - https://github.com/Sarahkel/Python-Problem-Sets/blob/master/Euler5.py

# Reference: Euler Problem 5 https://projecteuler.net/problem=5

i = 2520
n = 1

while n != 2:
    if (i%11 + i%12 + i%13 + i%14 + i%15 + i%16 + i%17 + i%18 + i%19 + i%20 ==0):
        print (i)
        break
    else:
        i = i + 2520
