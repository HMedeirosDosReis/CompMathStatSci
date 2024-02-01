#!/usr/bin/env python3

# Henri Medeiros Dos Reis
# 4/24/2023

# 2- Graph partitioning problem 

import itertools
import random
import json
import math

class Graph:
	"""
	represents an undirected simple graph
	n = number of vertices
	we consider the vertices labeled 1 through n
	edges = list(/set/tuple) of pairs of vertices that are connected,
		order irrelevant
	"""

	def __init__(self, n, edges):
		self.n = n
		self.edges = set(frozenset(e) for e in edges)
		# Also save the vertices
		self.vertices = set([i for i in range(n)])

		# now we do some checks to make sure the edges make sense
		assert all(len(e) == 2 for e in self.edges),\
			"all edges must have two distinct vertices"
		assert all(all(v <= self.n and v >= 1 for v in e) for e in self.edges),\
			"an edge has an illegal vertex label"

	def unpenalized_score(self, part1):
		"""
		part1 is a subset of vertex labels (can be list/tuple/set, etc)

		returns the number of edges that have one vertex in part1
		and one vertex not in part1
		"""
		assert len(part1) * 2 == self.n,\
			"this unpenalized_score only makes sense when part1 is half the size of the graph"
		part_set = frozenset(part1)
		return -sum(1 for e in self.edges if len(e.intersection(part_set)) == 1)

def random_graph(n, p):
	"""
	generates a random graph on n vertices. each possible edge exists
	with independent probability p
	"""
	edges = []
	for v1 in range(1, n+1):
		for v2 in range(v1+1, n+1):
			if random.random() <= p:
				edges.append([v1, v2])
	return Graph(n, edges)

