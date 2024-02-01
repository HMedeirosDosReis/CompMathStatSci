#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 09/06/2023

# Function to detect arbitrage opportunities in a currency exchange graph
def Arbitrage(G):
    """
    Detect arbitrage opportunities in a currency exchange graph.

    Parameters:
    - G: A 2D list representing the adjacency matrix with currency exchange rates.

    Returns:
    - D: The final adjacency matrix after the algorithm completes.
    """
    D = G
    # Floyd-Warshall
    for k in range(0, len(G)):
        for i in range(0, len(G)):
            for j in range(0, len(G)):
                if i != k and j != k:
                    mul = D[i][k] * D[k][j]
                    if mul > D[i][j]:
                        D[i][j] = mul

    for i in range(0, len(G)):
        if D[i][i] > 1:
            print("Can get from node", i + 1, "back to node",
                  i + 1, "with a value more than 1")
    return D

# Function to detect arbitrage opportunities in a currency exchange graph and print the path
def Arbitrage_print(G):
    """
    Detect arbitrage opportunities in a currency exchange graph and print the path.

    Parameters:
    - G: A 2D list representing the adjacency matrix with currency exchange rates.

    Returns:
    - D: The final adjacency matrix after the algorithm completes.
    """
    # Create a copy of the original adjacency matrix to keep track of the previous node
    prev = [row[:] for row in G]

    for s in range(0, len(G)):
        for t in range(0, len(G)):
            prev[s][t] = t

    D = G
    # Floyd-Warshall
    for k in range(0, len(G)):
        for i in range(0, len(G)):
            for j in range(0, len(G)):
                if i != k and j != k:
                    mul = D[i][k] * D[k][j]
                    if mul > D[i][j]:
                        D[i][j] = mul
                        prev[i][j] = prev[i][k]

    dummy = 1
    for i in range(0, len(G)):
        if D[i][i] > 1:
            print("Can get from node", i + 1, "back to node",
                  i + 1, "with a value more than 1")
            print("Path for solution:", end=' ')
            print_sol(i, i, prev)
            dummy = 0
    if dummy:
        print("No solution given the graph")

    return D

# Function to print the solution path
def print_sol(starting, ending, my_matrix):
    print(starting + 1, "-> ", end='')
    if my_matrix[starting][ending] == ending:
        print(ending + 1)
        print()
        return
    else:
        middle = my_matrix[starting][ending]
        print_sol(middle, ending, my_matrix)

# Example usage of the arbitrage detection algorithm
final_D = Arbitrage_print([[1, 2, 3, 4],
                           [1/3, 1, 0, 1/2],
                           [1/2, 0, 1, 3],
                           [1/4, 2, 1/2, 1]])

print("Solution:", final_D)


# List of test cases (each test case is a 2D graph)
test_cases = [
    [ # graph 1
        [1, 0.5],
        [2, 1]
    ],
    [
        [1, 2],
        [0.5, 1]
    ],
    [ # graph 2
        [1, 2, 0.5],
        [0.5, 1, 2],
        [2, 0.5, 1]
    ],
    [ # graph 3
        [1, 0.5, 2],
        [2, 1, 0.5],
        [0.5, 2, 1]
    ],
    [ # graph 4
        [1, 2, 0.5, 0.25],
        [0.5, 1, 2, 0.5],
        [2, 0.5, 1, 4],
        [4, 2, 0.25, 1]
    ],
    [ # graph 5
        [1, 2, 0.5, 0.25, 1],
        [0.5, 1, 2, 0.5, 1],
        [0.25, 4, 1, 4, 1],
        [4, 2, 0.25, 1, 1]
    ],
    [ # graph 6
        [1, 2, 0.5],
        [0.5, 1, -2],
        [-2, 0.5, 1]
    ],
    [ # graph 7
        [1, 2, 0.5, 0.25],
        [0.5, 1, 2, 0.5],
        [2, 0.5, 1, 1000],
        [4, 2, 0.25, 1]
    ]
]

# Iterate through test cases
for i, graph in enumerate(test_cases):
    print("Test Case", i + 1)
    c = [row[:] for row in graph]
    result = Arbitrage_print(graph)
    print("Original graph:",c)
    print("Result:", result)
    print()
