#!/usr/bin/env python3

# Henri Medeiros Dos Reis
#2/2/2023

# 4 - Digit factorials

# Let's start by making a list of the factorials 
def factorial(n):
    "Returns the factorial of the input"

    ans = 1
    for i in range(1, n+1):
        ans = ans*i
    return ans

# Let's also have a helper function that finds the sum of the factorials
# of the digits 
def fact_sum(n, factorials):
    "Returns the sum of the factorial digits"
    my_sum = 0
    for digit in str(n):
        my_sum+=factorials[int(digit)]
    return my_sum

facts = [factorial(i) for i in range(10)]

# The answer is a sum of all the numbers that are equal to their fact_sum 
print(sum([i for i in range(3,10_000_000) if i == fact_sum(i,facts)]))

# 10,000,000 was a choice after trying many numbers and trying to find an 
# upper bound

