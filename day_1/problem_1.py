input_file = list(map(int, open('input_file_1.txt', 'r').read().split('\n')))

def find_first_solution(input_file):
	for first_number in input_file:
		for second_number in input_file:
			if (first_number + second_number) == 2020:
				return [first_number, second_number, (first_number * second_number)]

def find_second_solution(input_file):
	for first_number in input_file:
		for second_number in input_file:
			for third_number in input_file:
				if (first_number + second_number + third_number) == 2020:
					return [first_number, second_number, third_number, (first_number * second_number * third_number)]

print('first solution')
print(find_first_solution(input_file))
print('second solution')
print(find_second_solution(input_file))

