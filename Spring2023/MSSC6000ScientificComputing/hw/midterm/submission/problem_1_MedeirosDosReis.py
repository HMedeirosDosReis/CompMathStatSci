#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 3/15/2023

# 1 - Brute force Courier problem 

import itertools
import math

def brute_force(S, J):
    """
    Brute force function to solve the Courier Problem.
    Takes as input two arguemnts, the location of home S and a list of jobs J. 
    Returns the best route and the length of the route. 
    """
    best_route = []
    route_length = float("inf")

    all_routes = generate_routes(S,J)
    for route in all_routes:
        # If we start and end at home
        if route[0] == S and route[-1] == S:
            # And the rest of the route is also valid 
            if is_valid_route(route, J,S):
                # Compute route len
                new_rl = sum([calc_distance(route[i], route[i+1]) for i in range(len(route)-1)])
                # Is it better than the solution we have
                if route_length > new_rl:
                    # Update it
                    route_length = new_rl
                    best_route = route

    return (best_route, route_length)


def is_valid_route(route, jobs, home):
    """
    Takes in a route, all the jobs that needed to be completed and home.
    Returns True is all the locations were visited in a proper order,
    False otherwise
    """

    locations = set([loc for job in jobs for loc in job] + [home])
    # Did I visit all the pick ups and deliveries?
    if set(route) != locations:
        return False
    
    for i in range(len(jobs)):
        # Is the pickup location in my route?
        if jobs[i][0] not in route:
            return False
        # Save the indexes of the locations I went
        pickup_idx = route.index(jobs[i][0])
        delivery_idx = route.index(jobs[i][1])

        # Did I pick up before delivering?
        if delivery_idx < pickup_idx:
            return False
    return True


def calc_distance(point_1, point_2):
    """
    Helper function to calculate the distance between 2 points
    """
    distance = math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
    return distance


def generate_routes(home, jobs):
    """
    Helper function that takes a list of jobs and a home as a parameter. 
    Then returns alist with the whole search space of the courier problem. 
    Which should be of size (2n)!
    """

    # All routes should start at home then go to all the places
    locations = [home] + [loc for job in jobs for loc in job]

    # Generate the permutations
    permutations = list(itertools.permutations(locations))

    # Include home at the end
    routes = [list(p) + [home] for p in permutations]
    return routes


sol = brute_force((5,5), [((6,1),(1,1)),((4,9),(5,7)),((7,2),(8,8)),((9,9),(6,3))])
print(sol)
