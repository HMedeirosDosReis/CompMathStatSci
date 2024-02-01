#!/usr/bin/env python3

# Henri Medeiros Dos Reis
#2/15/2023

# 4 - Gamestop greedy 

def read_data(file_name):
    """
    Reads in the file at <file_name> and returns a list of tuples of length two of the
    form (money, wait_time).

    A wait time of 0 means the customer will leave if not served first.
    A wait time of 1 means the customer will leave if not served first or second.
    etc.
    """

    customers = []
    with open(file_name, "r") as f:
        for line in f:
            data = line.strip().split(" ")
            if data:
                customers.append((int(data[0]), int(data[1])))
    return customers

def gamestop(customers):
    """
    Takes in a list of customers as input, then returns the best way to sell
    up to 60 consoles to customers that will wait a certain amount of time
    """

    # Start variable
    revenue = 0
    # Record the times that each customer can wait 
    times = [i[1] for i in customers]
    # The number of consoles that I can sell at most is the max wait time + 1 
    num_consoles_can_sell = max(times)+1

    # Sort customers in descending order based on the amount they are willing to pay
    # and their wait time
    sorted_customers = sorted(customers, key=lambda x: (-x[0], x[1]))
    sold_customers = []
    # Loop through the list of customers
    for customer in sorted_customers:
        # If there are consoles left 
        if num_consoles_can_sell >= 1 : 
            # Sell console to customer, increase revenue and descrese the number of consoles
            sold_customers.append(customer)
            revenue += customer[0]
            num_consoles_can_sell -= 1
        else:
            # Out of consoles, we are done selling
            break
    # Sort the sold_customers, but now only based on the wait time
    sold_customers = sorted(sold_customers, key=lambda x: x[1])
    # If we sold less than 60, record all the other timeslots as None
    if len(sold_customers) < 60:
        for i in range(len(sold_customers), 60):
            sold_customers.append(None)
    print(sold_customers)
    print(revenue)

