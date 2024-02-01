#!/usr/bin/env python3

# Henri Medeiros Dos Reis
#2/13/2023
import itertools

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable) 
    return itertools.chain.from_iterable(itertools.combinations(s,r) for r in range(len(s)+1))

def generate_search_space(items):
    """
    Helper function that takes a list of items as a parameter. Then returns a
    list with the whole search space of the two knapsack problem. 
    Which should be of size 3^n
    """
    # Generate all possible subsets of items
    subsets = list(powerset(items))

    # We have all subsets of items combinations, but now, we need the 
    # combinations of them inside or outside each knapsack
    search_space = []

    for subset1 in subsets:
        for subset2 in subsets:
            # In case the sets are disjoint add to the subspace 
            if set(subset1).isdisjoint(set(subset2)):
                search_space.append((subset1, subset2))

    return search_space


def brute_force_two_knapsacks(items, first_cap, second_cap):
    """
    Takes as input a list of items, each item being a pair, the capacity for 
    knapsack 1 and the capacity for knapsack 2. Then, it returns the a list 
    of the items that are in the solution and the score of that solution. 
    """

    search_space = generate_search_space(items)

    best_knapsack1 = []
    best_knapsack2 = []
    best_score = 0

    # Loop through all the combinations in the search space, using 2 subsets
    for subset1, subset2 in search_space:
        # Calculate the total weight and value for each knapsack
        weight1 = sum(item[0] for item in subset1)
        weight2 = sum(item[0] for item in subset2)
        value1 = sum(item[1] for item in subset1)
        value2 = sum(item[1] for item in subset2)

        # Check if the solution is valid
        if weight1 <= first_cap and weight2 <= second_cap:
            # In case they are, then sum their values 
            total_value = value1 + value2

            # Is the new solution better than the previous? Update 
            if total_value > best_score:
                best_knapsack1 = list(subset1)
                best_knapsack2 = list(subset2)
                best_score = total_value

    # Combine the list of the solutions    
    best_sol = [best_knapsack1, best_knapsack2]

    return best_sol, best_score

import random 

def random_item():
    weight = random.randint(10,100)
    value = round(random.random()*weight)
    return (weight, value)

def random_items(n):
    return [random_item() for _ in range(n)]


items = random_items(16)

sol = brute_force_two_knapsacks(items, 150, 150)
print(sol)
