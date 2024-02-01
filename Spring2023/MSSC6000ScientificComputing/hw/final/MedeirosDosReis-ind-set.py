# Henri Medeiros Dos Reis
# 05/05/2023

# 2 - SA - Largest independent set 

"""
This code has a bug, for some reason, my function 'is_independet_set' fails
quite often. The problem does not seem to be the function it self, but on
the variables that are being passed to the function. I could not track where
it was happening. 

This bug sometimes causes solutions to not be an independent set.  
"""

import random
import math
import time

class graph:
    """
    Class that represents a graph
    """
    def __init__(self, vertices, edges):
        """
        Initializer
        """
        self.vertices = [i for i in range(0,vertices)]
        self.edges = edges

    def size(self):
        return len(self.vertices)
    
    def smallest_edges(self):
        """
        Returns the vertex that has the smallest number of edges
        """
        min_edges = float('inf')
        vertex = None
        # Loop through the vertices 
        for v in self.vertices:
            # How many edge does each one have?
            edges_count = sum(1 for e in self.edges if v in e)
            # Is it smaller than the ones I saw previously, update it
            if edges_count<min_edges:
                min_edges = edges_count
                vertex=v
        return vertex


    def remove_vertex(self, v):
        """
        Removes vertex v from the graph. Also removes every edge and vertices 
        that were adjascent to this vertex
        """
        self.vertices.remove(v)
        # Find out which ones are adjacent 
        vertices_to_remove = [w for (u, w) in self.edges if (u == v or w == v) and w in self.vertices]
        self.edges = [e for e in self.edges if v not in e]
        # Loop and remove
        for i in vertices_to_remove:
            self.vertices.remove(i)
            self.edges = [e for e in self.edges if i not in e]


    def tweak(self, independent_set):
        """
        Tweak function that tries to do a small tweak in the solution. 

        This is not a good tweak function. Since we are pretty much just 
        generating random solutions and changing 2 elements from them. 
        The reason why I went with this tweak function was due to the 
        bug I talked about in the beggining of the code. Which caused it
        to be really hard to tweak and get valid solutions 
        """
        # Make a copy of the graph and solution 
        n = self.size()
        edg = list(self.edges)
        ind = graph(n,edg)
        ind_set = list(independent_set)
        ind_set = random_solution(ind)

        # Pick two elements from the solution
        element = random.choice(independent_set)
        element2 = random.choice(independent_set)

        # If the element is in the new solution, take it out
        # If it isnt, then add it there
        if(len(ind_set)> 1): 
            if element in ind_set:
                ind_set.remove(element)
            else:
                ind_set.append(element)
        
        if(len(ind_set)> 1): 
            if element2 in ind_set:
                ind_set.remove(element2)
            else:
                ind_set.append(element2)

        # while(not is_independent_set(ind_set, ind)): NOT WORKING
        # delete some vertices from the solution 
        
        return ind_set


def random_solution(no_change_graph):
    """
    Generates a random solution. Always a valid solution.
    """
    graph1 = graph(no_change_graph.size(),no_change_graph.edges)
    # Initialize empty solution
    independent_set = []
    # While there are vertices left
    while graph1.size() > 0:
        # Pick a randon vertice, add it to the solution, remove from the graph 
        v = random.choice(graph1.vertices)
        independent_set.append(v)
        graph1.remove_vertex(v)
    return independent_set


def is_independent_set(vertices, G):
    """
    Returns true if the vertices are an indepentend set of G 
    """
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if (vertices[i], vertices[j]) in G.edges or (vertices[j], vertices[i]) in G.edges:
                return False
    return True





def greedy(no_change_graph):
    """
    Greedy solution for the problem. Acts like the random solution, with 
    only one difference, which is how it is taking the vertices. It always
    picks the vertice with the smallest number of edges
    """
    graph1 = graph(no_change_graph.size(),no_change_graph.edges)
    independent_set = []
    while graph1.size() > 0:
        v = graph1.smallest_edges()
        independent_set.append(v)
        graph1.remove_vertex(v)
    return independent_set


def score(solution):
    return len(solution)

def random_graph(n, p):
    """
    Generates a fully connected random graph on n vertices.
    Each possible edge exists with probability p
    """
    edges = []
    for v1 in range(1, n+1):
        for v2 in range(v1+1, n+1):
            if random.random() <= p:
                edges.append([v1, v2])
    
    # Add edges to connect any isolated vertices
    isolated_vertices = [v for v in range(1, n+1) if v not in {e[0] for e in edges}]
    for i in range(len(isolated_vertices)):
        for j in range(i+1, len(isolated_vertices)):
            edges.append([isolated_vertices[i], isolated_vertices[j]])
    
    return graph(n, edges)

