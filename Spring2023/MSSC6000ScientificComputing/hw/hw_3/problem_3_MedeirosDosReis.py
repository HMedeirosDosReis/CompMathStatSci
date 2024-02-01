#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 3/6/2023

# 3 - Find the largest element in a list 

import math

def find_max(elements):
    """
    Takes in a list of elements that start increasing and then decreases, once
    it starts to decrease, it never increases again. 
    Returns the maximum value in that list 
    """

    my_list = list(elements)

    # Base case, if only one element, then this is the answer 
    if len(my_list) == 1:
        return my_list[0]
        
    # Find the midpoint and slice the list     
    mid_point = math.ceil(len(my_list)/2)
    left_half = my_list[:mid_point]   
    right_half = my_list[mid_point:]

    # Get the last element in the left, and the first in the right 
    last_element_left = left_half[-1]
    first_element_right = right_half[0]

    # In case the largest is in the left, solve from left, otherwise, solve from right
    if last_element_left >= first_element_right:
        return find_max(left_half)
    else:
        return find_max(right_half)

sol = find_max([3,6,7,12,17,5,2,1])
print(sol)
