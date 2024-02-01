#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 3/3/2023

# 3 - Find the largest element in a list 

import math
import random

def find_max(elements):
    my_list = list(elements)

    if len(my_list) == 1:
        return my_list[0]
        
    mid_point = math.ceil(len(my_list)/2)
    left_half = my_list[:mid_point]   
    right_half = my_list[mid_point:]

    # In case the largest is in the left, solve from left, otherwise, solve from right
    last_element_left = left_half[-1]
    first_element_right = right_half[0]

    if last_element_left >= first_element_right:
        return find_max(left_half)
    else:
        return find_max(right_half)


incre = [random.randint(1,1000000000) for _ in range(10000000)]
decre  = [random.randint(1,100000000) for _ in range(10000000)]
incre = sorted(incre)
decre = sorted(decre, reverse=True)
to_find = incre + decre
#print(to_find)
print(max(to_find))
sol = find_max(to_find)
print(sol)
