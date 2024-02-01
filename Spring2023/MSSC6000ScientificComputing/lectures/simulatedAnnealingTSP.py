# random solution AND random greedy solution

import math
import random
import itertools
from tqdm import tqdm
random.seed(1)

import matplotlib.pyplot as plt  # type: ignore


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
        

    def determine_initial_temp(self, trials=1000, initial_prob=0.5):
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


class TSPPlotter:
    """
    3D funtions only
    """

    def __init__(self):
        plt.ion()
        plt.style.use('ggplot')
        self.fig, ((self.ax_tour, self.ax_score), (self.ax_temp, self.ax_accept)) = plt.subplots(2,2)

        self.score_line, = self.ax_score.plot([], [])
        self.score_values = []
        self.score_x = []

        self.ax_tour.tick_params(
            which="both", bottom=False, labelbottom=False, left=False, labelleft=False
        )
        self.tour_plot = None

        self.best = None

        self.temp_line, = self.ax_temp.plot([], [], linestyle='-', marker='.', color='blue')
        self.temps = []

        self.accept_line, = self.ax_accept.plot([], [], linestyle='-', marker='.', color='green')
        self.accepts = []
        self.ax_accept.set_ylim((0, 1))


        plt.subplots_adjust(bottom=0.15)
        self.ax_tour.set_title("Tour", fontsize=20)
        self.ax_score.set_title("Value", fontsize=20)
        self.ax_temp.set_title("Temperature", fontsize=20)
        self.ax_accept.set_title("% Worsenings Accepted", fontsize=20)
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

        plt.pause(0.0001)

    def show_tour(self, tsp_solution, update_plot=True):

        if update_plot:
            x_points = [p[0] for p in tsp_solution.points]
            x_points.append(x_points[0])

            y_points = [p[1] for p in tsp_solution.points]
            y_points.append(y_points[0])

            if self.tour_plot is not None:
                self.tour_plot.remove()
            (self.tour_plot,) =self.ax_tour.plot(
                x_points + [x_points[0]],
                y_points + [y_points[0]],
                color="blue",
                marker="s",
                markerfacecolor="black",
                markersize=3,
            )

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


    def add_to_temp_line(self, temp):
        self.temps.append(temp)
        self.temp_line.set_data(range(len(self.temps)), self.temps)

        cur_x = self.ax_temp.get_xlim()
        cur_y = self.ax_temp.get_ylim()

        if len(self.temps) > cur_x[1]:
            self.ax_temp.set_xlim((0, cur_x[1] + 10))
        if max(self.temps) > cur_y[1]:
            self.ax_temp.set_ylim((0, max(self.temps)))


    def add_to_accept_line(self, accept):
        self.accepts.append(accept)
        self.accept_line.set_data(range(len(self.accepts)), self.accepts)

        cur_x = self.ax_accept.get_xlim()
        if len(self.accepts) > cur_x[1]:
            self.ax_accept.set_xlim((0, cur_x[1] + 10))

                      
    def update_best(self, value):
        if (
            self.best is None
            or value < self.best
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


points = [(random.random(), random.random()) for _ in range(100)]
tsp_problem = TSPProblem(points)

plotter = TSPPlotter()

SA = GeometricSimulatedAnnealing(tsp_problem, 0.995, maximization=False)

tour = tsp_problem.random()
value = tsp_problem.score(tour)

while SA.temp > 0.0005 * SA.initial_temp:

    plotter.add_to_temp_line(SA.temp)
    
    total = 0
    accept = 0

    for i in range(1000):
        
        update_plot = (i % 1000 == 0)

        plotter.show_tour(tour, update_plot=update_plot)
        plotter.update_best(value)
        plotter.add_to_score_line(value, update_plot=update_plot)

        if update_plot:
            plt.pause(0.00001)

        new_tour = tsp_problem.tweak(tour)
        new_value = tsp_problem.score(new_tour)

        if SA.is_worse(value, new_value):
            total += 1
        if SA.accept(value, new_value):
            if SA.is_worse(value, new_value):
                accept += 1
            tour = new_tour
            value = new_value

    plotter.add_to_accept_line(accept/total)
    print(SA.temp,plotter.best)
    SA.advance_temp()

plt.show(block=True)
