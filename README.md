# beautiful-python-decorators
Just a collection of many beautiful python decorators

*If you're unfamiliar with python decorators, you can read 
[this great article](https://realpython.com/primer-on-python-decorators/)*

*In short: python decorator is a function that get another function as parameter,
and returns a new function. This might sound cumbersome, but if you use the
terminology of 'decoration' it becomes easier: the decorator gets a function and
returns a new decorated one. The decoration can be: adding functionality, adding
debug information, and so forth*

### trace
This decorator shows all calls to a function, and return values. This becomes 
handy when investigating the nature of complex functions, especially if they're
recursive.

Usage example:
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

Result:
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

A more sophisticated version of `trace` is available as `beautiful_trace`, which
kind of does the same, but in addition show the "depth" of the recursion visually.

Usage example:
~~~~
from beautiful_decorators import beautiful_trace

@beautiful_trace
def rec_factorial(n):
	if n == 0:
		return 1
	return n * rec_factorial(n-1)

if __name__ == "__main__":
	print(rec_factorial(3))
~~~~

Result:
~~~~
|-- rec_factorial 3
|  |-- rec_factorial 2
|  |  |-- rec_factorial 1
|  |  |  |-- rec_factorial 0
|  |  |  |++ return 1
|  |  |++ return 1
|  |++ return 2
|++ return 6
6
~~~~

