import re

parse_input_regex = re.compile(r"^(?P<row>[FB]{7})(?P<seat>[LR]{3})$", re.MULTILINE)

assigned_seats = parse_input_regex.findall(open('input_file.txt', 'r').read())

seat_ids = list()
filled_seats = list()

num_rows = 128
num_columns = 8

for i in range(num_rows):
	seats = list()

	for j in range(num_columns):
		seats.append('0')

	filled_seats.append(seats)

for row, column in assigned_seats:
	row_range = range(num_rows)
	column_range = range(num_columns)

	for character in row:
		half_range = int(len(row_range) / 2)

		if (character == 'F'):
			row_range = row_range[:half_range]
		elif (character == 'B'):
			row_range = row_range[half_range:]

	final_row = row_range[0]

	for character in column:
		half_range = int(len(column_range) / 2)

		if (character == 'L'):
			column_range = column_range[:half_range]
		elif (character == 'R'):
			column_range = column_range[half_range:]

	final_column = column_range[0]

	seat_ids.append((final_row * 8) + final_column)

	filled_seats[final_row][final_column] = '1'


for row, seats in enumerate(filled_seats):
	seats_string = ''.join(seats)

	seat_index = seats_string.find('101')

	if (seat_index > -1):

		my_seat_id = (row * 8) + (seat_index + 1)

		break

print("Max seat ID: {max_seat_id}".format(max_seat_id = max(seat_ids)))
print("My seat ID: {my_seat_id}".format(my_seat_id = my_seat_id))
