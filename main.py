import environment as env
import pprint
import random
import sys
import algo
import datetime
import csv
from cell import Cell
# import pdb

def create_mazes():
	for i in range(0,101):
		grid = env.generate_grid(101)
		output_file = "mazes/maze_{0}.csv".format(i)
		env.write_csv(grid,output_file)
		print "Created {0}".format(output_file)

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

	# return start, goal

def part_2(num_files):
	# Compare run times for each maze using the two tie-break methods

	out_file = open('data/part_2_data.csv','w')
	writer = csv.writer(out_file)

	# Header
	writer.writerow(('maze_num','smaller_exec_time','larger_exec_time','smaller_expanded_states','larger_expanded_states'))

	for i in range(0,num_files):
		maze_file = "mazes/maze_{0}.csv".format(i)
		grid, size = env.read_grid(maze_file)
		start = Cell(0,0,size)
		goal = Cell(100,100,size)

		smaller_expanded_states = 0
		larger_expanded_states = 0

		print "start smaller"
		smaller_break_start = datetime.datetime.now()
		path, smaller_expanded_states = algo.repeated_forward_a_star(start,goal,grid,1,smaller_expanded_states)
		smaller_break_end = datetime.datetime.now()

		print "reset grid"
		# RE-INITIALIZE GRID
		new_grid, size = env.read_grid(maze_file)

		print "start larger"
		larger_break_start = datetime.datetime.now()
		path, larger_expanded_states = algo.repeated_forward_a_star(start,goal,new_grid,0,larger_expanded_states)
		larger_break_end = datetime.datetime.now()

		smaller_exec_time = (smaller_break_end - smaller_break_start).total_seconds()
		larger_exec_time = (larger_break_end - larger_break_start).total_seconds()

		print "{0},{1},{2},{3},{4}".format(i,smaller_exec_time,larger_exec_time,smaller_expanded_states,larger_expanded_states)
		writer.writerow((i,smaller_exec_time,larger_exec_time,smaller_expanded_states,larger_expanded_states))

	out_file.close()

def part_3(num_files):
	out_file = open('data/part_3_data.csv','w')
	writer = csv.writer(out_file)

	# Header
	writer.writerow(('maze_num','forward_exec_time','backward_exec_time','forward_expanded_states','backward_expanded_states'))

	for i in range(0,num_files):
		maze_file = "mazes/maze_{0}.csv".format(i)
		grid, size = env.read_grid(maze_file)
		start = Cell(0,0,size)
		goal = Cell(100,100,size)

		forward_expanded_states = 0
		backward_expanded_states = 0

		print "forward"
		forward_start = datetime.datetime.now()
		path, forward_expanded_states = algo.repeated_forward_a_star(start,goal,grid,0,forward_expanded_states)
		forward_end = datetime.datetime.now()

		print "reset grid"
		# RE-INITIALIZE GRID
		new_grid, size = env.read_grid(maze_file)

		print "backward"
		backward_start = datetime.datetime.now()
		path, backward_expanded_states = algo.repeated_backward_a_star(start,goal,new_grid,0,backward_expanded_states)
		backward_end = datetime.datetime.now()

		forward_exec_time = (forward_end - forward_start).total_seconds()
		backward_exec_time = (backward_end - backward_start).total_seconds()

		print "{0},{1},{2},{3},{4}".format(i,forward_exec_time,backward_exec_time,forward_expanded_states,backward_expanded_states) 
		writer.writerow((i,forward_exec_time,backward_exec_time,forward_expanded_states,backward_expanded_states))

	out_file.close()	

