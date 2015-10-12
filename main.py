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


if __name__ == '__main__':

	# size = 4
	# grid = env.generate_grid(size)
	# grid = env.tuples_to_objects(grid)
	if len(sys.argv) > 1:
		print "Format: python <path to maze file>"
		sys.exit(1)
	else:
		maze_file = sys.argv[0]

	print maze_file
	grid, size = env.read_grid(maze_file)
	env.print_cells(grid)


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


	a = Cell(0,0,size)
	b = Cell(0,0,size)

	path = algo.a_star(start,goal,grid)

	print "\n\n\n"

	if path:
		print "path not empty"
		for cell in path:
			print "({0},{1})".format(cell.x,cell.y)	
	else:
		print "path is empty"