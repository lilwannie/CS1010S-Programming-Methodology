#
# CS1010S --- Programming Methodology
#
# Mission 9 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###############
# Pre-defined #
###############

a = [6, 4, 2, 9, 10, 4, 2, 1, 3]

###################
# Helper function #
###################

def accumulate(fn, initial, seq):
    if not seq: # if seq is empty
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

###########
# Task 1a #
###########

# The enumerate function should be helpful for you here.
# It takes in a sequence (either a list or a tuple)
# and returns an iteration of pairs each of which
# contains the index of the element and the element itself.
# Here's how to use it.

# for i, elem in enumerate((4, 10, 1, 3)):
#     print("I am in the", i ,"position and I am", elem)
# 
# I am in the 0 position and I am 4
# I am in the 1 position and I am 10
# I am in the 2 position and I am 1
# I am in the 3 position and I am 3

'''
Write a search function that takes in a value x and a sorted sequence (either a tuple
or a list) and returns the position that the value should go to by iterating through the
elements of the sequence starting from the first element. The position that x should
go to in the list should be the first position such that it will be less than or equal to
the next element in the list. (4 marks)
Here are some examples.
>>> search (-5, (1, 5, 10 ))
0
'''

def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == () or seq == []:
        return 0
    else: #Not an empty seq
        position = 0 
        for i, elem in enumerate(seq):
            if x <= elem:
                break
            elif x > elem:
                position += 1
                continue
            else:
                pass
        return position     
                

            


'''
    if seq == () or seq == []:
        return 0
    elif len(seq) == 1: # If not an empty case
        if seq[0] < x:
            return 1 
        else:
            return 0
    else:
        return search(x,seq[0]) + search(x,seq[1:])
'''        
            
       
    

print("## Q1a ##")
print(search(-5, (1, 5, 10)))
# => 0
print(search(3, (1, 5, 10)))
# => 1
print(search(7, [1, 5, 10]))
# => 2
print(search(5, (1, 5, 10)))
# => 1
print(search(42, [1, 5, 10]))
# => 3
print(search(42, (-5, 1, 3, 5, 7, 10)))
# => 6

###########
# Task 1b #
###########



def binary_search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted.
    Uses O(lg n) time complexity algorithm.
    HINT:
Hint: the lecture contains an implementation for binary search in logn time.
Although it only returns boolean values for whether a list contains x,
we can modify the return statement to fit this question.

Hi, you can try to use the code in the lecture (helper function) and consider cases,
1) empty sequence
2) x smaller than the low or equal to
3) x larger than high
4) the difference between low and high is only 1
5) x smaller than the mid or equal to 6) something else. Hope it's useful :)
    """
    if seq == () or seq == []:
        return 0
    def helper(low,high):
        mid = (low + high) // 2    
        if x <= seq[low]:
            return low 
        elif x > seq[high]:
            return high + 1 
        elif x <= seq[mid]:
            return helper(low,mid-1)
        elif low - high == 1:
            return low     
        else:
            return helper(mid+1, high)
    return helper(0, len(seq)-1)   
 
 
 
 
print("## Q1b ##")
print(binary_search(-5, (1, 5, 10)))
# => 0
print(binary_search(3, (1, 5, 10)))
# => 1
print(binary_search(7, [1, 5, 10]))
# => 2
print(binary_search(5, (1, 5, 10)))
# => 1
print(binary_search(42, [1, 5, 10]))
# => 3
print(binary_search(42, (-5, 1, 3, 5, 7, 10)))
# => 6


""" Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted.
    Uses O(lg n) time complexity algorithm.
    HINT:
Hint: the lecture contains an implementation for binary search in logn time.
Although it only returns boolean values for whether a list contains x,
we can modify the return statement to fit this question.

