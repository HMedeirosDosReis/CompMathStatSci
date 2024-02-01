# optimal score ~ 0.673667521146854727506485226470

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

    # def tweak(self, point):
    #     delta = self.tweak_delta

    #     new_point = [coord + delta * (2 * random.random() - 1) for coord in point]
    #     while not self.in_bounds(new_point):
    #         new_point = [coord + delta * (2 * random.random() - 1) for coord in point]
    #     return new_point

    def score(self, point):
        return self.eval_function(*point)


class Particle:

    def __init__(self, initial_position, dimension, max_speed):
        self.dimension = dimension
        self.position = np.array(initial_position)
        self.velocity = np.array([0]*self.dimension)
        self.best_seen = None
        self.max_speed = max_speed

    def advance_position(self, global_best, alpha, beta, gamma):
        r1 = np.random.random_sample((self.dimension,))
        r2 = np.random.random_sample((self.dimension,))

        # debug = True
        # print(f"best_seen: {self.best_seen}")
        # print(f"best score: {self.best_seen_score}")

        # if debug:
        #     print(f"position: {self.position}")
        #     print(f"velocity: {self.velocity}")
        #     print(f"r1: {r1}")
        #     print(f"r2: {r2}")
        #     print(f"alpha: {alpha}")
        #     print(f"beta: {beta}")
        #     print(f"gamma: {gamma}")
        #     print(f"best_seen: {self.best_seen}")
        #     print(f"self.best_seen - self.position: {self.best_seen - self.position}")
        #     print(f"global_best: {global_best}")
        #     print(f"(global_best - self.position): {(global_best - self.position)}")

        self.velocity = (
            alpha * self.velocity + 
            beta * r1 * (self.best_seen - self.position) + 
            gamma * r2 * (global_best - self.position)
        )
        # if debug:
        #     print(f"velocity: {self.velocity}")
        speed = np.linalg.norm(self.velocity)
        # if debug:
        #     print(f"speed: {speed}")
        if speed > self.max_speed:
            self.velocity *= self.max_speed/speed
        # if debug:
        #     print(f"velocity: {self.velocity}")


        self.position += self.velocity
        # if debug:
        #     print(f"position: {self.position}")
        #     print("="*50)

    def set_best(self, best, score):
        # print(f"called with best = {best} and score = {score}")
        self.best_seen = best.copy()
        self.best_seen_score = score


class PSOManager:

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
        self.space = space
        self.dimension = dimension
        self.N = N
        self.maximization = maximization
        # self.max_speed = max_speed
        self.particles = [
            Particle(space.random(), dimension, max_speed)
            for _ in range(N)
        ]
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        self.global_best_sol = None
        self.global_best_score = None
        self.set_global_best()

    def is_better(self, new_score, old_score):
        if self.maximization:
            return new_score > old_score
        return new_score < old_score

    def set_global_best(self):
        for particle in self.particles:

            score = self.space.score(particle.position)

            # if particle.best_seen is not None:
                # print(f"is_better({score}, {particle.best_seen_score}): {self.is_better(score, particle.best_seen_score)}")
            if particle.best_seen is None or self.is_better(score, particle.best_seen_score):
                particle.set_best(particle.position, score)

            if (
                self.global_best_score is None
                or
                self.is_better(score, self.global_best_score)
            ):
                # print(f"old/new global best score: {self.global_best_score} / {score}")
                self.global_best_score = score
                self.global_best_sol = particle.position.copy()

        
    def advance(self):

        # debug = True
        for particle in self.particles:
            particle.advance_position(self.global_best_sol, self.alpha, self.beta, self.gamma)
            # debug=False
            # new_score = self.space.score(particle.position)
            # old_best_score = self.space.score(particle.best_seen)
            # if self.is_better(new_score, old_best_score):
            #     particle.set_best(particle.position)

        self.set_global_best()
        # print(f"global best score: {self.global_best_score}")
        # print(f"global best sol: {self.global_best_sol}")

        # print("~|"*50+"~")


