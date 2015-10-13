import environment as env
import pprint
import random
import sys
import algo
from cell import Cell
# import pdb

def create_mazes():
	for i in range(0,1):
		grid = env.generate_grid(4)
		output_file = "mazes/maze_{0}.csv".format(i)
		env.write_csv(grid,output_file)

def get_start_and_goal(grid):
	size = len(grid)
	start = Cell(random.randrange(0,sys.maxint) % size,random.randrange(0,sys.maxint) % size,size)
	goal = Cell(random.randrange(0,sys.maxint) % size,random.randrange(0,sys.maxint) % size,size)

	while grid[start.x][start.y].status == 'b':
		start.x = random.randrange(0,sys.maxint) % size
		start.y = random.randrange(0,sys.maxint) % size
	
	while grid[goal.x][goal.y].status == 'b':
		goal.x = random.randrange(0,sys.maxint) % size
		goal.y = random.randrange(0,sys.maxint) % size

	print "start  ({0},{1})".format(start.x,start.y)
	print "goal  ({0},{1})".format(goal.x,goal.y)

	return start, goal


if __name__ == '__main__':

	# Get rid of the .pyc files that get generated on each run
	sys.dont_write_bytecode = True 
	# size = 4
	# grid = env.generate_grid(size)
	# grid = env.tuples_to_objects(grid)
	if len(sys.argv) > 2:
		print "Format: python main.py <path to maze file>"
		sys.exit(1)
	else:
		maze_file = sys.argv[1]

	grid, size = env.read_grid(maze_file)
	# env.print_cells(grid)

	start, goal = get_start_and_goal(grid)

	# path = algo.a_star(start,goal,grid)
	path = algo.repeated_a_star(start,goal,grid)


	# if path:
	# 	print "path not empty"
	# 	for cell in path:
	# 		print "({0},{1})".format(cell.x,cell.y)	
	# else:
	# 	print "path is empty"