Hi, you can try to use the code in the lecture (helper function) and consider cases,
1) empty sequence
2) x smaller than the low or equal to
3) x larger than high
4) the difference between low and high is only 1
5) x smaller than the mid or equal to 6) something else. Hope it's useful :)
    """
###########
# Task 2a #
###########

def insert_list(x, lst):
    """ Inserts element x into list lst such that x is less than or equal
        to the next element and returns the resulting list."""
    position = binary_search(x, lst)
    lst.insert(position,x)
    return lst 
print("## Q2a ##")
print(insert_list(2, [1, 5, 9]))
#=> [1, 2, 5, 9]
print(insert_list(10, [1, 5, 9]))
#=> [1, 5, 9, 10]
print(insert_list(5, [2, 6, 8]))
#=> [2, 5, 6, 8]

###########
# Task 2b #
###########

def insert_tup(x, tup):
    """ Inserts element x into tuple tup such that x is less than or equal
        to the next element and returns the resulting tuple."""
    position = search(x, tup)
    return tup[:position] + (x,) + tup[position:]

print("## Q2b ##")
print(insert_tup(2, (1, 5, 9)))
#=> (1, 2, 5, 9)
print(insert_tup(10, (1, 5, 9)))
#=> (1, 5, 9, 10)
print(insert_tup(5, (2, 6, 8)))
#=> (2, 5, 6, 8)

###########
# Task 2c #
###########

tup = (5, 4, 10)
output_tup = insert_tup(7, tup)
lst = [5, 4, 10]
output_lst = insert_list(7, lst)

print("## Q2c ##")
print(tup is output_tup)
#=> Output: False
print(tup == output_tup)
#=> Output: False

print(lst is output_lst)
#=> Output: True 
print(lst == output_lst)
#=> Output: True 
#=> Explain the output:
#=>For the case of the insert_tup, a tuple has to be newly created as tuple
#=> is an immutable object, therefore it's identity changed and a new object is created
#=> and by comparing them , they are also not equivalent in the numbers they are pointing 


#=> For insert_lst, the identity holds true since the insertion/modification is on the
#=> pre-existing list and the list would have been updated already as well
#=> Thus both of the outputs expected to be True. 


###########
# Task 3a #
###########

def sort_list(lst):
    """ Sorts list lst in an ascending order."""
    sort = []
    while lst:
        smallest_no = lst[0]
        for number in lst:
            if number < smallest_no:
                smallest_no = number
            else:
                continue 
        lst.remove(smallest_no)
        insert_list(smallest_no, sort)
    
    return sort     
            


print("## Q3a ##")
print(sort_list([9, 6, 2, 4, 5]))
#=> [2, 4, 5, 6, 9]
print(sort_list([42, 7, 6, -42, 0]))
#=> [-42, 0, 6, 7, 42]
print(sort_list(["soda", "cola", "sprite", "root beer", "apple cider"]))
#=> ['apple cider', 'cola', 'root beer', 'soda', 'sprite']
print(sort_list(["turtle", "penguin", "dog", "cat", "ant eater", "butterfly"]))
#=> ['ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle']

###########
# Task 3b #
###########

#=> Time complexity of sort_list: It is O(n^2) by nature already since it involves
#=> looping through the whole lst to remove it and concetante innto the new list
#=> so O(n*n) = O(n**2) 

###########
# Task 3c #
###########

def sort_tup(tup):
    """ Sorts tuple tup in an ascending order."""
    sort = () #empty tuple initialisation 
 #sort_tup((9, 6, 2, 4, 5)) =>	(2, 4, 5, 6, 9)   
    while tup: #Loop through the whole freaking list to find out which number is the smallest 
        for i, number in enumerate(tup):
            smallest_no = tup[i]
            if number < smallest_no:
                smallest_no = number
            else:
                continue  #continue represents relooping, actually no need put but wanna look cool 
        tup = tup[:i] + tup[i+1:]
        sort = insert_tup(smallest_no, sort)
    return sort   

print("## Q3c ##")
print(sort_tup((9, 6, 2, 4, 5)))
#=> (2, 4, 5, 6, 9)
print(sort_tup((42, 7, 6, -42, 0)))
#=> (-42, 0, 6, 7, 42)
print(sort_tup(("soda", "cola", "sprite", "root beer", "apple cider")))
#=> ('apple cider', 'cola', 'root beer', 'soda', 'sprite')
print(sort_tup(("turtle", "penguin", "dog", "cat", "ant eater", "butterfly")))
#=> ('ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle')

###########
# Task 4a #
###########

import shelf

# Please uncomment the test function calls to see the animation

def insert_animate(block_pos, shelf, high):
    """
    Pops the block at block_pos and inserts it in the position in the shelf
    such that its size is less than or equal to the one succeeding it. It searches
    for this position within zero and high.

    NOTE: To actually see the animation, please uncomment the testing function
    below.
    """
    b = shelf.pop(block_pos)
    for i, book in enumerate(shelf[:high]):
        if i == high:
            shelf.insert(high,b)
            return shelf
        if b.size <= book.size:
            shelf.insert(i,b)
            break
        else:
            continue 
    # optional to return shelf but we do this for debugging
    return shelf

# Test cases for insert_animate

def test_insert_animate():
    shelf.clear_window()
    s = shelf.init_shelf((2, 6, 1, 4, 8, 3, 9))
    print("## Q4a ##")
    print(insert_animate(0, s, 0))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(1, s, 1))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(2, s, 2))
    # => [Block size: 1, Block size: 2, Block size: 6, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(3, s, 3))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(6, s, 6))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]

# Uncomment function call to test insert_animate()
test_insert_animate()

###########
# Task 4b #
###########

def sort_me_animate(shelf):
    """
    Maintains a sorted portion and inserts every block in the shelf into the
    sorted portion.
    """
    length = len(shelf)
    for block_pos in range(shelf): #Case of the row
        insert_animate(block_pos, shelf, length)


'''
    length = len(shelf)
    for shelf in range(length):
        for book in range(length):
            insert_animate(book,shelf,length)
'''        
    # optional to return shelf but we do this for debugging
    return shelf


# Test cases for sort_me_animate

def test_sort_me_animate():
    shelf.clear_window()
    s = shelf.init_shelf((5,2,6,9,1,4,8,3))
    print("## Q4b ##")
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 3, Block size: 4, Block size: 5, Block size: 6, Block size: 8, Block size: 9]
    shelf.clear_window()
    s = shelf.init_shelf((4, 8, 2, 9, 3, 1, 2, 3, 4, 10, 7, 5, 6))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 2, Block size: 3, Block size: 3, Block size: 4, Block size: 4, Block size: 5, Block size: 6, Block size: 7, Block size: 8, Block size: 9, Block size: 10]

# Test case to catch mutation while sorting

def test_sort_me_with_duplicates():
    shelf.clear_window()
    s = shelf.init_shelf((1,3,4,1,3,2))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 1, Block size: 2, Block size: 3, Block size: 3, Block size: 4]

# Uncomment function call to test sort_me_animate()
#test_sort_me_animate()
#test_sort_me_with_duplicates()
