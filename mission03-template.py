#
# CS1010S --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n = 9, because it is 3 times of 3 f 

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6))
# Explanation: 33. Apply add add1 to 6 27 times = 2, since thrice(thrice)blabla is 3 ^ 3

# (ii) print(thrice(thrice)(identity)(compose))
# Explanation: f(g(x)). 

# (iii) print(thrice(thrice)(sq)(1))
# Explanation: 1, because 27(sq(1)) will give a value of 1 nonetheless

# (iv) print(thrice(thrice)(sq)(2))
# Explanation: Number is too high to be even processed


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0) #initialise to 0, for this iterative function 
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        if x == 0:
            return 0
        else:
            return x * x #squared x as observed that S(5) highest number is 25

    def op(x, y):
        if y == f(1):
            return y
        else:
            return y + x + y 

    n = t + 1 #linking the parameter of t in the function smiley_sum to n

    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x):
        if x == 0:
            return 0
        elif x == 1 or x == 2:
            return 1
        else:
            return new_fib(n-1) + new_fib(n-2)
        

    def op(x, y):
        return y 

    # Do not modify this return statement
    return combine(f, op, n+1)

# Your answer here:

'''
def combine(f, op ,n):
    result = f(0) #initialise to 0, for this iterative function 
    for i in range(n):
        result = op(result, f(i))
    return result

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
new_fib(1)	1		
new_fib(2)	1		
new_fib(3)	2		
new_fib(10)	55

'''
