input_file = open('input_file_1.txt', 'r').read().split('\n')

def find_solutions(input_file):

	slopes = ((1,1), (1,3), (1,5), (1,7), (2, 1))
	total_trees = 1;

	lines		= len(input_file)
	line_length = len(input_file[0])

	for slope_y, slope_x in slopes:
		slope_trees = 0

		position_x = 0
		position_y = 0

		while position_y < (lines - 1):
			position_x = (position_x + slope_x) % line_length
			position_y = position_y + slope_y

			if (input_file[position_y][position_x] == '#'):
				slope_trees += 1

		total_trees *= slope_trees
		print(slope_y, slope_x, slope_trees)

	return total_trees


print('find_solutions')
print(find_solutions(input_file))