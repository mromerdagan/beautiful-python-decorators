# beautiful-python-decorators
Just a collection of some beautiful python decorators I think should be kept for
a rainy day

The decorators implementaion can be found at 
[beautiful_decorators.py](https://github.com/mromerdagan/beautiful-python-decorators/blob/master/beautiful_decorators.py)

Below you can find usage examples to all of the decorators + explanations

*If you're unfamiliar with python decorators, you can read 
[this great article](https://realpython.com/primer-on-python-decorators/)*

*In short: python decorator is a function that gets another function as a
parameter, and returns a new function. This might sound cumbersome, but if you
use the terminology of 'decoration', it becomes easier: the decorator gets a
function and returns it, but with some "decoration" (=modification). The
decoration can be: adding functionality, adding debug information, and so
forth.*

*Syntax: If you want to decorate a function with decorator named 'dec', you add
a @dec at the line above its definition. Suppose the function name is 'foo'- it
would look like this:*
~~~~
@dec
def foo():
	# implenetation
	return 'foo'
~~~~

*This is a syntactic sugar for:*
~~~~
def foo():
	# implenetation
	return 'foo'
foo = dec(foo)       # <--- foo is being decorated
~~~~

So, here are the decorators:

### @trace
This decorator will print all calls to a function when they are being made, and
return values. This becomes handy when investigating the nature of complex
functions, especially if they're recursive.

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
kind of does the same, but in addition represent the "depth" of the recursion
level as indentations.

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
> *memoization or memoisation is an optimization technique used primarily to
speed up computer programs by storing the results of expensive function calls
and returning the cached result when the same inputs occur again.* - 
[wikipedia](https://en.wikipedia.org/wiki/Memoization)

Before I start talking about @memoize, its worth noting that in python 3 there
is a built in memoization decorator- `functools.lru_cache`. Usage is as simple
as adding @functools.lru_cache above a function definition. Having said that,
the @memoize decorator is nice for education and learning and I do recomend at
least having a look at it.

Consider fibonacci function that uses recursion (I'm not recommending using
recursion here! it's for the sake of education only)  
So, let's look at the number of calculations needed to compute rec_fib(5). We 
will do that using our beloved `beautiful_trace` from two paragraphs ago :)

The code:
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

And the result:
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

Let's count how many times rec_fibo was called with each number:
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

Now let's put our magical @memoization into action. We keep the @trace as well
(nested decorations in action):

~~~~
#!/usr/bin/python3

import time
from beautiful_decorators import beautiful_trace, memoize

@beautiful_trace
@memoize
def rec_fibo(n):
	if 0 <= n <= 1:
		return 1
	return rec_fibo(n-1) + rec_fibo(n-2)

if __name__ == "__main__":
	rec_fibo(5)

~~~~

The result after the change:
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
|  |  |++ return 2
|  |++ return 5
|  |-- rec_fibo 3
|  |++ return 3
|++ return 8
~~~~

It is clear that now each call to rec_fibo is done only once per number.
The greater n is, the greater runtime improvement we get. Of course, nothing
comes for free-
this improvement costs us with memory being used to store the results but for
many cases we would'nt mide paying this price.

### @supress_output
Generally speaking, functions can do two things: return values, and have "side
effects". Many times they do both. For example, some functions can calculate
some value (to return) and print something regarding the process (side effect).
However, you might want to supress output (if this is a deamon that runs in bg,
for instace).  
This is where @supress_output can become handy.

Let's look at an example:  
Suppose we have a function that gets a list of integers and returns the first
even element, if any. It would look something like this:

~~~~
def find_even(l):
	for i in l:
		print(f'Checking {i}')
		if i % 2 == 0:
			return i
	else:
		return None
	

if __name__ == "__main__":
	even = find_even([1,3,4])
	if even:
		print(f'Found: {even}')
~~~~

For this input [1,3,4] output would be:
~~~~
Checking 1
Checking 3
Checking 4
4
~~~~

For empty case input such as [1, 3, 5] output would be:
~~~~
Checking 1
Checking 3
Checking 5
~~~~

Now, lets add the decorator. So now the code looks like this:
~~~~
from beautiful_decorators import supress_output

@supress_output
def find_even(l):
	for i in l:
		print(f'Checking {i}')
		if i % 2 == 0:
			return i
	else:
		return None
	

if __name__ == "__main__":
	even = find_even([1,3,5])
	if even:
		print(f'{even}')
~~~~

And the outputs would look like (respectively):
~~~~
4
~~~~
And:
~~~~
~~~~

(the trick used by this decorator is replacting the process stdout with devnull,
then restore it).
Nice!


### CountCalls
This one was taken from [Real Python](https://realpython.com/primer-on-python-decorators) 
as is, I put it here because I find it beautiful.

So CountCalls is another decorator that helps monitor the execution of a
function. Whenever a function is called, a counter is being incremented, it can
be accessed as a field (will be clearer in the exmple).

It worth noting that this decorator is implemented as a (callable) class rather
then a function. In order to to so the implementing class needs to get function
refernce in the constructor, and implement the "\_\_call\_\_" function, so the
returning object is callable.

Usage example:
~~~~
#!/usr/bin/python3

from beautiful_decorators import CountCalls

@CountCalls
def say_whee():
    print("Whee!")

if __name__ == "__main__":
	say_whee()
	print(say_whee.num_calls)
	say_whee()
	say_whee()
	say_whee()
	print(say_whee.num_calls)
~~~~

Result:
~~~~
Whee!
1
Whee!
Whee!
Whee!
4
~~~~

That's it for now. I'll keep adding beautiful decorators to this git repo when
I encounter them. Feel free to contribute by yourselfs.

