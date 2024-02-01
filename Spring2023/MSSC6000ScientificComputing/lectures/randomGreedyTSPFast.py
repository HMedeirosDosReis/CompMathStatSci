# random solution AND random greedy solution

import math
import random
random.seed(1)

import matplotlib.pyplot as plt  # type: ignore
from matplotlib.widgets import Button  # type: ignore


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


class TSPProblem:
    def __init__(self, points):
        self.points = set(points)

    def random_solution(self):
        return TSPSolution(random.sample(self.points, len(self.points)))

    def random_greedy_solution(self):
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




def randomize_event(plotter, event=None):
    plotter.draw(tsp_problem.random_solution())


points = [(random.random(), random.random()) for _ in range(100)]
tsp_problem = TSPProblem(points)

plt.ion()
fig, (ax, ax2) = plt.subplots(1,2)
# fig2, ax2 = plt.subplots()
(data_line,) = ax2.plot([], [])

plt.subplots_adjust(bottom=0.15)
ax.set_title("Traveling Salesman Demo", fontsize=20)
ax.tick_params(
    which="both", bottom=False, labelbottom=False, left=False, labelleft=False
)
plot = None
text = None
best = None

while True:
    tsp_solution = tsp_problem.random_greedy_solution()

    x_points = [p[0] for p in tsp_solution.points]
    y_points = [p[1] for p in tsp_solution.points]
    length = tsp_solution.path_length()

    previous_line_data = data_line.get_data()
    xdata = list(previous_line_data[0])
    ydata = list(previous_line_data[1])
    xdata.append(len(xdata))
    ydata.append(length)
    data_line.set_data(xdata, ydata)
    ax2.set_xlim((0, len(xdata)))
    ax2.set_ylim((0, max(ydata)))

    if plot is not None:
        plot.remove()
    (plot,) = ax.plot(
        x_points + [x_points[0]],
        y_points + [y_points[0]],
        color="blue",
        marker="s",
        markerfacecolor="black",
        markersize=3,
    )
    props = dict(boxstyle="round", facecolor="blue", alpha=0.5)
    if text is not None:
        text.remove()
    if best is None or best > length:
        best = length
    text = ax.text(
        0,
        -0.05,
        f"Best route length: {best}",
        transform=ax.transAxes,
        fontsize=14,
        verticalalignment="top",
        bbox=props,
    )
    # plt.draw()
    plt.pause(0.0000001)



