#def normalize(numbers):
#	total = sum(numbers)
#	result = []
#	for value in numbers:
#		percent = 100*value/total
#		result.append(percent)
#	return result


##visits = [15,38,80]
##percentages = normalize(visits)
##print(percentages)


def read_visits(data_path):
	with open(data_path) as f:
		for line in f:
			yield int(line)

#it = read_visits('my_numbers.txt')
#print(list(it))
#print(list(it))
##percentages = normalize(it)
##print(percentages)


def normalize_copy(numbers):
	numbers = list(numbers)
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100*value/total
		result.append(percent)
	return result

it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)



def normalize_func(get_iter):
	total = sum(get_iter())
	result = []
	for value in numbers:
		percent = 100*value/total
		result.append(percent)
	return result