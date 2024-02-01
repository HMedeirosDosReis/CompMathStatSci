
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import numpy as np
import math
import random
import time


class ContinuousFunction:

    def __init__(self, eval_function, bounds, tweak_delta):
        self.eval_function =  eval_function
        self.bounds = bounds
        self.tweak_delta = tweak_delta

    def random(self):
        pt = []
        for (_min, _max) in self.bounds:
            diff = _max - _min
            pt.append(random.random() * diff + _min)
        return pt

    def in_bounds(self, point):
        return all(
            p >= bnd[0] and p <= bnd[1]
            for (p, bnd) in zip(point, self.bounds)
        )

    def tweak(self, point):
        delta = self.tweak_delta

        new_point = [coord + delta * (2 * random.random() - 1) for coord in point]
        while not self.in_bounds(new_point):
            new_point = [coord + delta * (2 * random.random() - 1) for coord in point]
        return new_point

    def score(self, point):
        return self.eval_function(*point)


eval_function = lambda x,y: math.sin(3*math.pi*x)**2 + (x-1)**2*(1+math.sin(3*math.pi*y)**2) + (y-1)**2*(1+math.sin(2*math.pi*y)**2) + 1
bounds = [[-10, 10]]*2
tweak_delta = 0.1
cns_func = ContinuousFunction(eval_function, bounds, tweak_delta)


alpha = 0.99
temp = 100
final_temp_factor = 1/100000
final_temp = temp * final_temp_factor
tweaks_per_temp = 20000

point = cns_func.random()
value = cns_func.score(point)
best = None

num_gens = math.ceil(math.log(final_temp_factor)/math.log(alpha))
gen = 0

while temp > final_temp:
    
    num_worse_total = 0
    num_worse_accepted = 0
    gen += 1

    for i in range(tweaks_per_temp):
        
        if best is None or value < best:
            best = value
            best_sol = point

        new_point = cns_func.tweak(point)
        new_value = cns_func.score(new_point)

        if new_value > value:
            # worse solution
            num_worse_total += 1

            # check if we should accept
            score_change = value - new_value

            accept_probability = math.exp(score_change/temp)
            if random.random() < accept_probability:
                # accept
                num_worse_accepted += 1
                point = new_point
                value = new_value
        else:
            # better solution, always accept
            point = new_point
            value = new_value
                
    print(
        f"gen: {gen}/{num_gens}, "
        f"temp: {temp:.2f}, "
        f"% acc: {num_worse_accepted/num_worse_total*100:.5f}, "
        f"cur score: {value:.2f}, "
        f"best score: {best}, "
    )

    temp *= alpha
