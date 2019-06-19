#!/usr/bin/python3
import os
import sys
import time
import functools

def trace(f):
	def inner(x):
		print(f.__name__, x)
		value = f(x)
		print('return', repr(value))
		return value
	return inner

def beautiful_trace(f):
	f.rec_depth = 0
	@functools.wraps(f)
	def inner(x):
		print('|  ' * f.rec_depth + '|--', f.__name__, x)
		f.rec_depth += 1
		value = f(x)
		f.rec_depth -= 1
		print('|  ' * f.rec_depth + '|++', 'return', repr(value))
		return value
	return inner

def profile(func):
	def inner(*kargs, **kwargs):
		start = time.time()
		ret = func(*kargs, **kwargs)
		end = time.time()
		print("Total time: {}".format(end-start))
		return ret
	return inner

def memoize(f):
	f.cache = {}
	@functools.wraps(f)
	def g(x):
		if x not in f.cache:
			f.cache[x] = f(x)
		return f.cache[x]
	return g

def supress_output(func):
	def inner(*args):
		old_stdout = sys.stdout
		sys.stdout = open(os.devnull, "w")
		ret = func(*args)
		sys.stdout.close()
		sys.stdout = old_stdout
		return ret
	return inner

# Class as decorators:
# Class needs to get func in constructor, and also be callable

import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        return self.func(*args, **kwargs)

