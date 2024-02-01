
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


class GeometricSimulatedAnnealing:

    def __init__(self, space, alpha, maximization=True):
        self.space = space
        self.maximization = maximization
        self.initial_temp = self.determine_initial_temp()
        self.alpha = alpha
        self.temp = self.initial_temp
        

    def determine_initial_temp(self, trials=1000, initial_prob=0.95):
        total_change = 0
        decreases = 0
        tried = 0
        while decreases < trials:
            tried += 1
            sol = self.space.random()
            new_sol = self.space.tweak(sol)
            diff = self.space.score(new_sol) - self.space.score(sol)
            if not self.maximization:
                diff *= -1
            if diff < 0:
                decreases += 1
                total_change += diff
        avg_change = total_change / trials
        return avg_change / math.log(initial_prob)

    def advance_temp(self):
        self.temp *= self.alpha

    def accept(self, old_score, new_score):
        score_change = new_score - old_score
        
        if not self.maximization:
            score_change *= -1

        if score_change > 0:
            return True
        else:
            accept_probability = math.exp(score_change/self.temp)
            return random.random() < accept_probability

    def is_worse(self, old_score, new_score):
        score_change = new_score - old_score
        
        if not self.maximization:
            score_change *= -1

        return score_change < 0


eval_function = lambda x,y: math.sin(3*math.pi*x)**2 + (x-1)**2*(1+math.sin(3*math.pi*y)**2) + (y-1)**2*(1+math.sin(2*math.pi*y)**2)
bounds = [[-10, 10]]*2
tweak_delta = 0.1
cns_func = ContinuousFunction(eval_function, bounds, tweak_delta)
alpha = 0.999999

SA = GeometricSimulatedAnnealing(cns_func, alpha, maximization=False)

point = cns_func.random()
value = cns_func.score(point)
best = None

final_temp_factor = 0.00000001

num_gens = math.ceil(math.log(final_temp_factor)/math.log(alpha))
gen = 0

while SA.temp > final_temp_factor * SA.initial_temp:
    
    total = 0
    accept = 0
    gen += 1

    for i in range(1000):
        
        if best is None or value < best:
            best = value
            best_sol = point

        new_point = cns_func.tweak(point)
        new_value = cns_func.score(new_point)

        if SA.is_worse(value, new_value):
            total += 1
        if SA.accept(value, new_value):
            if SA.is_worse(value, new_value):
                accept += 1
            point = new_point
            value = new_value

    print(
        f"gen: {gen}/{num_gens}, "
        f"temp: {SA.temp:.2f}, "
        f"% acc: {accept/total*100:.5f}, "
        f"cur score: {value:.2f}, "
        f"best score: {best}, "
    )

    SA.advance_temp()
