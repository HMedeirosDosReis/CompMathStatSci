#!/usr/bin/env python3

# Henri Medeiros Dos Reis
#2/13/2023

# 1 - Smallest sum of products from 2 lists

def read_data(file_name):
    """
    reads in the file at <file_name> and returns a list of two lists, e.g.
    [[1, 2, 3], [4, 5, 6]]
    """

    with open(file_name, "r") as f:
        list1 = list(map(int, f.readline().strip().split(" ")))
        list2 = list(map(int, f.readline().strip().split(" ")))
    return [list1, list2]

def greedy(l1,l2):
    """
    Takes two lists of integer as input, and returns the smallest sum
    between the products of pairs of the lists. 
    """

    # The solution is to sort one list in reverse, and sort the other one normally
    list1 = sorted(l1)
    list2 = sorted(l2, reverse=True)
    
    # Loops from 1 to the length of one of the lists, and multiply both 
    # corresponding values of the the lists
    s = [list1[i]*list2[i] for i in range(1,len(list1))]
    print(sum(s))

