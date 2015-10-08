from binary_heap import BHeap
import math
import pdb

infinity = 1000000 

def heuristic(a,b):
	return abs(b.x-a.x) + abs(b.y-a.y)

def get_neighbors(cell,grid):
	# Retrieves all un-blocked neighbors
	size = len(grid)

	i = cell.x
	j = cell.y

	# Get initial neighbors list
	if i == 0 and j == 0:
		neighbors = [grid[i+1][j],grid[i][j+1]]
	elif i == 0 and j == size-1:
		neighbors = [grid[i][j-1],grid[i+1][j]]
	elif i == size-1 and j == size-1:
		neighbors = [grid[i-1][j],grid[i][j-1]]
	elif i == size-1 and j == 0:
		neighbors = [grid[i-1][j],grid[i][j+1]]
	elif i == 0:
		neighbors = [grid[i][j-1],grid[i][j+1],grid[i+1][j]]
	elif i == size-1:
		neighbors = [grid[i][j-1],grid[i][j+1],grid[i-1][j]]
	elif j == 0:
		neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j+1]]
	elif j == size-1:
		neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1]]
	else:
		neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]]

	blocked = list()

	for item in neighbors:
		if item.status == 'b':
			blocked.append(item)

	for item in blocked:
		neighbors.remove(item)

	return neighbors

def init_grid(grid):	
	size = len(grid)

	for i in range(0,size):
		for j in range(0,size):
			grid[i][j].search_val = 0

def in_closed_list(closed_list,cell):
	for item in closed_list:
		if cell.equals(item):
			return True

	return False

def print_closed_list(closed_list):
	for i in range(1,len(closed_list)):
			print "({0},{1}) -> {2}".format(closed_list[i].x,closed_list[i].y,closed_list[i].f_val)

def a_star(start,goal,grid):
	closed_list = list()
	open_list = BHeap() 
	open_list.insert(start)

	came_from = dict()

	start.g_val = 0
	start.f_val = start.g_val + heuristic(start,goal)

	while not open_list.empty():
		# pdb.set_trace()
		current = open_list.delete() # get cell with lowest f_value
		# path.append(current)
		closed_list.append(current)

		if current.equals(goal):
			return reconstruct_path(came_from,goal)

		for neighbor in get_neighbors(current,grid):
			# pdb.set_trace()
			if in_closed_list(closed_list,neighbor):
			# for item in closed_list:
				# if neighbor.equals(item):
					continue

			temp_g_score = current.g_val + 1 # cost(current,neighbor) will always be 1

			if temp_g_score < neighbor.g_val:
				came_from[neighbor] = current
				neighbor.g_val = temp_g_score
				neighbor.f_val = neighbor.g_val + heuristic(neighbor,goal)
				if not open_list.contains(neighbor):
					open_list.insert(neighbor)

	return False

def reconstruct_path(came_from,current):
	for item in came_from:
		print "({0},{1}) -> ({2},{3})".format(item.x,item.y,came_from[item].x, came_from[item].y)


	# pdb.set_trace()
	total_path = [current]
	while in_dict(current,came_from):
		current = came_from[current]
		total_path.append(current)

	return total_path


def in_dict(current,came_from):
	for key in came_from:
		if current.equals(key):
			return True

	return False










def compute_path(start,goal,grid,open_list,closed_list,counter):
	while goal.g_val > open_list.check_min():
		s = open_list.delete()
		closed_list.append(s)

		neighbors = get_neighbors(s,grid)

		for neighbor in neighbors:
			if neighbor.search_val < counter:
				neighbor.g_val = infinity
				neighbor.search_val = counter
			if neighbor.g_val > s.g_val + 1:
				neighbor.g_val = s.g_val + 1
				path_list.append(s)

				# if neighbor

def repeated_a_star(start,goal,grid):
	counter = 0
	init_grid()

	while start != goal:
		counter += 1
		start.g_val = 0
		start.search_val = counter

		goal.g_val = infinity
		goal.search_val = counter

		open_list = BHeap()
		closed_list = list()

		start.h_val = heuristic(start,goal)
		start.f_val = start.g_val + heuristic(start,goal)

		open_list.append(start)

		#a_star()

		if open_list.empty():
			print "Cannot reach target"

		# Follow sequence of states to destination

		# Set start state to current state of the agent

		# Update increased action costs?

	print "I reached the target"























