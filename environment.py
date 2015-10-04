import pprint
import random
import sys
# import pdb

'''
Make the initial cell the current cell and mark it as visited
While there are unvisited cells
	If the current cell has any neighbours which have not been visited
		Choose randomly one of the unvisited neighbours
		Push the current cell to the stack
		Remove the wall between the current cell and the chosen cell
		Make the chosen cell the current cell and mark it as visited
	Else if stack is not empty
		Pop a cell from the stack
		Make it the current cell
'''

def determine_blocked_status():
	number = random.randrange(0,sys.maxint) % 10
	if number <= 2:
		return "b"
	elif number > 2:
		return "u"

def find_unvisited_neighbors(cell,size,visited):
	i = cell[0]
	j = cell[1]

	# Get initial neighbors list
	if i == 0 and j == 0:
		neighbors = [(i+1,j),(i,j+1)]
	elif i == 0 and j == size-1:
		neighbors = [(i,j-1),(i+1,j)]
	elif i == size-1 and j == size-1:
		neighbors = [(i-1,j),(i,j-1)]
	elif i == size-1 and j == 0:
		neighbors = [(i-1,j),(i,j+1)]
	elif i == 0:
		neighbors = [(i,j-1),(i,j+1),(i+1,j)]
	elif i == size-1:
		neighbors = [(i,j-1),(i,j+1),(i-1,j)]
	elif j == 0:
		neighbors = [(i-1,j),(i+1,j),(i,j+1)]
	elif j == size-1:
		neighbors = [(i-1,j),(i+1,j),(i,j-1)]
	else:
		neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

	for item in neighbors:
		if item in visited:
			neighbors.remove(item)

	return neighbors


# Use recursive back-tracking to generate grid
def generate_grid(size):

	# Create initial grid
	grid = [["x" for i in range(size)] for j in range(size)]

	# Initialize algorithm
	visited = list()	
	unvisited = list() # Maybe make this a BST? For efficiency's sake
	stack = list() # append() adds to the end of the list, pop() without arguments removes last element in the list

	# Select random cell in grid to start at
	current_cell = (random.randrange(0,sys.maxint) % size, random.randrange(0,sys.maxint) % size)
	visited.append(current_cell)

	grid[current_cell[0]][current_cell[1]] = 'u'

	# Make all other cells unvisited
	for i in range(size):
		for j in range(size):
			cell = (i,j)
			if cell != current_cell:
				unvisited.append(cell)

	# While there are unvisited cells
	while unvisited:
		# Get unvisited neighbors of current cell
		neighbor_list = find_unvisited_neighbors(current_cell,size,visited)

		# for item in neighbor_list:
		# 	if item in visited:
		# 		neighbor_list.remove(item)

		# pdb.set_trace()
		# If there are unvisited neighbors
		if neighbor_list:
			# Select random neighbor
			neighbor = neighbor_list[random.randrange(0,sys.maxint) % len(neighbor_list)]
			# pdb.set_trace()

			# Push current cell onto the stack
			stack.append(current_cell)

			# Co-ordinates for convenience
			i = neighbor[0]
			j = neighbor[1]

			# Set blocked status
			grid[i][j] = determine_blocked_status()

			# Make the chosen cell the current cell and mark it as visited
			# if neighbor in unvisited:
			unvisited.remove(neighbor)
			visited.append(neighbor)
			current_cell = neighbor
			# pdb.set_trace()

		# If stack is not empty
		elif stack:
			current_cell = stack.pop()
			# pdb.set_trace()

	return grid


pp = pprint.PrettyPrinter()

size = int(sys.argv[1])
grid = generate_grid(size)

pp.pprint(grid)
