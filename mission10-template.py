#
# CS1010S --- Programming Methodology
#
# Mission 10 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.


####################
# Helper functions #
# - print_tree     #
# - accumulate     #
####################

def print_tree(tree, print_output=True):
    """
    Helper function to print trees in this mission.

    Yes, it looks scary. Nothing to see here (:
    """
    def get_elements_at_level(tree, level):
        def helper(tree, level, cur):
            if is_empty_tree(tree) and cur < level:
                dummy = build_tree(" ", make_empty_tree(), make_empty_tree())
                return helper(left_branch(dummy), level, cur + 1) + helper(right_branch(dummy), level, cur + 1)
            if cur == level:
                if is_empty_tree(tree):
                    return (" ", )
                else:
                    return (entry(tree), )
            elif cur < level:
                return helper(left_branch(tree), level, cur + 1) + helper(right_branch(tree), level, cur + 1)
        return helper(tree, level, 0)

    def height(tree):
        if is_empty_tree(tree):
            return 0
        else:
            return 1 + max(height(left_branch(tree)), height(right_branch(tree)))

    h = height(tree)
    output_string = ""

    for level in range(h):
        indent = 2 ** (h - (level + 1)) - 1
        spacing = 2 ** (h - level) - 1

        output = " " * indent

        for i, e in enumerate(get_elements_at_level(tree, level)):
            if level == 0 or i == 0:
                output = output + str(e)
            else:
                output = output + " " * spacing + str(e)
        if print_output:
            print(output)
        else:
            output_string += output + '/'
    if not print_output:
        return output_string

def accumulate(fn, initial, seq):
    if not seq: # if seq is empty
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))


###########
# Task 1a #
###########

def build_tree(entry, left, right):
    # Your code here
    return [entry, left, right]


###########
# Task 1b #
###########

def entry(tree):
    # Your code here
    return tree[0]

def left_branch(tree):
    # Your code here
    return tree[1]

def right_branch(tree):
    # Your code here
    return tree[2]


###########
# Task 1c #
###########

def make_empty_tree():
    # Your code here
    return []


###########
# Task 1d #
###########

def is_empty_tree(tree):
    # Your code here
    return False if tree else True 

t1 = build_tree(2, build_tree(1, make_empty_tree(),
                                 make_empty_tree()),
                   build_tree(3, make_empty_tree(),
                                 make_empty_tree()))
print_tree(t1)
#=> 2
#=>1 3

t2 = build_tree(5, build_tree(2, build_tree(1, make_empty_tree(),
                                               make_empty_tree()),
                                 make_empty_tree()),
                   build_tree(7, make_empty_tree(),
                                 build_tree(10, make_empty_tree(),
                                                make_empty_tree())))
print_tree(t2)
#=>   5
#=> 2   7
#=>1     10


###########
# Task 2a #
###########

def insert_tree(x, tree):
    """
    - tree is empty -> return a tree with x as entry and empty left and right branches
    - x <= entry -> return new tree with x inserted into left sub tree
    - otherwise -> return new tree with x inserted into right sub tree
    """
    if is_empty_tree(tree):
        return build_tree(x,make_empty_tree(),make_empty_tree())
    else:
        if x <= entry(tree):
            return build_tree(entry(tree),insert_tree(x,left_branch(tree)),right_branch(tree))
        else:
            return build_tree(entry(tree),left_branch(tree),insert_tree(x,right_branch(tree)))
                            

t1 = insert_tree(5, t1)
print_tree(t1)
#=> 2           insert_tree(5, t1)        2
#=>1 3               ===>               1   3
#=>                                          5

t2 = insert_tree(6, t2)
print_tree(t2)
#=>   5         insert_tree(6, t2)        5
#=> 2   7            ===>               2   7
#=>1     10                            1   6 10

t2 = insert_tree(3, t2)
print_tree(t2)
#=>   5         insert_tree(3, t2)        5
#=> 2   7            ===>               2   7
#=>1   6 10                            1 3 6 10


###########
# Task 2b #
###########

# Time complexity of insert_tree: It is O(N),
# cause though recursive, only go down to the left or right branch every time,
# such that the depth is N also. 


###########
# Task 2c #
###########

def contains(x, tree):
    """ Returns true if x is in binary tree, otherwise return false """
    if is_empty_tree(tree):
        return False
    elif x == entry(tree):
        return True
    elif x < entry(tree):
        return contains(x,left_branch(tree))
    else: #x > entry(tree)
        return contains(x,right_branch(tree))
            

print(contains(1, t1))
#=> True

print(contains(5, t1))
#=> True

print(contains(42, t1))
#=> False

print(contains(10, t2))
#=> True

print(contains(6, t2))
#=> True

print(contains(11, t2))
#=> False


###########
# Task 2d #
###########

# Time complexity of contains: O(N), since though recursive function,
#only go down to the left or right branch every time,
# such that the depth is N also. 


###########
# Task 2e #
###########

def flatten(tree):
    """ flattens tree with the following rule:
        visit left branch, visit entry then visit right branch """
    # Your code here
    if is_empty_tree(tree):
        return []
    else: #Not an empty tree #Notice the pattern is that entry(value) in the 'middle' gets selected
        #Hint: The list concatenation operator might be helpful to you.
        #Use + to concatenate
        #multiple lists. e.g [my_val] + some_list + [another_val] + some_other_list        
        # even if [] + [1] + [] == [1] based on IDLE, so does not matter if left_branch/right_branch is_empty_tree
        return flatten(left_branch(tree)) + [entry(tree)] + flatten(right_branch(tree))
        
        
#Hint: The list concatenation operator might be helpful to you. Use + to concatenate
#multiple lists. e.g [my_val] + some_list + [another_val] + some_other_list        

print(flatten(t1))
#=> [1, 2, 3, 5]

print(flatten(t2))
#=> [1, 2, 3, 5, 6, 7, 10]


###########
# Task 2f #
###########

# Time complexity of flatten: It will likely be O(N^2), since it traverses down the left and right of every branches
# in a recursive manner so O(n * n) = O(N^2)


###########
# Task 3a #
###########
#Using the functions insert_tree and flatten, define a function sort_it that takes in
#a list of numbers and returns a sorted list in an ascending order. (4 marks)

def sort_it(lst):
    # Your code here
    apple_tree = make_empty_tree()
    for elem in lst:
        apple_tree = insert_tree(elem, apple_tree)
    return flatten(apple_tree)    
        

print(sort_it([5, 3, 2, 1, 4, 6, 7, 9]))
#=> [1, 2, 3, 4, 5, 6, 7, 9]

print(sort_it([5, 3, 2, 1, 4, -1, 6, 0, 7, 9]))
#=> [-1, 0, 1, 2, 3, 4, 5, 6, 7, 9]


###########
# Task 3b #
###########

# Time complexity of sort_it:
