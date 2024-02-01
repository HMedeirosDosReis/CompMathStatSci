# Henri Medeiros Dos Reis
# 05/05/2023

# 1 - Hill climbing cylindrical tank problem 
import random
import math
import time

class my_function:
    """
    Class for a continuous functions that has bounds and constraints 
    """

    def __init__(self, score, bounds):
        """
        Initializer 
        """
        self.score = score
        self.bounds = bounds

    def random_in_bounds(self):
        """
        Returns a random point that is bounded by the bounds in every dimension
        """
        point = []
        for (lower, upper) in self.bounds:
            diff = upper - lower
            point.append(random.random() * diff + lower)
        return point
    
    def is_in_bounds(self, point):
        """
        Returns true if all bounds of the function are satisfied 
        """
        return all(
            p >= bnd[0] and p <= bnd[1]
            for (p, bnd) in zip(point, self.bounds)
        )
    
    def constraints(self, point):
        """
        Returns True if all the constraints are satisfied 
        """
        d_1 = point[0]
        d_2 = point[1]
        r = point[2]
        L = point[3]
        first=0
        second=0  
        third=0
        fourth = 0

        # If first constraint is met, set first to 1 (True)
        if d_1 >= 0.0193*r:
            first = 1
        # If second constraint is met, set second to 1 (True)
        if d_2 >= 0.00954*r:
            second = 1
        # If third constraint is met, set third to 1 (True)
        if math.pi*r**2*L>=1296000:
            third =1
        # If fourth constraint is met, set fourth to 1 (True)
        if L <= 240:
            fourth = 1
        
        # Returns True, if all the variables are True
        return first and second and third and fourth
    
    def scoref(self, point):
        """
        Evaluate the point 
        """
        return self.score(*point)
    
    def tweak(self, point):
        """
        Tweak function used to move the point in space, also guarantees to 
        tweak only inside of valid space. It takes into acount the range of 
        each dimension to do the magnitute of the tweak
        """
        delta_ds = 0.005
        delta_r = 0.1
        delta_L = 0.1
        d_1 = point[0]
        d_2 = point[1]
        r = point[2]
        L = point[3]

        new_d1 = d_1 + (random.random()*2-1) * delta_ds
        while new_d1 < 0.0625 or new_d1 > 1:
            new_d1 = d_1 + (random.random()*2-1) * delta_ds
        
        new_d2 = d_2 + (random.random()*2-1) * delta_ds
        while new_d2 < 0.0625 or new_d2 > 1:
            new_d2 = d_2 + (random.random()*2-1) * delta_ds

        new_r = r + (random.random()*2-1) * delta_r
        while new_r < 10:
            new_r = r + (random.random()*2-1) * delta_r

        new_L = L + (random.random()*2-1) * delta_L
        while new_L > 200:
            new_L = L + (random.random()*2-1) * delta_L

        new_point = [new_d1,new_d2,new_r, new_L]
        return new_point
    
class HCmanager:
    """
    Class that will manage the Hill Climbing 
    """
    def __init__(
        self,
        space,
        N,
        maximization=True
    ):
        """
        Initializer 
        """
        self.space = space
        self.N = N
        self.maximization = maximization

        self.best_sol = None
        self.best_score = None
        self.best_sol_over_restarts = []

    def better(self, curr, prev):
        """
        Is this new score better than the previous one? returns true if so
        """
        if self.maximization:
            return curr > prev
        return curr < prev
    
    def random_solution(self):
        """
        Function to generate a random solution 
        """
        return self.space.random_in_bounds()



    def optimize(self):
        """
        Actual Hill Climbing part 
        """

        # Number of restarts predefined 
        for i in range(0,self.N):
            # Start from random solution
            start = self.random_solution()
            # Is any of the contraints violated?
            while not self.space.constraints(start):
                start = self.random_solution()
            
            # We are good to go
            self.best_sol = start
            self.best_score = self.space.scoref(start) 

            worse = 0
            # Start trying to climb
            while True:
                new_sol = self.space.tweak(self.best_sol)
                while not self.space.constraints(new_sol):
                    new_sol = self.space.tweak(self.best_sol)
                
                # Compute score
                new_score = self.space.scoref(new_sol)
                if self.better(self.best_score, new_score):
                    # This one is better, reset the worse we've seen and 
                    # update the best we've seen
                    worse = 0
                    self.best_sol = new_sol
                    self.best_score = new_score
                else:
                    # This one is worse
                    worse += 1
                    if worse > 5000:
                        # We tried 5000 times to climb and didnt climb,
                        # time to print results and restart
                        print(f"Best score ={self.best_score:.4f},\n"
                            f"Best solution={self.best_sol}")
                        self.best_sol_over_restarts+= [[self.best_score, [self.best_sol]]]
                        print(f"Restarts: {i+1}/{self.N}")
                        break
        # Return the minimum solution across all the restarts 
        return min(self.best_sol_over_restarts, key=lambda x: x[0])


eval_func = lambda d_1,d_2,r,L: 0.6224*d_1*r*L+1.7781*d_2*r**2+3.1661*d_1**2*L+19.84*d_1**2*r

# Bound I came up with that were not given by the problem:
# r < 1000, upon testing, having bigger numbers for r only slow the process to
# find good solutions that satisfies constraits. Since the problem just gives 
# a lower bound for r, the random solutions with an infinite bound that 
# satisfies the constraints are VERY hard to find
bounds = [[0.0625,1],[0.0625,1],[10,1000],[0,200]]

cost_function = my_function(eval_func, bounds)

restarts = 300
HC = HCmanager(cost_function,restarts,maximization=False)

# start_time = time.time()

final_best = HC.optimize()
print(f"Final solution:\n"
      f"Best score = {final_best[0]:.4f}\n"
      f"Best solution = {final_best[1]}")

# Code takes around 100 seconds on my pc 
# end_time = time.time()
# total_time = end_time - start_time
# print(f"Total time taken:{total_time} seconds")