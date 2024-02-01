#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 3/3/2023

# 2 - Backtracking two knapsacks 

def backtracking_two_knapsacks(items, first_cap, second_cap):
    """
    This is a helper function that will actually call the function that will
    solve the problem. 
    Takes as input a list of items, each item being a pair, the capacity for 
    knapsack 1 and the capacity for knapsack 2. Then, it returns the a list 
    of the items that are in the solution and the score of that solution. 
    """

    n = len(items)

    my_sol = solve(items, first_cap, second_cap, n)
    
    # Get the best score from the solution 
    first_list = list(my_sol[0])
    second_list = list(my_sol[1])
    score_1 = sum(first_list[i][1] for i in range(len(first_list)))
    score_2 = sum(second_list[i][1] for i in range(len(second_list)))
    
    return [my_sol, score_1+score_2]

def solve(items, first_cap, second_cap,n):
    """
    Function that actually solves the problem. Takes as input a list of items, 
    each item being a pair, the capacity knapsack 1, the capacity for 
    knapsack 2 and the size of the list.
    Returns two lists, each containing the items in each knapsack. 
    """

    # Base case, if we cant fit it in either knapsack, return 
    if first_cap <= 0 and second_cap <= 0:
        return [],[]
    
    best_score = 0
    best_sol_1 = []
    best_sol_2 = []

    # Loop through all the items before making any decision 
    for i in range(len(items)):
        weight_i, value_i = items[i]

        # If we can fit in the first knapsack, put it and solve from there
        if first_cap >= weight_i:
            sol_1, sol_2 = solve(items[1+i:], first_cap-weight_i,
                                second_cap, n-i+1)
            score_sol1 = sum(sol_1[j][1] for j in range(len(sol_1)))
            score_sol2 = sum(sol_2[j][1] for j in range(len(sol_2)))
            score = value_i + score_sol1 +score_sol2
            
            # If we find a better score, update the sol
            if score > best_score:
                best_score = score
                best_sol_1 = [(weight_i,value_i)]+ sol_1
                best_sol_2 = sol_2    
        
        # If we can fit in the second knapsack, put it and solve from there
        if second_cap >= weight_i:
            sol_1, sol_2 = solve(items[1+i:], first_cap,
                                second_cap-weight_i, n-i+1)
            score_sol1 = sum(sol_1[j][1] for j in range(len(sol_1)))
            score_sol2 = sum(sol_2[j][1] for j in range(len(sol_2)))
            score = value_i + score_sol1 +score_sol2
            
            # If we find a better score, update the sol
            if score > best_score:
                best_score = score
                best_sol_1 = sol_1
                best_sol_2 = [(weight_i,value_i)] + sol_2
    
    # Once we are here, we are done
    return best_sol_1, best_sol_2

import random 

def random_item():
    weight = random.randint(10,100)
    value = round(random.random()*weight)
    return (weight, value)

def random_items(n):
    return [random_item() for _ in range(n)]


items = random_items(30)

sol = backtracking_two_knapsacks(items, 150,150)
print(sol)
