#!/usr/bin/env python3

# Henri Medeiros Dos Reis
#2/2/2023

# 1 - Largest Palindrome problem

# Idea 1
#ans = 0
#for i in range(100,1000): # Loop through all 3 digits numbers twice
#    for j in range(100,1000):
#        prod = i * j
#        # If the number reads the same backwards and is bigger than the last ans
#        if(str(prod) == str(prod)[::-1] and prod > ans): 
#            ans = prod # This is my new ans
#print(ans)

# Idea 2
print(max(i * j for i in range(100, 1000) for j in range(100, 1000) if str(i * j) == str(i * j)[::-1]))