class ContinuousOptimizationPlotter:
    """
    3D funtions only
    """

    def __init__(self, contour_grids, levels=None, maximization=True):
        plt.ion()
        plt.style.use('ggplot')
        self.fig, (self.ax_contour, self.ax_score) = plt.subplots(1,2)

        self.score_line, = self.ax_score.plot([], [])
        self.score_values = []
        self.score_x = []

        self.explore_line, = self.ax_contour.plot([], [], linestyle='', marker='o', color='red')
        self.explored_points = []
        self.best = None

        plt.subplots_adjust(bottom=0.15)
        self.ax_contour.set_title("Contour Plot", fontsize=20)
        self.ax_score.set_title("Value", fontsize=20)
        plt.show(block=False)

        self.props = dict(boxstyle="round", facecolor="blue", alpha=0.5)
        self.text = self.ax_score.text(
            0,
            -0.1,
            f"Best Score: {self.best}",
            transform=self.ax_score.transAxes,
            fontsize=14,
            verticalalignment="top",
            bbox=self.props,
        )

        X, Y, Z = contour_grids
        if levels is None:
            self.ax_contour.contour(X, Y, Z)
        else:
            self.ax_contour.contour(X, Y, Z, levels=levels)

        self.maximization = maximization

        plt.pause(0.0001)

    @staticmethod
    def points_to_xy(points):
        x_points = [pt[0] for pt in points]
        y_points = [pt[1] for pt in points]
        return x_points, y_points

    def update_particles(self, particles, update_plot=True):
        if update_plot:
            self.explore_line.set_data(*self.points_to_xy([p.position for p in particles]))
            # print([p.position for p in particles])

    def add_to_score_line(self, value, update_plot=True):
        self.score_values.append(value)

        if len(self.score_x) == 0:
            self.score_x.append(0)
        else:
            self.score_x.append(self.score_x[-1]+1)

        if len(self.score_values) > 10000:
            self.score_values.pop(0)
            self.score_x.pop(0)

        if update_plot:

            self.score_line.set_data(self.score_x, self.score_values)
            cur_x = self.ax_score.get_xlim()
            cur_y = self.ax_score.get_ylim()

            if self.score_x[-1] > cur_x[1]:
                self.ax_score.set_xlim((self.score_x[0], self.score_x[-1]))
            if max(self.score_values) > cur_y[1] or min(self.score_values) < cur_y[0]:
                self.ax_score.set_ylim((min(0, min(self.score_values)), max(self.score_values)))
                      
    def update_best(self, value):
        if (
            self.best is None
            or (self.maximization and value > self.best)
            or ((not self.maximization) and value < self.best)
        ):
            self.best = value
            self.text.remove()
            self.text = self.ax_score.text(
                0,
                -0.05,
                f"Best Score: {self.best}",
                transform=self.ax_score.transAxes,
                fontsize=14,
                verticalalignment="top",
                bbox=self.props,
            )




grid_delta = 0.01
tp = 2 * math.pi
x = np.arange(-tp, tp, grid_delta)
y = np.arange(-tp, tp, grid_delta)
X, Y = np.meshgrid(x, y)
Z = np.sin(X-Y)**2 * np.sin(X+Y)**2 / np.sqrt(X**2 + Y**2)
levels = np.arange(0, 0.7, 0.03)

plotter = ContinuousOptimizationPlotter([X, Y, Z], levels, maximization=True)

eval_function = lambda x,y: math.sin(x-y)**2 * math.sin(x+y)**2 / math.sqrt(x**2 + y**2)
bounds = [[-tp, tp]]*2
tweak_delta = 0.1
cns_func = ContinuousFunction(eval_function, bounds, tweak_delta)

PSO = PSOManager(cns_func, 2, 100, alpha=0.9, beta=0.5, gamma=1.5, max_speed=0.1, maximization=True)
gen = 0

while True:
    gen += 1
    # print(gen)
    current_scores = [cns_func.score(part.position) for part in PSO.particles]

    plotter.update_particles(PSO.particles)
    plotter.add_to_score_line(max(current_scores))
    plotter.update_best(PSO.global_best_score)
    plt.pause(0.07)

    PSO.advance()
    # if gen == 10:
        # break

plt.show(block=True)