#!/usr/bin/env python3

# Henri Medeiros Dos Reis
#2/13/2023

# 2 - knapsack 3 versions 

def read_data(file_name):
    """
    reads in the file at <file_name> and returns a tuple wih two entries
    - the first entry is the capacity of the knapsack (a float)
    - the second entry is a list of 3-tuples, (name, weight, value), a string and two
        floats, for each item
    """

    capacity = 0
    items = []

    with open(file_name, "r") as f:
        capacity = float(f.readline().strip())
        for line in f:
            data = line.strip()
            if data:
                split_data = data.split(" ")
                items.append(
                    (split_data[0], float(split_data[1]), float(split_data[2]))
                )

    return (capacity, items)

def run_greedy(items, capacity, sort_function):
    """
    Takes 3 inputs, items, capacity and a sort_function to solve the knapsack
    problem in three different versions. 
    """

    # Start variables 
    cur_w = 0
    cur_v = 0
    
    # Sort the items accordingly with the sort_function from input
    sorted_items = sorted(items, key=sort_function)
    solution = []

    # Loop through sorted items. 
    while len(sorted_items) > 0:
        # Take the first item
        item = sorted_items.pop(0)
        # If we can carry, record weight and value in cur_w and cur_v
        if capacity >= cur_w+item[1]:
            cur_w += item[1]
            cur_v += item[2]
            # Save this item in solution
            solution.append(item[0])
    return solution,cur_w, cur_v

def greedy(items, cap):
    """
    Helper function that actually calls the greedy algorithm and handles output
    """

    # Define 3 lambda functions, one of each definition of the best 
    lightest_weight = lambda item : item[1]
    highest_value = lambda item : -item[2]
    lrvw = lambda item : -item[2]/item[1]
    
    # Call the algorithm and store in different versions of the solution
    s1 = run_greedy(items, cap, lightest_weight)
    s2 = run_greedy(items, cap, highest_value)
    s3 = run_greedy(items, cap, lrvw)

    print("lightest")
    print("solution: ", s1[0])
    print("weight: ", round(s1[1],2))
    print("value: ", round(s1[2],2))
    print()
    print("most valuable")
    print("solution: ", s2[0])
    print("weight: ", round(s2[1],2))
    print("value: ", round(s2[2],2))
    print()
    print("largest ratio")
    print("solution: ", s3[0])
    print("weight: ", round(s3[1],2))
    print("value: ", round(s3[2],2))


