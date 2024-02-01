#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 3/20/2023

# 3 - Backtracking Courier problem 

# I modified the algorithm I gave in inclass part of the exam. The one I did 
# in class was not exactly a backtracking algorithm, since I had a part that 
# was considering the score of the solution, and backtracking should not do 
# that. 

import math

def backtracking(S, J):
    """
    Backtracking function to solve the Courier Problem.
    Takes as input two arguemnts, the location of home S and a list of jobs J. 
    Returns the best route and the length of the route. 
    """
    best_route = []
    route_length = float("inf")

    # Generate all valid routes
    all_routes = generate_routes(S,J)
    for route in all_routes:
        new_rl = sum([calc_distance(route[i], route[i+1]) 
                      for i in range(len(route)-1)])
        # Is it better than the solution we have
        if route_length > new_rl:
        # Update it
            route_length = new_rl
            best_route = route

    return (best_route, route_length)


def calc_distance(point_1, point_2):
    """
    Helper function to calculate the distance between 2 points
    """
    distance = math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
    return distance

def generate_routes(home, jobs):
    """
    Helper function that takes a list of jobs and a home as a parameter. 
    Then returns a list with the whole valid search space of the courier problem. 
    """

    # Save pickup and delivery locations
    pickups = [jobs[i][0] for i in range(0, len(jobs))]
    deliveries = [jobs[i][1] for i in range(0, len(jobs))]

    # All routes should start at home then go to all the places
    locations = [home] + [loc for job in jobs for loc in job]

    # Generate the permutations using backtrack
    permutations = []
    backtrack_helper([home], locations[1:], permutations,pickups,deliveries,home)

    return permutations

def backtrack_helper(curr_permutation, remaining_locations, permutations,
                      pickups, deliveries, home):
    """
    Backtracking helper, takes is the current "branch" that we are trying
    to expand (curr_permutation), all the locations we still need to visit,
    the permutations we did up to now, our pickup, deliveries and home locations. 

    Returns all the valid permutations for the courier problem
    """

    # If we went to all locations
    if not remaining_locations:
        # Check if pickups are made before deliveries
        for i in range(len(pickups)):
            if (curr_permutation.index(pickups[i]) 
                > curr_permutation.index(deliveries[i])):
                return # Prune it 
        permutations.append(curr_permutation + [home])
    else:
        # Else, there is still places to visit
        for loc in remaining_locations:
            new_permutation = curr_permutation + [loc]
            new_remaining_locations = [l for l in remaining_locations if l != loc]
            backtrack_helper(new_permutation, new_remaining_locations,
                             permutations,pickups,deliveries,home)


sol = backtracking((5,5), [((6,1),(1,1)),((4,9),(5,7)),((7,2),(8,8)),((9,9),(6,3))])
print(sol)
