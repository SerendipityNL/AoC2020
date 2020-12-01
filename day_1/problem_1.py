input = list(map(int, open('input_1.txt', 'r').read().split('\n')))

def find_first_solution(input):
	for first_number in input:
		for second_number in input:
			if (first_number + second_number) == 2020:
				return [first_number, second_number, (first_number * second_number)]

def find_second_solution(input):
	for first_number in input:
		for second_number in input:
			for third_number in input:
				if (first_number + second_number + third_number) == 2020:
					return [first_number, second_number, third_number, (first_number * second_number * third_number)]

print('first solution')
print(find_first_solution(input))
print('second solution')
print(find_second_solution(input))