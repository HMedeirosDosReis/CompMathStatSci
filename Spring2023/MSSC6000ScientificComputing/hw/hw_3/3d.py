#!/usr/bin/env python3


import random 
import math 
def find_max(elements):
    """
    Takes in a list of elements and returns the maximum value in that list 
    """
    elements = list(elements)
    mid_point = math.ceil(len(elements)/2)

    max_val = elements[0]   # assume the first element is the max initially
    for element in elements:
        mid_point = math.ceil(len(elements)/2)
        if element > max_val:
            max_val = element
    return max_val


incre = [random.randint(1,1000000000) for _ in range(10000000)]
decre  = [random.randint(1,1000000000) for _ in range(10000000)]
incre = sorted(incre)
decre = sorted(decre, reverse=True)
to_find = incre + decre
#print(to_find)
print(max(to_find))
sol = find_max(to_find)
print(sol)