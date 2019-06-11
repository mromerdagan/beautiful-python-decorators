#!/usr/bin/python3

def trace(f):
	def inner(x):
		print(f.__name__, x)
		value = f(x)
		print('return', repr(value))
		return value
	return inner

#def beautiful_trace(f):
#	f.rec_depth = 0
#	def inner(x):
#		print '|  ' * f.rec_depth + '|--', f.__name__, x
#		f.rec_depth += 1
#		value = f(x)
#		f.rec_depth -= 1
#		print '|  ' * f.rec_depth + '|++', 'return', repr(value)
#		return value
#	return inner
#
#def profile(func):
#	import time
#	func.depth = 0
#	def inner(x):
#		func.depth += 1
#		start = time.time()
#		if func.depth == 1:
#			print "D: ",start
#		ret = func(x)
#		end = time.time()
#		if func.depth == 1:
#			print "D: ",end
#		func.depth -= 1
#		if func.depth == 0:
#			print "D:", end, start
#			print func.__name__, x, "({})".format(end-start)
#		return ret
#	return inner
#
#def memoize(f):
#	f.cache = {}
#	def g(x):
#		if x not in f.cache:
#			f.cache[x] = f(x)
#		return f.cache[x]
#	return g
#
#def supress_output(func):
#	def inner(*args):
#		old_stdout = sys.stdout
#		sys.stdout = open(os.devnull, "w")
#		ret = func(*args)
#		sys.stdout.close()
#		sys.stdout = old_stdout
#		return ret
#	return inner
#
#@trace
#def foo(msg):
#	print msg
#
#
#@profile
#def flatten_list(nested):
#	ret = []
#	if isinstance(nested, list):
#		for i in nested:
#			ret += flatten_list(i)
#		return ret
#	else:
#		return [nested]
#
#@profile
#@memoize
#def fib(n):
#	if n is 0 or n is 1:
#		return 1
#	else:
#		return fib(n-1) + fib(n-2)
##flatten_list([1,2,3,[1,5,[345,1]],[1,2,3]])
#print fib(46)
