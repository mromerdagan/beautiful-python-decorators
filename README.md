# beautiful-python-decorators
Just a collection of many beautiful python decorators

The decorators implementaion can be found at 
[beautiful_decorators.py](https://github.com/mromerdagan/beautiful-python-decorators/blob/master/beautiful_decorators.py)

Below you can find usage examples to all of the decorators + explanations

*If you're unfamiliar with python decorators, you can read 
[this great article](https://realpython.com/primer-on-python-decorators/)*

*In short: python decorator is a function that get another function as parameter,
and returns a new function. This might sound cumbersome, but if you use the
terminology of 'decoration' it becomes easier: the decorator gets a function and
returns a new decorated one. The decoration can be: adding functionality, adding
debug information, and so forth*


### @trace
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
rec_factorial 3
rec_factorial 2
rec_factorial 1
rec_factorial 0
return 1
return 1
return 2
return 6
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

### @profile
If you know `timeit`, this decorator does the same trick: It will measure the
time of execution of a function.

Usage example:
~~~~

import time
from beautiful_decorators import profile

@profile
def longtime_foo():
	time.sleep(4)


if __name__ == "__main__":
	longtime_foo()
~~~~

Result:
~~~~
Total time: 4.004046440124512
~~~~

### @memoize
*memoization or memoisation is an optimization technique used primarily to speed
up computer programs by storing the results of expensive function calls and 
returning the cached result when the same inputs occur again.* - 
[wikipedia](https://en.wikipedia.org/wiki/Memoization)

Consider fibonacci function that uses recursion (I know recursion is not a good
idea here! it's for the sake of education!)  
So, let's look at the calculations needed to compute rec_fib(5). We will do that
using our beloved `beautiful_trace` of course :)

So the code is something like this:
~~~~
#!/usr/bin/python3

import time
from beautiful_decorators import beautiful_trace

@beautiful_trace
def rec_fibo(n):
	if 0 <= n <= 1:
		return 1
	return rec_fibo(n-1) + rec_fibo(n-2)

if __name__ == "__main__":
	rec_fibo(5)
~~~~

And the result is:
~~~~
|-- rec_fibo 5
|  |-- rec_fibo 4
|  |  |-- rec_fibo 3
|  |  |  |-- rec_fibo 2
|  |  |  |  |-- rec_fibo 1
|  |  |  |  |++ return 1
|  |  |  |  |-- rec_fibo 0
|  |  |  |  |++ return 1
|  |  |  |++ return 2
|  |  |  |-- rec_fibo 1
|  |  |  |++ return 1
|  |  |++ return 3
|  |  |-- rec_fibo 2
|  |  |  |-- rec_fibo 1
|  |  |  |++ return 1
|  |  |  |-- rec_fibo 0
|  |  |  |++ return 1
|  |  |++ return 2
|  |++ return 5
|  |-- rec_fibo 3
|  |  |-- rec_fibo 2
|  |  |  |-- rec_fibo 1
|  |  |  |++ return 1
|  |  |  |-- rec_fibo 0
|  |  |  |++ return 1
|  |  |++ return 2
|  |  |-- rec_fibo 1
|  |  |++ return 1
|  |++ return 3
|++ return 8
~~~~

Let's count the computations:
* rec_fibo(5): 1
* rec_fibo(4): 1
* rec_fibo(3): 2
* rec_fibo(2): 3
* rec_fibo(1): 5

We can see that rec_fibo(3), rec_fibo(2), and rec_fibo(1) are computed more than
once. Memoization lets us spare these redundant computaions.  
These might seem a little amount of computations beeing saved, but consider the
number if we tried it with n=15  - In this case the number of times rec_fibo(3)
will be computed is **233**! Yeah... it grows very fast (oh... recursion)