def brute_force(G):
	"""
	compute a brute force solution by iterating over all ways of splitting
	the vertices into two equally sized subsets
	"""
	n = G.n
	assert n % 2 == 0,\
		"this problem requires graphs with an even number of vertices"
	best_sol = None
	best_unpenalized_score = None

	vertices = list(range(1, n))
	for part1 in itertools.combinations(vertices, n//2):
		unpenalized_score = G.unpenalized_score(part1)
		if best_unpenalized_score is None or best_unpenalized_score > unpenalized_score:
			best_sol = part1
			best_unpenalized_score = unpenalized_score

	return best_sol

def graph_to_file(G, file_name):
	with open(file_name, "w") as f:
		f.write(str(G.n)+"\n")
		f.write(json.dumps(tuple(map(tuple,G.edges))))

def read_graph(file_name):
	with open(file_name, "r") as f:
		n = int(f.readline().strip())
		edges = json.loads(f.readline().strip())
		return Graph(n, edges)
	

def tweak(sol, compliment):
	"""
	Takes in the best solution and the compliment of that solution,
	returns a tweaked version of the solution.
	"""

	copy_sol = set(sol)
	copy_c = set(compliment)

	# Select a random element from the solution and remove it
	random_element = random.choice(tuple(copy_sol))
	copy_sol.remove(random_element)
	
	# Select a random element from the compliment and remove it
	other_random_element = random.choice(tuple(copy_c))
	copy_c.remove(other_random_element)

	# Swap the random elements between the sets
	copy_sol.add(other_random_element)
	copy_c.add(random_element)
	return copy_sol
   

def random_sol(V):
	"""
	Creates a split of the set of vertices
	"""
	my_vertices = V.vertices
	n1 = len(my_vertices) // 2

	new_set = set(random.sample(sorted(my_vertices), n1))

	return new_set

def determine_initial_temp(graph, trials=100, initial_prob=0.96):
	"""
	Returns the initial temperature of the system to have 100 trials with
	probability of 96%. It takes as parameter only the graph.  
	"""
	total_change = 0
	decreases = 0
	tried = 0
	while decreases < trials:
		tried += 1
		sol = random_sol(graph)
		compl = graph.edges - sol
		new_sol = tweak(sol, compl)
		diff = -(graph.unpenalized_score(new_sol) - graph.unpenalized_score(sol))
		if diff < 0:
			decreases += 1
			total_change += diff
	avg_change = total_change / trials
	return avg_change / math.log(initial_prob)

def SA(graph, initial_temp, alpha, final_temp, trials_per_temp,num_gens):
	"""
	Actual simulated annealing method. 

	Takes as input, the graph, initial temperature, change in temperature(alpha),
	how many trials per temperature, and how many generations to run.

	Returns the best sol
	"""

	# Initialize variables
	temp = initial_temp
	generation = 0
	x = random_sol(graph)
	best_sol = x

	# While we are "hot"
	while temp >= final_temp:
		generation += 1
		accepted_worse = 0
		total_worse = 0
		# Loop through the number of specified trials
		for i in range(trials_per_temp):
			# Tweak and store the solution
			compl = graph.vertices -x
			s = tweak(x, compl)
			diff_unpenalized_score = graph.unpenalized_score(s) - graph.unpenalized_score(x)
			# Is the tweak solution better?
			if diff_unpenalized_score>0:
				x = s
				# Is it better than the best?
				if graph.unpenalized_score(x) > graph.unpenalized_score(best_sol):
					best_sol = x
			else:
				# We are worse
				total_worse += 1
				p = math.exp(diff_unpenalized_score/temp)
				r = random.random()
				# Should I accept?
				if r <= p:
					accepted_worse += 1 
					x = s

		print(
			f"gen: {generation}/{num_gens}, "
			f"temp: {temp:.6f}, "
			f"% acc: {accepted_worse/total_worse*100:.5f}, "
			f"cur unpenalized_score: {-graph.unpenalized_score(x):.2f}, "
			f"best unpenalized_score: {-graph.unpenalized_score(best_sol)}, "
		)
		temp *= alpha
	return(best_sol, graph.unpenalized_score(best_sol))


locs = [70, 873, 607, 85, 119, 856, 485, 738, 807, 321, 791, 58, 790, 628, 717, 387, 768, 924, 844, 50, 138, 840, 923, 830, 498, 284, 553, 609, 293, 171, 499, 42, 892, 926, 489, 795, 514, 67, 439, 480, 883, 600, 163, 365, 528, 682, 704, 15, 890, 534, 472, 374, 373, 342, 668, 619, 681, 781, 645, 578, 356, 266, 737, 145, 800, 281, 651, 824, 277, 496, 380, 199, 980, 770, 683, 421, 894, 93, 616, 961, 778, 307, 949, 232, 235, 107, 713, 280, 995, 690, 828, 279, 194, 451, 637, 245, 7, 940, 221, 352, 864, 383, 8, 405, 243, 881, 306, 835, 252, 53, 941, 366, 732, 788, 740, 897, 630, 466, 925, 490, 103, 301, 943, 102, 833, 435, 812, 708, 6, 361, 379, 101, 957, 625, 838, 882, 902, 734, 43, 642, 251, 183, 268, 213, 772, 541, 507, 842, 686, 32, 746, 22, 742, 797, 726, 965, 170, 853, 718, 1000, 424, 453, 702, 536, 137, 928, 89, 906, 122, 77, 754, 636, 10, 316, 184, 448, 855, 688, 664, 771, 845, 423, 186, 265, 433, 314, 401, 970, 1, 908, 577, 347, 546, 65, 469, 621, 323, 354, 98, 311, 35, 11, 643, 629, 295, 847, 240, 52, 13, 978, 695, 229, 996, 693, 663, 786, 727, 94, 653, 99, 743, 154, 464, 904, 128, 880, 156, 180, 513, 81, 662, 113, 826, 384, 381, 477, 332, 218, 75, 108, 979, 428, 985, 135, 744, 447, 893, 829, 580, 444, 935, 665, 505, 821, 446, 222, 440, 652, 497, 762, 544, 626, 590, 567, 623, 112, 117, 792, 305, 188, 591, 396, 289, 205, 574, 364, 337, 172, 129, 910, 931, 495, 885, 173, 201, 660, 945, 457, 599, 658, 963, 519, 557, 187, 335, 638, 647, 836, 959, 460, 334, 582, 823, 263, 33, 302, 839, 552, 761, 679, 430, 670, 707, 31, 948, 255, 443, 780, 233, 521, 372, 916, 608, 937, 9, 456, 620, 562, 537, 535, 764, 481, 857, 569, 719, 939, 445, 17, 59, 300, 715, 51, 271, 47, 747, 264, 516, 238, 220, 142, 141, 675, 468, 818, 784, 523, 710, 736, 532, 292, 272, 518, 178, 914, 692, 677, 563, 816, 777, 705, 699, 849, 418, 962, 432, 193, 542, 549, 872, 317, 815, 603, 822, 483, 106, 586, 756, 529, 179, 239, 879, 328, 905, 79, 168, 287, 969, 310, 841, 208, 40, 545, 62, 143, 714, 572, 64, 389, 198, 80, 596, 993, 304, 915, 393, 987, 55, 753, 848, 197, 426, 997, 458, 522, 725, 901, 547, 333, 749, 831, 850, 391, 234, 248, 133, 869, 217, 325, 763, 952, 640, 809, 868, 149, 246, 942, 91, 487, 966, 431, 260, 801, 25, 861, 597, 41, 318, 579, 392, 74, 862, 242, 673, 308, 865, 946, 972, 568, 226, 509, 960, 341, 200, 846, 158, 369, 134, 735, 968, 799, 700, 86, 407, 303, 72, 494, 371, 654, 656, 429, 274, 210, 438, 147, 775, 345, 606, 661, 157, 121]
graph = read_graph("graph-1000-0p01.txt")
print(graph.unpenalized_score(locs))


alpha = 0.96
initial_temp = determine_initial_temp(graph)
final_temp_fact = 10e-8
final_temp = final_temp_fact * initial_temp
num_gens = math.ceil(math.log(final_temp_fact)/math.log(alpha))

#def SA(graph, initial_temp, alpha, final_temp, trials_per_temp,num_gens):
my_solution = SA(graph, initial_temp, alpha, final_temp, 100,num_gens)
print(my_solution)

