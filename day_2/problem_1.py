import re

input_file = open('input_file_1.txt', 'r').read().split('\n')

first_pattern = r'^(?P<minimum>\d+)-(?P<maximum>\d+) (?P<character>.): (?P<password>[\w\d]*)$'
second_pattern = r'^(?P<first_position>\d+)-(?P<second_position>\d+) (?P<character>.): (?P<password>[\w\d]*)$'

def find_first_solution(input_file):
	correct_passwords = list(filter(fits_first_password_rule, input_file))
	return len(correct_passwords)

def find_second_solution(input_file):
	correct_passwords = list(filter(fits_second_password_rule, input_file))
	return len(correct_passwords)

def fits_first_password_rule(line):
	m = re.match(first_pattern, line)
	return int(m.group('minimum')) <= m.group('password').count(m.group('character')) <= int(m.group('maximum'))

def fits_second_password_rule(line):
	m = re.match(second_pattern, line)

	password = m.group('password')
	password_length = len(password)
	character = m.group('character')
	first_position = int(m.group('first_position')) - 1;
	second_position = int(m.group('second_position')) - 1;

	return sum(list([(first_position < password_length and password[first_position] == character), (second_position < password_length and password[second_position] == character)])) == 1

print('first solution')
print(find_first_solution(input_file))
print('second solution')
print(find_second_solution(input_file))

# if nmin-1 < 0 or nmax-1 >= len(password):
#    print(line)