#
# CS1010S --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

#recursive function = A function that calls upon itself

def fractal(pic, n):
    if n == 1:
        return pic 
    else:
        N = 0
        N += 1
        return beside(pic, stackn(2**N, fractal(pic, n-1)))
        
#code works and i am not sure why???    
    

# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########
'''Here is an update, cos the original was really confusing and I'm really sorry:

You would probably need to define a variable first and then have a for loop or a while loop, where the n decreases and more stuff are added to the variable to get your final pattern in this form: variable = beside( <stuff to add beside>, variable).

Let's start small with n = 1, which returns the pattern itself.

When n = 2, the final pattern is the pattern when n = 1 together with a stackn(2(2^1), pattern).

When n = 3, the final pattern is the pattern when n = 1 together with a stackn(2(2^1), pattern) together with a stackn(4(2^2), pattern).

Do you see a formula coming out to calculate the number of runes that should be in the stack in each additional pattern?

From the value of n, you could calculate the number of runes that should be in the stack in the rightmost column, when n decreases by one, you can calculate the number of runes that should be in the stack in the second rightmost column and so on......

Hope this helps better!


Yes, you need to use the beside function! Not sure if you count this as adding another variable:

At first, before entering the while loop, I specified a variable = something.

When I entered the while loop, my beside function is in the form of something like that:

variable = beside(<thing you want to add>, variable)

'''




def fractal_iter(pic, n):
    i = n - 1
    last_column = stackn(2**(i), pic)
    while i >= 1:
        last_column = beside(stackn(2**(i-1), pic), last_column)
        i -= 1 
    return last_column 
        
    

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########  
# Task 1c #
###########
def dual_fractal(pic1,pic2, n):
    if n == 1:
        return pic 
    else:
        N = 0
        N += 1
        if N % 2 != 0:
            pic1,pic2=pic2,pic1   
        if N % 2 == 0:
            return beside(pic1,stack(dual_fractal(pic2,pic1,n-1),dual_fractal(pic2,pic1,n-1)))
        if N%2 !=0:
            return beside(pic2,stack(dual_fractal(pic1,pic2,n-1),dual_fractal(pic1,pic2,n-1)))

def illegitimate_dual_fractal(pic1, pic2, n):
     if n == 1:
        return pic1
     else: 
        if n % 2 == 0:
            pic1,pic2=pic2,pic1   
        if n % 2 != 0:
            return beside(pic1,stack(dual_fractal(pic2,pic1,n-1),dual_fractal(pic2,pic1,n-1)))
        if n%2 ==0:
            return beside(pic2,stack(dual_fractal(pic1,pic2,n-1),dual_fractal(pic1,pic2,n-1)))


# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########


def dual_fractal_iter(pic1, pic2, n):
    i = n - 1
    if i % 2 != 0:
        last_column = stackn(2**(i), pic2)
    if i % 2 == 0:
        last_column = stackn(2**(i), pic1)
    while i >= 1:
        if i % 2 != 0:
            last_column = beside(stackn(2**(i-1), pic1), last_column)
        else:
            last_column = beside(stackn(2**(i-1), pic2), last_column)
        i -= 1
    return last_column


# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########
def mosaic(p1, p2, p3, p4):
    return beside(stack(p4, p3), stack(p1,p2))

def steps(p1,p2,p3,p4):
    return beside(stack(p4, overlay_frac(0.25,blank_bb, p3)), stack(overlay_frac(0.75,blank_bb,p1),overlay_frac(0.5,blank_bb,p2)))

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
