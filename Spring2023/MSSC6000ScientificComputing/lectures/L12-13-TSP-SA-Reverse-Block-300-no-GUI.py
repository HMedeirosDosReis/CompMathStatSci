
import math
import random
import itertools
from tqdm import tqdm
random.seed(1)



def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)


class TSPSolution:
    def __init__(self, points):
        self.points = points

    def path_length(self):
        return sum(
            euclidean_distance(self.points[i], self.points[i + 1])
            for i in range(len(self.points) - 1)
        ) + euclidean_distance(self.points[-1], self.points[0])

    def tweak(self):
        indices = sorted(random.sample(list(range(1,len(self.points))), 2))
        p = self.points
        new_points = p[:indices[0]] + p[indices[0]:indices[1]+1][::-1] + p[indices[1]+1:]
        assert len(p) == len(new_points), indices
        return TSPSolution(new_points)

class TSPProblem:
    def __init__(self, points):
        self.points = set(points)

    def random(self):
        return TSPSolution(random.sample(list(self.points), len(self.points)))

    def random_greedy(self):
        start_point = random.choice(list(self.points))
        solution = [start_point]

        points_left = set(self.points)
        points_left.remove(start_point)

        while len(points_left) > 0:
            closest = min(
                points_left, key=lambda p: euclidean_distance(p, solution[-1])
            )
            solution.append(closest)
            points_left.remove(closest)

        return TSPSolution(solution)

    def tweak(self, tour):
        return tour.tweak()

    def score(self, tour):
        return tour.path_length()


class GeometricSimulatedAnnealing:

    def __init__(self, space, alpha, maximization=True):
        self.space = space
        self.maximization = maximization
        self.initial_temp = self.determine_initial_temp()
        self.alpha = alpha
        self.temp = self.initial_temp
        

    def determine_initial_temp(self, trials=1000, initial_prob=0.8):
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


points = [(random.random(), random.random()) for _ in range(300)]
tsp_problem = TSPProblem(points)
alpha = 0.995
final_temp_factor = 0.0001

SA = GeometricSimulatedAnnealing(tsp_problem, alpha, maximization=False)

tour = tsp_problem.random()
value = tsp_problem.score(tour)
best_sol, best_score = tour, value

num_gens = math.ceil(math.log(final_temp_factor)/math.log(alpha))
gen = 0

while SA.temp > final_temp_factor * SA.initial_temp:

    gen += 1
    total = 0
    accept = 0

    for i in range(10000):
        
        new_tour = tsp_problem.tweak(tour)
        new_value = tsp_problem.score(new_tour)

        if SA.is_worse(value, new_value):
            total += 1
        if SA.accept(value, new_value):
            if SA.is_worse(value, new_value):
                accept += 1
            else:
                if new_value < best_score:
                    best_sol = new_tour
                    best_score = new_value
            tour = new_tour
            value = new_value

    print(
        f"gen: {gen}/{num_gens}, "
        f"temp: {SA.temp:.6f}, "
        f"% acc: {accept/total*100:.5f}, "
        f"cur score: {value:.6f}, "
        f"best score: {best_score}, "
    )

    SA.advance_temp()

