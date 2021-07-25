#
# CS1010S --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(p1, p2, p3, p4):
    return beside(stack(p4, p3), stack(p1,p2))


# Test
#show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))

##########
# Task 2 #
##########

def simple_fractal(pic):
    return beside(pic, stack(pic,pic))

# Test
#show(simple_fractal(make_cross(rcross_bb)))