class SA:
    """
    Class that defines simulated annealing 
    """

    def __init__(self, graph1, alpha,final_temp_factor,dont_change, maximization = True):
        """
        Initializer 
        """
        self.graph = graph1
        self.alpha = alpha
        self.final_temp_factor = final_temp_factor
        self.maximization = maximization
        self.dc = dont_change
        self.i_temp = self.initial_temp()
        self.temp = self.i_temp
        

    def initial_temp(self, trials = 1000, initial_prob = 0.9):
        """
        Function that returns what the initial temperature should be in 
        order to get an initial probability of 90%
        """

        change = 0
        worse = 0
        iteration = 0
        # Loop until we get more worsenings than the trials 
        while worse < trials:
            iteration +=1

            # Get a randon solution, make a copy and tweak the copy 
            sol = random_solution(self.graph)
            copy_sol = list(sol)
            new_sol = self.graph.tweak(copy_sol)

            diff_in_score = score(sol)-score(new_sol)

            # If not maximizing, make sure to switch signs 
            if not self.maximization:
                diff_in_score = -diff_in_score
            
            if diff_in_score<0:
                worse += 1
                change += diff_in_score
        # compute the temperature
        avg = change/iteration
        return avg/math.log(initial_prob)
        
    def should_accept(self, old, new):
        """
        Returns true if we should accept this solution
        """
        change = new-old

        if not self.maximization:
            change = -change
        
        if change > 0:
            return 1
        
        else:
            prob = math.exp(change/self.temp)
            return random.random() < prob
    
    # Is the new solution worse?
    def is_worse(self, old, new):
        change = new - old
        if not self.maximization:
            change = -change
        return change < 0 
    
    #simA = (self, graph1, alpha, final_temp, maximization = True):
def metaheuristic(simA, trials_per_gen,dont_change):
    """
    Funcion that will run the simulated annealing
    """

    # Make a copy of the graph
    n = simA.graph.size()
    edg = list(simA.graph.edges)
    copy_graph = graph(n,edg)

    # get a random sol and compute scores 
    sol = random_solution(copy_graph)
    curr_score = score(sol)
    best_sol = sol
    best_score = curr_score

    # How many generations?
    gens = math.ceil(math.log(simA.final_temp_factor)/math.log(simA.alpha))
    gen = 0

    while (simA.temp > simA.final_temp_factor*simA.i_temp):
        gen += 1
        total = 0
        accept = 0

        for i in range(0,trials_per_gen):
            # Make a copy of the solution and tweak it
            copy_sol = list(sol)
            new_sol = simA.graph.tweak(copy_sol)
            new_score = score(new_sol)

            # if worse, record we saw a worse one
            if simA.is_worse(curr_score,new_score):
                total+=1
            # if we should accept, accept, record we accepted if worse
            if simA.should_accept(curr_score,new_score):
                if simA.is_worse(curr_score,new_score):
                    accept+=1
                else:
                    # It is a better sol, so just update it
                    if new_score > best_score:
                        best_sol = new_sol
                        best_score = new_score
                # update the current ones before going to the next iteration
                sol = new_sol
                curr_score = new_score

        print(
            f"gen: {gen}/{gens}, "
            f"temp: {simA.temp:.6f}, "
            f"% acc: {accept/total*100:.5f}, "
            f"cur score: {curr_score}, "
            f"best score: {best_score}, "
        )
        # decrease temp
        simA.temp *= simA.alpha
    return best_sol


input_graph = [7, [(0,1), (1,2), (1,3), (1,5), (2,6), (3,4), (4,6)]]
G = graph(input_graph[0], input_graph[1])
alpha = 0.97
final_temp_fact = 0.01
G = random_graph(100,0.1)# takes around 3 minutes to run with these parameters 
sol = greedy(G)
print(sol)
#simA = (self, graph1, alpha, final_temp_factor, maximization = True):
start_time = time.time()
my_SA = SA(G,alpha,final_temp_fact,G)

sol = metaheuristic(my_SA,1000,G)
print(sol)
print(is_independent_set(sol,G))
end_time = time.time()
total_time = end_time - start_time
print(f"Total time taken:{total_time} seconds")





