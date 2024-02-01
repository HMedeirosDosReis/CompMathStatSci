import itertools
import random

import time

class Job:
	"""
	This class represents a single job, storing its location the list of all jobs [index]
	and its duration, deadline, and profit.
	"""

	def __init__(self, index, duration, deadline, profit):
		self.index = index
		self.duration = duration
		self.deadline = deadline
		self.profit = profit

	def __eq__(self, other):
		return self.index == other.index

	def __repr__(self):
		return f"Job({self.index}, {self.duration}, {self.deadline}, {self.profit})"



class Schedule:
	"""
	A schedule represents a *possible solution* in the search space. It contains a
	variable "self.jobs_done" which is a list of jobs in the order they get done.
	It does *not* represent the full table of all jobs. Just a solution / partial
	solution.
	"""

	def __init__(self, jobs_done, all_jobs):
		self.jobs_done = jobs_done
		self.all_jobs = all_jobs
		self.time_used = None

	def possible(self):
		"""
		returns True if this is schedule is actually possible, meaning each job can be
		finished before the deadline without overlap
		"""
		time = 0
		for job in self.jobs_done:
			time += self.all_jobs[job].duration
			if time > self.all_jobs[job].deadline:
				return False

		self.time_used = time
		return True

	def score(self):
		assert self.possible(), "you are scoring an impossible schedule"
		return sum(self.all_jobs[job].profit for job in self.jobs_done)
	
	def upper_bound(self):
		# TRY NOT CARE ABOUT DEADLINE

		# Sort the remaining jobs by their profit per unit of time
		remaining_jobs = [self.all_jobs[i] for i in range(len(self.all_jobs)) if i not in self.jobs_done]
		remaining_jobs.sort(key=lambda job: job.profit / job.duration, reverse=True)
		
		max_duration = max([job.deadline for job in remaining_jobs]) #AKA capacity

        # Compute the total profit of all the jobs that can be done before their deadline
		time = self.time_used
		max_duration = max_duration-time #AKA capacity
		total_value = 0

		for job in remaining_jobs:
			if job.duration <= max_duration:
				total_value += job.profit
				max_duration -= job.duration
			else:
				fraction = max_duration / job.duration
				total_value += fraction * job.profit
				break
        
		return total_value + self.score()


def branch_and_bound(all_jobs):
	"""
	This calls the function "rec" which is recursive and does all the work.
	"""
	return rec([], all_jobs, 0, [])


def rec(sch, all_jobs, best_score, best_sol):
	"""
	Recursive branch-and-bound function.
	sch = a list of jobs representing the schedule we have built so far
	  (a schedule is a selection of jobs to do in a particular order)
	all_jobs = a list of Job objects represnrint all possible jobs
	best_score = highest profit seen so far
	best_sol = best schedule seen so far
	"""

	# turn sch into a Schedule object and make sure it's still possible
	# "assert" means "this should be true", and they are a useful way to notice bugs
	S = Schedule(sch, all_jobs)
	assert S.possible()

	# branching -> which jobs could be scheduled next?
	# any job that has not been done already, and could still be done before the deadline
	next_jobs = [
			job for job in all_jobs
			if (
				job.index not in sch
				and
				job.duration + S.time_used <= job.deadline
			)
		]
	
	# if no more jobs are possible this is a base case
	if len(next_jobs) == 0:
		s_score = S.score()
		if best_score >= s_score:
			return best_score, best_sol
		else:
			return s_score, sch

	# if some jobs CAN still be done, compute and upper bound
	# if that upper bound is not bigger than the best score seen so far,
	#   prune this branch (don't recursively keep looking, just return)
	if S.upper_bound() <= best_score:
		return best_score, best_sol

	# otherwise, for each possibel next job, add it to a copy of the
	# schedule, and recursively continue down each branch
	for nj in next_jobs:
		new_sch = sch + [nj.index]
		rec_score, rec_sol = rec(new_sch, all_jobs, best_score, best_sol)
		if rec_score > best_score:
			best_score, best_sol = rec_score, rec_sol

	return best_score, best_sol


def search_space(n):
	return itertools.chain.from_iterable(
		itertools.permutations(subset)
		for k in range(n+1)
		for subset in itertools.combinations(range(n),k)
	)

def jobs_brute_force(all_jobs):
	"""
	compute the best score and best solution using brute force
	all_jobs = list of Job objects
	"""
	space = search_space(len(all_jobs))
	best_score, best_sol = 0, []
	for sol in space:
		S = Schedule(sol, all_jobs)
		if S.possible():
			score = S.score()
			if score > best_score:
				best_score, best_sol = score, list(sol)

	return best_score, best_sol

def random_jobs(n):
	jobs = [Job(i, random.randint(1,n//2), random.randint(1,n+1), random.randint(1, n)) for i in range(n)]
	return jobs


all_jobs = [Job(0, 19, 3, 28), Job(1, 16, 37, 1), Job(2, 7, 30, 32), Job(3, 9, 42, 11), Job(4, 2, 34, 32), Job(5, 11, 5, 16), Job(6, 24, 24, 3), Job(7, 14, 9, 39), Job(8, 12, 25, 27), Job(9, 10, 44, 17), Job(10, 15, 12, 44), Job(11, 10, 43, 24), Job(12, 5, 30, 50), Job(13, 8, 29, 40), Job(14, 13, 3, 38), Job(15, 1, 16, 9), Job(16, 7, 20, 35), Job(17, 12, 50, 16), Job(18, 11, 43, 36), Job(19, 15, 28, 31), Job(20, 3, 42, 38), Job(21, 11, 33, 11), Job(22, 8, 27, 16), Job(23, 2, 3, 32), Job(24, 10, 39, 43), Job(25, 3, 35, 6), Job(26, 5, 25, 37), Job(27, 12, 39, 10), Job(28, 4, 50, 50), Job(29, 4, 29, 11), Job(30, 7, 23, 28), Job(31, 14, 29, 16), Job(32, 22, 18, 10), Job(33, 20, 34, 12), Job(34, 4, 18, 30), Job(35, 10, 11, 43), Job(36, 21, 12, 50), Job(37, 6, 31, 50), Job(38, 12, 21, 28), Job(39, 8, 1, 35), Job(40, 23, 3, 22), Job(41, 11, 16, 6), Job(42, 9, 29, 26), Job(43, 19, 11, 25), Job(44, 16, 44, 16), Job(45, 24, 34, 18), Job(46, 17, 31, 39), Job(47, 16, 5, 11), Job(48, 16, 44, 30), Job(49, 13, 9, 27)]
n=27
my_jobs = all_jobs[:n]
#my_jobs = random_jobs(n)
t = time.time()
sol = branch_and_bound(my_jobs)
print(sol)
#sol = jobs_brute_force(my_jobs)
print(sol)
print("--- %s seconds ---" % (time.time() - t))
