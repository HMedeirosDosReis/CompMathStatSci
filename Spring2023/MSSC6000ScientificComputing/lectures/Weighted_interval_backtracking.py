"""
    Backtracking solution to weighted interval scheduling.

    I've set the requests have length >= 5 to make things a little faster and avoid
    the trivial cases of a bunch of length 1 requests

    "build" can handle 200 requests within a few seconds
"""

import random
from itertools import chain, combinations

from tqdm import tqdm

# return the powerset of the input
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

# generate one random request with start/end in the set [0, 1, ..., 9]
#   and value a uniform real number between 0 and 10
# repeatedly re-randomizes until meeting lasts at least 5 minutes
def random_request():
    req = [sorted(random.sample(range(100), 2)), random.random() * 10]
    while req[0][1] - req[0][0] < 5:
        req = [sorted(random.sample(range(100), 2)), random.random() * 10]
    return req

# generate n random requests
def make_requests(n):
    return [random_request() for i in range(n)]

# return a boolean for whether the meetings r1 and r2 are compatible
#  (True = are compatible = don't overlap)
def compatible(r1, r2):
    return r2[0][1] <= r1[0][0] or r2[0][0] >= r1[0][1]

# return a boolean for whether "request" is compatible with EVERY
#   request in the list "solution"
def is_compatible(request, solution):
    r = request
    return all(compatible(r, s) for s in solution)

# checks whether "solution" is valid, meaning there are no two overlapping
#   requests. This is slow!
def valid_solution(solution):
    return all(
        is_compatible(solution[i], solution[i + 1 :]) for i in range(len(solution) - 1)
    )

# compute the total value of all meetings in "solution"
def score(solution):
    return sum(r[1] for r in solution)

# plot a set of requests
def plot_requests(requests):
    for r in sorted(requests, key=lambda x: x[0][1]):
        print(
            " " * (r[0][0])
            + "-" * (r[0][1] - r[0][0])
            + "   ("
            + str(round(r[1], 2))
            + ")"
        )

# greedy solution from previous code
def greedy(requests, sort_key):
    sorted_requests = sorted(requests, key=sort_key)  # O(n*log(n))
    solution = []
    solution.append(sorted_requests.pop(0))

    while len(sorted_requests) > 0:  # O(n)
        request = sorted_requests.pop(0)
        if is_compatible(request, solution):
            solution.append(request)

    return solution


shortest = lambda x: x[0][1] - x[0][0]
most_value = lambda x: -x[1]
density = lambda x: -(x[1]) / (x[0][1] - x[0][0])


# brute force solution, slow!
def brute_force(requests):
    all_poss = powerset(requests)
    best_score = 0
    best_sol = []
    # loop over all subsets of meetings
    for sol in tqdm(all_poss, total=2 ** len(requests)):
        if not valid_solution(sol):
            continue
        # if solution has no overlaps, compute its score
        sc = score(sol)
        # if score is a new record, save it
        if sc > best_score:
            best_score = sc
            best_sol = sol
    return best_sol


# to help you write recursive functions, always plan out
#   SUPER explicitly what the inputs and outputs are
# input:
#   remaining_requests: list of remaining requests to choose from
#                 (at the start, all requests are remaining)
# output:
#   the best solution using just "remaining_requests" 
def backtracking(remaining_requests):
    """
    find next valid requests
    add it or not, return which of those leads to the largest score
    if no other valid requests, just return score
    """

    # make a copy so we don't mess things up when we pop!
    # SUPER IMPORTANT
    rr = list(remaining_requests)

    if not rr:
        return []

    # take the first request
    # we are going to try (1) to accept it, and (2) to reject it, recursively
    #   solve both versions, and keep which one is better
    to_add = rr.pop(0)

    # find requests compatible with "to_add"
    remaining_valid_requests = [
        req for req in rr if compatible(to_add, req)
    ]
    # recursively compute best solution using "to_add"
    version_accept = [to_add] + backtracking(remaining_valid_requests)

    # recursively compute best solution not using "to_add"
    version_reject = backtracking(rr)

    # return the one that is the max, using the "score" function as
    # the way of assigning value (this is like using "key" when sorting)
    return max([version_accept, version_reject], key=score)
