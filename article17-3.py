class ReadVisits(object):
	def __init__(self, data_path):
		self.data_path = data_path

	def __iter__(self):
		with open(self.data_path) as f:
			for line in f:
				yield int(line)

def normalize_defensive(numbers):
	if iter(numbers) is iter(numbers):
		raise TypeError('Must supply a container')
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100*value/total
		result.append(percent)
	return result


path = 'my_numbers.txt'
visits = [15,34,80]
normalize_defensive(visits)   # no error
visits = ReadVisits(path)
normalize_defensive(visits)    # no error
it = iter(visits)
normalize_defensive(it)