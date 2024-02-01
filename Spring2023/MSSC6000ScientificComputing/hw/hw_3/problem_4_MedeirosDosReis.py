#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 3/6/2023

# 4 - Devide and Conquer Stock Prices 
import math

def mssc(prices):
    """
    Takes in a list of stock prices, whose indexes are the days corresponding
    to that price. 
    Returns the best day to buy and sell, such that the profit is maximized 
    """

    # Base case, if the lenght is one, buy and sell it in the same day, profit=0
    if len(prices) == 1:
        return [0, 0]

    # Find the midpoint and slice the list     
    mid_point = math.ceil(len(prices)/2)    
    left_prices = prices[:mid_point]
    right_prices = prices[mid_point:]

    # Solve the problem in the left half and right half 
    left_buy, left_sell = mssc(left_prices)
    right_buy, right_sell = mssc(right_prices)

    # Done dividing, start to conquer
    # Find smallest value in the left, and largest in the right 
    min_left = min(left_prices)
    max_right = max(right_prices)

    # Save the indexes that correspond to the day
    cross_buy = prices.index(min_left)
    cross_sell = prices.index(max_right)

    # Find profit 
    cross_profit = max_right - min_left
    
    # If the profit made buying at minimun in left and selling at maximum in right
    if cross_profit > left_sell-left_buy and cross_profit > right_sell-right_buy:
        # Then buy and sell across left and right 
        return [cross_buy, cross_sell]
    # If the profit is higher buying and selling inside left than inside right
    elif left_sell - left_buy > right_sell - right_buy:
        # Buy and sell in the left 
        return [left_buy, left_sell]
    # If we are here, buy and sell in right
    else:
        # Sum the midpoint, since we sliced the list 
        return [right_buy + mid_point, right_sell + mid_point]


sol = mssc([4,10,1,3,7,2,5,8])
print(sol)