def part_4(num_files):
	out_file = open('data/part_4_data.csv','w')
	writer = csv.writer(out_file)

	# Header
	writer.writerow(('maze_num','forward_exec_time','adaptive_exec_time','forward_expanded_states','adaptive_expanded_states'))

	for i in range(0,num_files):
		maze_file = "mazes/maze_{0}.csv".format(i)
		grid, size = env.read_grid(maze_file)
		start = Cell(0,0,size)
		goal = Cell(100,100,size)

		forward_expanded_states = 0
		adaptive_expanded_states = 0

		print "forward"
		forward_start = datetime.datetime.now()
		path, forward_expanded_states = algo.repeated_forward_a_star(start,goal,grid,0,forward_expanded_states)
		forward_end = datetime.datetime.now()

		print "reset grid"
		# RE-INITIALIZE GRID
		new_grid, size = env.read_grid(maze_file)

		print "adaptive"
		adaptive_start = datetime.datetime.now()
		path, adaptive_expanded_states = algo.adaptive_a_star(start,goal,new_grid,0,adaptive_expanded_states)
		adaptive_end = datetime.datetime.now()

		forward_exec_time = forward_end - forward_start
		adaptive_exec_time = adaptive_end - adaptive_start

		forward_exec_time = forward_exec_time.total_seconds()
		adaptive_exec_time = adaptive_exec_time.total_seconds()

		print "{0},{1},{2},{3},{4}".format(i,forward_exec_time,adaptive_exec_time,forward_expanded_states,adaptive_expanded_states) 
		writer.writerow((i,forward_exec_time,adaptive_exec_time,forward_expanded_states,adaptive_expanded_states))

	out_file.close()	


if __name__ == '__main__':

	# Get rid of the .pyc files that get generated on each run
	sys.dont_write_bytecode = True 

	if len(sys.argv) != 3:
		print "Format: python main.py <path to maze file> <tiebreak val: 1 for smaller g, 0 for larger g>"
		sys.exit(1)
	else:
		maze_file = sys.argv[1]
		tie_val = int(sys.argv[2])
		if tie_val != 1 and tie_val != 0:
			print "Invalid tie break value. Use only 1 or 0"
			sys.exit(1)

	num_files = 50
	# create_mazes()
	# part_2(num_files)
	# part_3(num_files)
	part_4(num_files)

	# grid, size = env.read_grid(maze_file)
	# # start, goal = get_start_and_goal(grid)
	# start = Cell(0,0,101)
	# goal = Cell(100,100,101)

	# print "start forward"
	# forward_expanded_states = 0
	# forward_start = datetime.datetime.now()
	# path, forward_expanded_states = algo.repeated_forward_a_star(start,goal,grid,0,forward_expanded_states)
	# # path = algo.repeated_forward_a_star(start,goal,grid,1)
	# forward_end = datetime.datetime.now()
	# print "finished with forward"
	# # RE-INITIALIZE GRID
	# new_grid, size = env.read_grid(maze_file)
	# print "reset the grid"

	# print "start adaptive"
	# adaptive_expanded_states = 0
	# backward_expanded_states = 0
	# adaptive_start = datetime.datetime.now()
	# # path, adaptive_expanded_states = algo.adaptive_a_star(start,goal,new_grid,0,adaptive_expanded_states)
	# path, backward_expanded_states = algo.repeated_backward_a_star(start,goal,new_grid,0,backward_expanded_states)
	# adaptive_end = datetime.datetime.now()
	# print "finished with adaptive"

	# forward_exec_time = forward_end - forward_start
	# adaptive_exec_time = adaptive_end - adaptive_start

	# forward_exec_time = forward_exec_time.total_seconds()
	# adaptive_exec_time = adaptive_exec_time.total_seconds()
	# print "{0}, {1}, {2}, {3}".format(forward_exec_time,adaptive_exec_time,forward_expanded_states,backward_expanded_states)
























	# grid, size = env.read_grid(maze_file)
	# env.print_cells(grid)

	# start, goal = get_start_and_goal(grid)

	# path = algo.a_star(start,goal,grid)
	# print "forward"
	# path = algo.repeated_forward_a_star(start,goal,grid,tie_val)
	# print "backward"
	# path = algo.repeated_adaptive_a_star(start,goal,grid,tie_val)

	# if path:
	# 	print "path not empty"
	# 	for cell in path:
	# 		print "({0},{1})".format(cell.x,cell.y)	
	# else:
	# 	print "path is empty"