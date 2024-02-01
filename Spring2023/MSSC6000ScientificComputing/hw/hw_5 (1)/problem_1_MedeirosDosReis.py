# Henri Medeiros Dos Reis
# 4/24/2023

# 1 - Blue lights problem 


import itertools
import json
import math
import random

class Campus:
	"""
	represents a campus of buildings
	buildings = set of tuples of x,y-coordinates

	for example: Campus([(0.5, 0.2), (0.1, 0.35), (0.75, 0.75)])
	"""
	def __init__(self, buildings):
		self.buildings = set(buildings)

	def score(self, light_locs):
		"""
		light_locs is a set/list of tuples with x,y-points
		for example: C.score([(0.5, 0.5), (0.2, 0.1)])
		"""
		# Since we are minimizing in this problem, return the negative of the sum
		return -sum(
			min(
				euc_dist(building, light)
				for light in light_locs
			)
			for building in self.buildings
		)


def random_campus(N):
	"""
	creates a random campus with N buildings
	"""
	return Campus([(random.random(), random.random()) for _ in range(N)])

def euc_dist(p1, p2):
	"""
	calculates the Euclidean distance between two points
	"""
	# print("p1:",p1,"p2:",p2)
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def campus_to_file(C, file_name):
	"""
	stores the given campus in a file
	"""
	with open(file_name, "w") as f:	    
		f.write(json.dumps(tuple(C.buildings)))

def read_campus(file_name):
	"""
	reads the given file and returns a Campus object
	"""
	with open(file_name, "r") as f:
		buildings = set(map(tuple,json.loads(f.readline().strip())))
		return Campus(buildings)
	
def tweak(sol, tweak_delta):
	"""
	Takes in a solution and how much to tweak it by, returns a new solution
	"""

	delta = tweak_delta
	# Choose one light to tweak
	light_to_tweak = random.randint(0, len(sol)-1)

	new_point = [coord+ 
	      delta * (2 * random.random() - 1) for coord in sol[light_to_tweak]]
	# Make sure we are in bound
	while not in_bounds(new_point):
		new_point = [coord + 
	      delta * (2 * random.random() - 1) for coord in sol[light_to_tweak]]
	
	# Update and return new_sol
	new_sol = list(sol)
	new_sol[light_to_tweak] = new_point
	return new_sol
   
def in_bounds(point):
	"""
    Checks if the given cartesian point (x, y) is inside the square with corners (0, 0) and (1, 1).
    Returns True if the point is inside the square, False otherwise.
    """
	if 0 <= point[0] <= 1 and 0 <= point[1] <= 1:
		return True
	else:
		return False

def random_lights(N):
	"""
	creates a random campus with N buildings
	"""
	return [(random.random(), random.random()) for _ in range(N)]

def determine_initial_temp(ligths, campus, trials=1000, initial_prob=0.96):
	"""
	Returns the initial temperature of the system to have 100 trials with
	probability of 96%. It takes as parameters, the number of ligths and 
	the campus. 
	"""
	total_change = 0
	decreases = 0
	tried = 0

	while decreases < trials:
		tried += 1
		sol = random_lights(ligths)
		new_sol = tweak(sol,0.01)
		diff = -(campus.score(new_sol) - campus.score(sol))
		if diff < 0:
			decreases += 1
			total_change += diff
	avg_change = total_change / trials
	return avg_change / math.log(initial_prob)

def SA(campus, initial_temp, alpha, final_temp, trials_per_temp, k,delta,num_gens):
	"""
	Actual simulated annealing method. 

	Takes as input, the campus, initial temperature, change in temperature(alpha),
	how many trials per temperature, number of lights (k), how much to tweak the 
	solution (delta), and how many generations to run.

	Returns the best sol
	"""

	# Initialize variables
	temp = initial_temp
	generation = 0
	x = random_lights(k)
	best_sol = x

	# While we are "hot"
	while temp >= final_temp:
		generation += 1
		accepted_worse = 0
		total_worse = 0
		# Loop through the number of specified trials
		for i in range(trials_per_temp):
			# Tweak and store the solution
			s = tweak(x, delta)
			diff_score = campus.score(s) - campus.score(x)
			# Is the tweak solution better?
			if diff_score>0:
				x = s
				# Is it better than the best?
				if campus.score(x) > campus.score(best_sol):
					best_sol = x
			else:
				# We are worse
				total_worse += 1
				p = math.exp(diff_score/temp)
				r = random.random()
				# Should I accept?
				if r <= p:
					accepted_worse += 1 
					x = s

		print(
			f"gen: {generation}/{num_gens}, "
			f"temp: {temp:.6f}, "
			f"% acc: {accepted_worse/total_worse*100:.5f}, "
			f"cur score: {-campus.score(x):.2f}, "
			f"best score: {-campus.score(best_sol)}, "
		)
		temp *= alpha
		# make smaller tweaks, as the number of generations go by
	return(best_sol)



locs = [[0.49852367041951934, 0.47281676837201414], [0.45219737933804754, 0.14774968720832407], [0.3717712020628129, 0.8150855123966199], [0.8686859832446606, 0.489885749036388], [0.144598332469227, 0.2238261973605511], [0.7537208986790759, 0.1441197207856418], [0.09270959156399691, 0.6405371166292089], [0.7665387275367724, 0.7843663845523087], [0.33922770603700036, 0.47005680234961855], [0.13547913452044177, 0.05938590932742994]]
campus = read_campus("campus.txt")
print(campus.score(locs))


lig = 10 # We have 10 lights 
alpha = 0.98 # Lets "cool down" by 0.96
initial_temp = determine_initial_temp(lig, campus) 
final_temp_fact = 10e-8 
final_temp = final_temp_fact * initial_temp
num_gens = math.ceil(math.log(final_temp_fact)/math.log(alpha))

#SA(campus,              initial_temp, alpha, final_temp, trials_per_temp, k,delta,num_gens):
my_solution = SA(campus, initial_temp, alpha, final_temp, 1000, lig, 0.01,num_gens)
print(my_solution)


