#
# CS1010S --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# (a)
# the input is a Unit-Interval whilst the output is a curve 

# (b)
# The input types is an integer type and the output types is none 

# (c)
def vertical_line(point, length):
    return lambda t: make_point(x_of(point), y_of(point) + length *t)
    

##draw_connected(200, vertical_line(make_point(0.1, 0.1), 0.4))

# (d)
# your answer here

# (e)
# your answer here

##########
# Task 2 #
##########

# (a)
# your answer here

# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        "your answer here"

    return reflected_curve
	
##draw_connected_scaled(200, arc)
##draw_connected_scaled(200, reflect_through_y_axis(arc))
