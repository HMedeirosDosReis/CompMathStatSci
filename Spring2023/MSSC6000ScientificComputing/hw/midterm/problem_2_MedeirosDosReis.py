#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 3/16/2023

# 2 - Greedy Courier problem 

import math

def greedy(S, J):
    """
    Brute force function to solve the Courier Problem.
    Takes as input two arguemnts, the location of home S and a list of jobs J. 
    Returns the a good route and the length of the route. 
    """

    # Start from home
    current_location = S
    unvisited_pickup_locations = [pickup for (pickup, _) in J]
    unvisited_delivery_locations = [delivery for (_, delivery) in J]
    visited_locations = [S]
    total_distance = 0

    # First pick up all the packages
    while unvisited_pickup_locations:

        # Calculate the distances for all packages
        pickup_distances = [(calc_distance(current_location, pickup), pickup)
                             for pickup in unvisited_pickup_locations]
        # Go to the closest one
        closest = min(pickup_distances, key=lambda x: x[0])
        total_distance += closest[0]
        current_location = closest[1] # Save where we are 
        visited_locations += [closest[1]] # Add it to the route
        unvisited_pickup_locations.remove(closest[1]) # Mark as visited

    # Now deliver all the packages
    while unvisited_delivery_locations:

        # Calculate the distances for all deliveries
        delivery_distances = [(calc_distance(current_location, delivery), delivery)
                               for delivery in unvisited_delivery_locations]
        closest = min(delivery_distances, key=lambda x: x[0])
        total_distance += closest[0]
        current_location = closest[1] # Save where we are 
        visited_locations += [closest[1]] # Add it to the route
        unvisited_delivery_locations.remove(closest[1]) # Mark as visited

    # Return home
    total_distance += calc_distance(current_location, S)
    visited_locations.append(S)

    return visited_locations, total_distance


def calc_distance(point_1, point_2):
    """
    Helper function to calculate the distance between 2 points
    """
    distance = math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
    return distance

sol = greedy((5,5), [((6,1),(1,1)),((4,9),(5,7)),((7,2),(8,8)),((9,9),(6,3))])
print(sol)
