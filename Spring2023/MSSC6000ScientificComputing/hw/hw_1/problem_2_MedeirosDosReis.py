#!/usr/bin/env python3

# Henri Medeiros Dos Reis
#2/2/2023

# 2 - Longest Collatz sequence

# First, lets start by defining the Collatz sequence count for a given number
def col_count(n):
    "Returns the number of chains involved in the Collatz sequence starting at that number"

    count = 1 # should start at 1, since it always have the starting num
    while n != 1: # Keep going until it reaches 1, which should always be the last num
        if n % 2 == 0:
            n = n // 2 # use // to keep the divison as integers 
        else:
            n = 3 * n + 1
        count += 1
    return count

# Then, we can find the largest one

prev_ans = 0
ans = 0
for i in range(1, 1_000_000): 
    my_count= col_count(i) # Use the helper function
    if my_count > prev_ans: # If the new is bigger, replace the count and save the ans
        prev_ans = my_count
        ans = i
print(ans)
