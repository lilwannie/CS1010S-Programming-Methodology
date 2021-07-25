# CS1010S --- Programming Methodology
# Mission 0

############################################################################
# Note that written answers are commented out to allow us to run your code #
# easily while grading your problem set.                                   #
#                                                                          #
# The expected answer is what you think the line of code will produce if   #
# it were to be run in IDLE.                                               #
#                                                                          #
# The final answer is the actual output after running the line of code.    #
# You may leave the final answer blank if the output is what you expected. #
############################################################################

############################################################################
# The first line has already been uncommented for you.                     #
# If a line causes an error, you should leave it commented out.            #
#                                                                          #
# Just press F5 to run this file in IDLE.                                  #
# On Mac, the shortcut for running your script is <fn> + F5 or <cmd> + F5. #
# In some Windows systems, it may be <fn> + F5 or <ctrl> + F5.             #
############################################################################

##########
# Task 1 #
##########

print(42)
# expected answer:42
# final answer:

print(0000)
# expected answer:0000
# final answer:0

print("the force!")
# expected answer:the force!
# final answer:

print("Hello World")
# expected answer:Hello World
# final answer:

#print "Hello World"
# expected answer:Hello World
# final answer:Missing parentheses in call to 'print'. Did you mean print("Hello World")?

print(6 * 9)
# expected answer:54
# final answer:

print(2 + 3)
# expected answer:5
# final answer:

print(2 ** 4)
# expected answer:16
# final answer:

print(2.1**2.0)
# expected answer:4.41
# final answer:

print(15 > 9.7)
# expected answer:True
# final answer:

print((5 + 3) ** (5 - 3))
# expected answer:64
# final answer:

print(--4)
# expected answer:4
# final answer:

print(1 / 2)
# expected answer:0.5
# final answer:

print(1 / 3)
# expected answer:0.3333333333333333
# final answer:

#print(1 / 0)
# expected answer:Error
# final answer:ZeroDivisionError: division by zero

print(7 / 3 == 7 / 3.0)
# expected answer:True
# final answer:

print(3 * 6 == 6.0 * 3.0)
# expected answer:True
# final answer:

print(11 % 3)
# expected answer:2
# final answer:

print(2 > 5 or (1 < 2 and 9 >= 11))
# expected answer:False
# final answer:

print(3 > 4 or (2 < 3 and 9 > 10))
# expected answer:False
# final answer:

print("2" + "3")
# expected answer:23
# final answer:

print("2" + "3" == "5")
# expected answer:False
# final answer:

print("2" <= "5")
# expected answer:True
# final answer:

print("2 + 3")
# expected answer:2 + 3
# final answer:

print("May the force" + " be " + "with you")
# expected answer:May the force be with you
# final answer:

print("force"*2)
# expected answer:forceforce
# final answer:

print('daw' in 'padawan')
# expected answer:True
# final answer:

a, b = 3, 4 # Do not comment this line

print(a)
# expected answer:3
# final answer:

print(b)
# expected answer:4
# final answer:

a, b = b, a # Do not comment this line

print(a)
# expected answer:b
# final answer:4

print(b)
# expected answer:a
# final answer:3

#print(red == 44)
# expected answer:False
# final answer:NameError: name 'red' is not defined

red, green = 44, 43 # Do not comment this line

print(red == 44)
# expected answer:True
# final answer:

#print(red = 44)
# expected answer:Error
# final answer:TypeError: 'red' is an invalid keyword argument for print()

print("red is 1") if red == 1 else print("red is not 1")
# expected answer:red is not 1 
# final answer:

print(red - green)
# expected answer:1
# final answer:

purple = red + green # Do not comment this line

print("purple")
# expected answer:87
# final answer:purple

print(red + green != purple + purple / purple - red % green)
# expected answer:False
# final answer:

print(green > red)
# expected answer:False
# final answer:

print("green bigger") if green > red else print("red equal or bigger")
# expected answer:red equal or bigger
# final answer:

print(green + 5)
# expected answer:48
# final answer:

print(round(3.8))
# expected answer:4
# final answer:

print(int(3.8))
# expected answer:3
# final answer:

#############################################################
# The following 4 questions are to ensure that you have     #
# installed PILLOW, matplotlib, scipy, and numpy correctly. #
# Do not worry about the syntax.                            #
# Just uncomment the line --- from <package> import *       #
# and observe the output (if any)                           #
#############################################################

from PIL import *
# expected answer: Not sure
# final answer:

from matplotlib import *
# expected answer:Not sure
# final answer:

from scipy import *
# expected answer:Not sure
# final answer:

from numpy import *
# expected answer:Not sure 
# final answer:
