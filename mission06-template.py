#
# CS1010S --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn),rotate(-theta)(curve_fn))) #left curve theta, right curve -theta
    return inner_gosperize


# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(10)(0.1), 50)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below
# profile_fn(lambda: gosper_curve(10)(0.1), 300)


# Time measurements
#  Reading 1 : 19.955799999934243
#  Reading 2 : 19.537399999990157
#  Reading 3 : 17.477699999972174
#  Reading 4 : 19.43770000002587
#  Reading 5 : 18.0004600000040227
#  Average Reading : 18.88s
#  <...do for at least 5 times and take the average...>


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# profile_fn(lambda: gosper_curve_with_angle(10, lambda lvl:pi/4)(0.1), 300)

#  Reading 1: 27.61040000018511
#  Reading 2: 15.334400000028836
#  Reading 3: 18.719099999998434
#  Reading 4: 14.103400000067268
#  Reading 5: 14.271399999870482
#  Average Reading: 18.01s 
#  <...do for at least 5 times and take the average...>

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# profile_fn(lambda: your_gosper_curve_with_angle(10, lambda lvl:pi/4)(0.1), 300)

#  Reading 1: 294.6113000000423
#  Reading 2: 297.57519999998294
#  Reading 3: 302.26999999990767
#  Reading 4: 311.71199999994315
#  Reading 5: 295.2809000000798
#  Average Reading: 300.29
#  <...do for at least 5 times and take the average...>


# Conclusion:
# It appears that the more customisable a function is, the less time-efficient it would be such as the case
# of your_gosper_curve_with_angle, that takes 10 times longer than the other two functions 

##########
# Task 2 #
##########

#  1) Definitely, joe_rotate will work and achieve the same purpose as rotate 


#  2) Before explaining, let's observe the derivation of the function gosper_curve from hi_graph below:
#     what do we notice, gosper_curve itself by nature, is called upon recursively, as observed in the
#     gosper_curve, gosperize and repeated function. So this insights mean that by removing the variable
#     pt = curve(t), the storage of x, y will increased exponentially from 2, 4 to order of growth(2**n) by nature
#     rather than simply having the storage 'removed', kept constant by the assigned pt = curve(t), thus accounting for the
#     exponential growth in joe_rotate 
'''
def gosper_curve(level):
    return repeated(gosperize, level)(unit_line)

def gosperize(curve):
    scaled_curve = scale(sqrt(2)/2)(curve)
    left_curve = rotate(pi/4)(scaled_curve)
    right_curve = translate(0.5,0.5)(rotate(-pi/4)(scaled_curve))

    return connect_rigidly(left_curve, right_curve)

    
def repeated(f, n):
    if (n == 0):
        return identity
    return composed(f, repeated(f, n-1))


'''

##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <3>         <4>
#                      2         <5>         <10>
#                      3         <7>         <20>
#                      4         <9>         <46>
#                      5         <11>        <94>
#
#  Evidence of exponential growth in joe_rotate.
#  From the table, it is evident that rotate increases linearly in terms of order of time(N), whilst joe_rotate is exponential
# in terms of order of growth in time(2^N), thus proven. 

