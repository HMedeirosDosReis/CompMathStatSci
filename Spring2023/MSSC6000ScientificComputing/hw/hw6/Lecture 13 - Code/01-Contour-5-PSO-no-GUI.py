import numpy as np
import math
import random
import time

# np.whatever
# numpy.whatever


class ContinuousFunction:
    """
    This is a class that represents the function we are trying to optimize.
    eval_function is a lambda function representing the function we're
       optimizing, and bounds represents the min and max allowed value in
       each dimension (so, this assumes a rectangular boundary)
    """

    def __init__(self, eval_function, bounds):
        self.eval_function =  eval_function
        self.bounds = bounds

    """
    Return a random point within the bounds
    """
    def random(self):
        pt = []
        for (_min, _max) in self.bounds:
            diff = _max - _min
            pt.append(random.random() * diff + _min)
        return pt

    """
    Check if a point is within the bounds
    """
    def in_bounds(self, point):
        return all(
            p >= bnd[0] and p <= bnd[1]
            for (p, bnd) in zip(point, self.bounds)
        )
    ###################
    def constraints(self, point):
        L = point[0]
        d = point[1]
        w = point[2]
        first=0
        second=0  
        third=0
        fourth = 0
        if (1-(d**3*L)/(7178*w**4)) <= 0:
            first = 1
        if ((4*d**2-w*d)/(12566*d*w**3-w**4))+(1/(5108*w**2))-1 <= 0:
            second = 1
        if (1-(140.45*w/(d**2*L))) <= 0:
            third =1
        if ((w+d)/1.5-1) <= 0:
            fourth = 1
        return first and second and third and fourth

    """
    Plug the point into the function to find its value at this point
    """
    def score(self, point):
        return self.eval_function(*point)


class Particle:
    """
    This class represents a single particle that will move around the
    search space
    """

    def __init__(self, initial_position, dimension, max_speed, my_function):
        """
        initial_position = starting position of the particle
        dimension = how many dimensions the problem has, e.g. f(x,y,z) is 3
        max_speed = the largest speed the particle is allowed to have
        """
        self.dimension = dimension
        # this uses a big library called "numpy" that does fast vector 
        #   computation

        # library called numpy
        self.position = np.array(initial_position)
        # velocity starts at 0
        self.velocity = np.array([0]*self.dimension)
        # will keep track of best solution seen so far
        self.best_seen = None
        self.max_speed = max_speed
    #####################
        self.func = my_function

    def advance_position(self, global_best, alpha, beta, gamma):
        """
        Moves the particle one step forward by calculating a new velocity
          depending on past velocity, best solution THIS particle has ever
          seen, and best solution ANY particle has ever seen.
        """
        # generate two random vectors r1 and r2
        r1 = np.random.random_sample((self.dimension,))
        r2 = np.random.random_sample((self.dimension,))

        # compute next velocity according to the formula from class
        self.velocity = (
            alpha * self.velocity + 
            beta * r1 * (self.best_seen - self.position) + 
            gamma * r2 * (global_best - self.position)
        )

        # compute the speed of the particle
        # if v is the velocity vector, then speed is its 2-norm:
        #   sqrt(v[0]^2 + v[1]^2 + ...)
        speed = np.linalg.norm(self.velocity)

        # if the particle is going to fast, scale it's velocity vector
        #   down so it's new speed is exactly self.max_speed
        if speed > self.max_speed:
            self.velocity = self.velocity * (self.max_speed/speed)
        # note that this code makes no effort to stop the particle from going
        #  out of bounds, which is bad!
        # TODO: what happens if the particle goes out of bounds?

        ##### First use in bounds to check the first 3 conditions

        ##### Second check the 4 g(L,d,w)


        ############################
        next_position = self.position +self.velocity
        if (self.func.in_bounds(next_position) 
            and self.func.constraints(next_position)):
            #print("YAY")
            #print(next_position)

            # move the particle according to its new velocity
            self.position += self.velocity



    def set_best(self, best, score):
        """
        set "best" with score "score" as the best seen so far
        """
        self.best_seen = best.copy()
        self.best_seen_score = score


class PSOManager:
    """
    This is a class that handles the main PSO routine, including managing
    all of the particles
    """

    def __init__(
        self,
        space,
        dimension,
        N,
        max_speed=0.01,
        alpha=0.9,
        beta=1,
        gamma=1,
        maximization=True
    ):
        """
        space = object representing the problem in this case a ContinuousFunction objec
        dimension = dimension of the problem
        N = number of particles
        maximization = true if maximizing, false if minimizing
        """
        self.space = space
        self.dimension = dimension
        self.N = N
        self.maximization = maximization
        # Create a list of random particles
        self.particles = [
            Particle(space.random(), dimension, max_speed,space)
            for _ in range(N)
        ]
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        self.global_best_sol = None
        self.global_best_score = None
        self.set_global_best()

    def is_better(self, new_score, old_score):
        """
        return if new_score is better than old_score (depends if we're
        maximizing or minimizing)
        """
        if self.maximization:
            return new_score > old_score
        return new_score < old_score

    def set_global_best(self):
        """
        Loops over each particle and computes its score. If it's the best that
        particle has even seen, tells the particle to store it. If it's the best
        any particle has even seen, stores it for itself
        """
        for particle in self.particles:

            score = self.space.score(particle.position)

            if particle.best_seen is None or self.is_better(score, particle.best_seen_score):
                particle.set_best(particle.position, score)

            if (
                self.global_best_score is None
                or
                self.is_better(score, self.global_best_score)
            ):
                self.global_best_score = score
                self.global_best_sol = particle.position.copy()
                print(f"Best score = {self.global_best_score} for sol = {self.global_best_sol}")

        
    def advance(self):
        """
        Moves all the particles, then checks for new best scores
        """

        for particle in self.particles:
            particle.advance_position(self.global_best_sol, self.alpha, self.beta, self.gamma)

        self.set_global_best()

# define the problem we're solving
eval_function = lambda L,d,w: (2+L)*d*w**2
bounds = [[2, 15], [0.25, 1.3], [0.05,2]]
cns_func = ContinuousFunction(eval_function, bounds)

# creates the PSO particle manager
PSO = PSOManager(cns_func, 3, 1000, alpha=0.9, beta=1, gamma=1.2, max_speed=0.5, maximization=False)
gen = 0

while 1:
    gen += 1
    PSO.advance()
    #print(f"Generation {gen}: Best score = {PSO.global_best_score} for sol = {PSO.global_best_sol}")
    