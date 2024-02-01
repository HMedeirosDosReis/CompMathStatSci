#!/usr/bin/env python3

# Henri Medeiros Dos Reis
#2/2/2023

# 3 - Distinct powers.

# Idea 1
# Just use sets to take care of the duplicates 
#my_set = set()

# Loop through the needed values, calculate their powers and add to the set
#for i in range(2,101):
#    for j in range(2,101):
#        a_power_b = i**j 
#        my_set.add(a_power_b)
#print(len(my_set))

# Idea 2
print(len(set(i**j for i in range(2,101) for j in range(2,101))))
