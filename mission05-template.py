#
# CS1010S --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    #The end and the start of the curves can be found | Find relation bet end of curve 1 and start of curve 2
    end_of_curve1 = curve1(1)
    start_of_curve2 = curve2(0)
    #Find the diff in x pos and y pos from end of curve1 = start of curve2
    x_diff = x_of(end_of_curve1) - x_of(start_of_curve2)
    y_diff = y_of(end_of_curve1) - y_of(start_of_curve2)
    new_curve_2 = translate(x_diff, y_diff)(curve2)
    return connect_rigidly(curve1, new_curve_2)    
    


##########
# Task 2 #
##########



    
        
def show_points_gosper(level, num_points, initial_curve):
    squeezed_curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)(repeated(gosperize, level)(initial_curve))
    draw_points(num_points, squeezed_curve)

    
    
    
    



#show_points_gosper(7, 1000, arc)	The beautiful cursive graph you may find under Mission 5 PDF Task 2.		
#show_points_gosper(5, 500, arc)	The beautiful cursive graph you may find under Mission 5 PDF Task 2.

##########
# Task 3 #
##########

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends())
    return inner_gosperize


'''
**Hints**

So the question is how to gosperize the given curve_fn with angle theta
You only need to pass a general form of gosper curve to connect_ends, then put_in_standard_position will take care of all the translating, rotating and scaling for you. So the question is how to gosperize the given curve_fn with angle theta

anyways, for those that got lost for task 3. My method was:

look at the gosperize_with_angle...

put_in_standard_position is a magic bullet for scaling.
and connect_ends is a substitute for translation.

---

Personally, I'm a bit disappointed in how I'm solving this. 

I'm not thoroughly understanding what goes on in the function.

I'm just using some kind of inference to substitute parts of the code out.
'''
# testing
# draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
# draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
