#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 09/06/2023

# Assign#1 comparing prefix averages time complexity

import random
import time

class PrefixAverage:
    """
    Class that contains two implementations of prefix average
    """

    def prefixAverage1(self, x):
        """
        Calculates prefix average of a list x. With time complexity O(n^2)
        """
        
        n = len(x)
        a = [0] * n
        
        for j in range(n):
            total = 0
            for i in range(j+1):
                total += x[i]
            a[j] = total / (j+1)
            
        return a
    
    def prefixAverage2(self, x):
        """
        Calculates prefix average of a list x. With time complexity O(n)
        """
        
        n = len(x) 
        a = [0] * n
        total = 0
        for j in range(n):
            total += x[j]
            a[j] = total / (j+1)
            
        return a


# Time the methods
test = PrefixAverage()

n_values = [10000,15000,20000,25000,30000,35000,40000]
for n in n_values:
    x = [random.randint(0,n) for i in range(n)]

    print("n = ", n)
    start = time.time()
    a1 = test.prefixAverage1(x)
    end = time.time()
    print(f"Method 1 time:{end-start:.8f} seconds")

    start = time.time() 
    a2 = test.prefixAverage2(x)
    end = time.time()
    print(f"Method 2 time:{end-start:.8f} seconds")