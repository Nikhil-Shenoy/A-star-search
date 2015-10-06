import environment as env

def create_mazes():
	for i in range(0,50):
		grid = env.generate_grid(101)
		output_file = "mazes/maze_{0}.csv".format(i)
		env.write_csv(grid,output_file)

if __name__ == '__main__':

	create_mazes()
