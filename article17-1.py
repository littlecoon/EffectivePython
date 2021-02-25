def normalize_func(get_iter):
	total = sum(get_iter())
	result = []
	for value in get_iter():
		percent = 100*value/total
		result.append(percent)
	return result

def read_visits(data_path):
	with open(data_path) as f:
		for line in f:
			yield int(line)


# 注意这个lambda的用法
percentages = normalize_func(lambda:read_visits('my_numbers.txt'))
print(percentages)

