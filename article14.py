#def divide(a,b):
#	try:
#		return a/b 
#	except ZeroDivisionError:
#		return None

##result = divide(0,1)
##if result is None:
##	print('Invalid inputs')


x,y = 5,0
#result = divide(x,y)
#if not result:
#	print("Invalid inputs")


#def divide(a,b):
#	try:
#		return True, a/b
#	except ZeroDivisionError:
#		return False, None


#success,result = divide(x,y)
#if not success:
#	print('Invalid inputs')

#_, result = divide(x,y)
#if not result:
#	print('Invalid inputs')


def divide(a,b):
	try:
		return a/b
	except ZeroDivisionError as e:
		raise ValueError('Invalid inputs') from e



x,y = 5,2
try:
	result = divide(x,y)
except ValueError:
	print('Invalid inputs')	
else:
	print('Result is %.1f' % result)

		