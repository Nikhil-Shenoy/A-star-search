from binary_heap import BHeap
import math
# import pdb

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
			sup = 1
			# print "({0},{1}) -> {2}".format(closed_list[i].x,closed_list[i].y,closed_list[i].f_val)

def reconstruct_path(came_from,current,size):
	key_list = list()
	for key in came_from:
		x = key / size # change to size
		if key < size:
			y = key
		else:	
			y = key % size # change to size
		key_list.append(key)

	total_path = [current]
	key = current.hash_value
	while key in key_list:
		current = came_from[key]
		total_path.append(current)
		key = current.hash_value

	forward_path = list()

	for i in range(len(total_path)-1,-1,-1):
		item = total_path.pop()
		forward_path.append(item)


	return forward_path

def a_star(start,goal,grid):
	size = len(grid)
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
			# pdb.set_trace()def repeated_backward_a_star(start,goal,grid,Tie_val):

			return reconstruct_path(came_from,goal,size)

		for neighbor in get_neighbors(current,grid):
			# pdb.set_trace()
			if in_closed_list(closed_list,neighbor):
			# for item in closed_list:
				# if neighbor.equals(item):
					continue

			temp_g_score = current.g_val + 1 # cost(current,neighbor) will always be 1

			if temp_g_score < neighbor.g_val:
				came_from[neighbor.hash_value] = current
				neighbor.g_val = temp_g_score
				neighbor.f_val = neighbor.g_val + heuristic(neighbor,goal)
				if not open_list.contains(neighbor):
					open_list.insert(neighbor)

	empty_list = list()
	return empty_list

def compute_path(start,goal,grid,open_list,closed_list,counter,expanded_states):
	size = len(grid)

	came_from = dict()

	while not open_list.empty():
		# gpdb.set_trace()
		current = open_list.delete() # get cell with lowest f_value
		expanded_states += 1
		# path.append(current)
		closed_list.append(current)

		if current.equals(goal):
			# pdb.set_trace()
			return reconstruct_path(came_from,goal,size), expanded_states

		for neighbor in get_neighbors(current,grid):
			# pdb.set_trace()
			if in_closed_list(closed_list,neighbor):
			# for item in closed_list:
				# if neighbor.equals(item):
					continue

			if neighbor.search_val < counter:
				neighbor.g_val = infinity
				neighbor.search_val = counter

			temp_g_score = current.g_val + 1 # cost(current,neighbor) will always be 1

			if temp_g_score < neighbor.g_val:
				came_from[neighbor.hash_value] = current
				neighbor.g_val = temp_g_score
				neighbor.f_val = neighbor.g_val + heuristic(neighbor,goal)
				if not open_list.contains(neighbor):
					open_list.insert(neighbor)
	
	empty_list = list()
	return empty_list, 0

def repeated_forward_a_star(start,goal,grid,Tie_val,forward_expanded_states):
	counter = 0
	empty_list = list()

	while start != goal:
		counter += 1
		start.g_val = 0
		start.search_val = counter

		goal.g_val = infinity
		goal.search_val = counter

		open_list = BHeap(tie_val=Tie_val)
		closed_list = list()

		start.f_val = start.g_val + heuristic(start,goal)

		open_list.insert(start)

		optimal_path, forward_expanded_states = compute_path(start,goal,grid,open_list,closed_list,counter,forward_expanded_states)

		if open_list.empty():
			print "Cannot reach target"
			break

		if not optimal_path:
			print "Cannot reach target"
			break

		start = optimal_path[0]
		for i in range(1,len(optimal_path)):
			# if cost(start,optimal_path[i]) != 1:
			# 	# update increased action costs?
			# 	break
			# else:
			# 	start = optimal_path[i]	
			# print "({0},{1})".format(start.x, start.y)
			start = optimal_path[i]

	return optimal_path, forward_expanded_states

def repeated_backward_a_star(start,goal,grid,Tie_val,backward_expanded_states):
	counter = 0
	empty_list = list()

	while start != goal:
		counter += 1
		goal.g_val = 0
		goal.search_val = counter

		start.g_val = infinity
		start.search_val = counter

		open_list = BHeap(tie_val=Tie_val)
		closed_list = list()

		goal.f_val = goal.g_val + heuristic(goal,start)

		open_list.insert(goal)

		optimal_path_reversed, backward_expanded_states = compute_path(goal,start,grid,open_list,closed_list,counter,backward_expanded_states)

		optimal_path = list()

		for i in range(len(optimal_path_reversed)-1,-1,-1):
			item = optimal_path_reversed.pop()
			optimal_path.append(item)

		if open_list.empty():
			print "Cannot reach target"
			return empty_list, 0

		if not optimal_path:
			print "Cannot reach target"
			return empty_list, 0

		start = optimal_path[0]
		for i in range(1,len(optimal_path)):
			# if cost(start,optimal_path[i]) != 1:
			# 	# update increased action costs?
			# 	break
			# else:
			# 	start = optimal_path[i]	
			# print "({0},{1})".format(start.x, start.y)
			start = optimal_path[i]


	print "I reached the target"

	return optimal_path, backward_expanded_states

def adaptive_heuristic(current,goal):
	return goal.g_val - current.g_val

def compute_adaptive_path(start,goal,grid,open_list,closed_list,counter,expanded_states):
	size = len(grid)

	came_from = dict()

	while not open_list.empty():
		# gpdb.set_trace()
		current = open_list.delete() # get cell with lowest f_value
		expanded_states += 1
		# path.append(current)
		closed_list.append(current)

		if current.equals(goal):
			# pdb.set_trace()
			return reconstruct_path(came_from,goal,size), expanded_states

		for neighbor in get_neighbors(current,grid):
			# pdb.set_trace()
			if in_closed_list(closed_list,neighbor):
			# for item in closed_list:
				# if neighbor.equals(item):
					continue

			if neighbor.search_val < counter:
				neighbor.g_val = infinity
				neighbor.search_val = counter

			temp_g_score = current.g_val + 1 # cost(current,neighbor) will always be 1

			if temp_g_score < neighbor.g_val:
				came_from[neighbor.hash_value] = current
				neighbor.g_val = temp_g_score
				neighbor.f_val = neighbor.g_val + adaptive_heuristic(neighbor,goal)
				if not open_list.contains(neighbor):
					open_list.insert(neighbor)
	
	empty_list = list()
	return empty_list, 0

def adaptive_a_star(start,goal,grid,Tie_val,adaptive_expanded_states):
	counter = 0
	empty_list = list()

	while start != goal:
		counter += 1
		start.g_val = 0
		start.search_val = counter

		goal.g_val = infinity
		goal.search_val = counter

		open_list = BHeap(tie_val=Tie_val)
		closed_list = list()

		start.f_val = start.g_val + adaptive_heuristic(start,goal)

		open_list.insert(start)

		optimal_path, adaptive_expanded_states = compute_adaptive_path(start,goal,grid,open_list,closed_list,counter,adaptive_expanded_states)

		if open_list.empty():
			print "Cannot reach target"
			break

		if not optimal_path:
			print "Cannot reach target"
			break

		start = optimal_path[0]
		for i in range(1,len(optimal_path)):
			# if cost(start,optimal_path[i]) != 1:
			# 	# update increased action costs?
			# 	break
			# else:
			# 	start = optimal_path[i]	
			# print "({0},{1})".format(start.x, start.y)
			start = optimal_path[i]

	return optimal_path, adaptive_expanded_states


















