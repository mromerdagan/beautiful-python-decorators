# beautiful-python-decorators
Just a python script with many beautiful decorators

### trace
Show all calls to a function, and return values. This becomes handy when
investigating the nature of complex functions, especially if they're recursive.

For example:
~~~~
from beautiful_decorators import trace

@trace
def rec_factorial(n):
	if n == 0:
		return 1
	return n * rec_factorial(n-1)

if __name__ == "__main__":
	print(rec_factorial(3))

~~~~

Would result in:

~~~~
('rec_factorial', 3)
('rec_factorial', 2)
('rec_factorial', 1)
('rec_factorial', 0)
('return', '1')
('return', '1')
('return', '2')
('return', '6')
6
~~~~
