#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv
from math import ceil 
##########
# Task 1 # #OKAY! 
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

'''
_map = map
def map(fn, x):
    return tuple(_map(fn, x))
    
'''

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)
    #obtain rep_title
    rep_title = map(int,rows[0][1:]) #rep_title q. easy, just the first row only
    #to obtain data and age_title, we need to loop the whole damn rows
    #hence,
    data, age_title = (), () #initialise first with empty tuple 
    for row in rows[1:]:
        age_title = age_title + (int(row[0]),)
        data = data + (map(int, row[1:]),)
    return create_table(data, age_title, rep_title)    

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

print("## Q1 ##")
# Sit-up score of a 24-year-old who did 10 sit-ups.
print(access_cell(situp_table, 24, 10))    # 0

#Push-up score of a 18-year-old who did 30 push-ups.
print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 # #WELL DONE! 
##########

def pushup_score(pushup_table, age, pushup):
    "Your Solution Here"
    if pushup > 60: #Only need to cover the case when pushup exceeds 60! 
        return 25
    elif pushup == 0:
        return 0 
    else: #otherwise, just access_cell 
        return access_cell(pushup_table, age, pushup)
    

def situp_score(situp_table, age, situp):
    #Only need to cover the case when situp exceeds 60 and when situp == 0 
    "Your Solution Here"
    if situp > 60:
        return 25 
    elif situp == 0:
        return 0
    else: 
        return access_cell(situp_table, age, situp)
    

def run_score(run_table, age, run):
    "Your Solution Here"
    if run < 510:
        return 50
    elif run > 1100:
        return 0
    else:
        modified_run_time = ceil(run/10) * 10 #for e.g 721, 725 will both be converted into the 730, the next tenth placing.
        return access_cell(run_table, age, modified_run_time)
        

print("## Q2 ##")
print(pushup_score(pushup_table, 18, 61))   # 25
print(pushup_score(pushup_table, 18, 70))   # 25
print(situp_score(situp_table, 24, 0))      # 0

print(run_score(run_table, 30, 720))        # 36
print(run_score(run_table, 30, 725))        # 35
print(run_score(run_table, 30, 735))        # 35
print(run_score(run_table, 30, 500))        # 50
print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    "Your Solution Here"
    if score < 51:
        return 'F'
    elif (score >= 51 and score <= 60):
        return 'P'
    elif (score >= 61 and score <= 74):
        return 'P$'
    elif (score >=75 and score <= 84):
        return 'S'
    else:
        return 'G'

print("## Q3 ##")
print(ippt_award(50))     # F
print(ippt_award(51))     # P
print(ippt_award(61))     # P$
print(ippt_award(75))     # S
print(ippt_award(85))     # G


##########
# Task 4 # #COMPLETED ; WELL DONE 
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    "Your solution here"
    # I need to combine the pushup, situp and run scores to get the ippt_award(score)
    pushup_table = get_pushup_table(ippt_table)
    situp_table = get_situp_table(ippt_table)
    run_table = get_run_table(ippt_table)
    pushup_points =  pushup_score(pushup_table, age, pushup)
    situp_points = situp_score(situp_table, age, situp)
    run_points = run_score(run_table, age, run)
    total_ippt_score = pushup_points + situp_points + run_points
    ippt_award_string = ippt_award(total_ippt_score)


    return (total_ippt_score, ippt_award_string)
    
    

print("## Q4 ##")
print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        "Your solution here"
        # My objective is to:
        # Get the improved pushup, situp and run values maybe use floor divide 
        # run the values to get ippt_results
        # return a tuple of improved pushup, situp, run_values and a nested tuple of ippt results

        #pushup
        new_pushup = pushup + (days//rate_pushup)
        #situp
        new_situp = situp + (days//rate_situp)
        #run
        new_run = run - (days//rate_run)

        #get ippt award string using ippt_results
        ippt_award_string = ippt_results(ippt_table,age, new_pushup, new_situp, new_run)

        return (new_pushup, new_situp, new_run, ippt_award_string)

    return training_program

print("## Q5 ##")
tp = make_training_program(7, 3, 10)
print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        "Your solution here"
        #pushup
        new_pushup = pushup + (days//rate_pushup)
        pushup_diff = days//rate_pushup
        #situp
        new_situp = situp + (days//rate_situp)
        situp_diff = days//rate_situp
        #run
        new_run = run - (days//rate_run)
        run_diff = days//rate_run

        #only can one at a time
        '''

        if pushup_diff < 1 and situp_diff < 1 and run_diff < 1:
            return (pushup, situp, run, ippt_results(ippt_table,age, pushup, situp, run))
        elif pushup_diff >= situp_diff and situp_diff <= run_diff:
            return (new_pushup, situp, run, ippt_results(ippt_table,age, new_pushup, situp, run))
        elif pushup_diff <= situp_diff and situp_diff >= run_diff:
            return (pushup, new_situp, run, ippt_results(ippt_table,age, pushup, new_situp, run))
        elif run_diff >= pushup_diff and run_diff >= situp_diff:
            return (pushup, situp, new_run, ippt_results(ippt_table,age, pushup, situp, new_run))
        elif pushup_diff == situp_diff == run_diff:
            return (new_pushup, situp, run, ippt_results(ippt_table,age, new_pushup, situp, run))
        elif pushup_diff == situp_diff and pushup_diff > run_diff:
            return (new_pushup, situp, run, ippt_results(ippt_table,age, new_pushup, situp, run))
        elif situp_diff == run_diff and situp_diff > pushup_diff:
            return (pushup, new_situp, run, ippt_results(ippt_table,age, pushup, new_situp, run))       
        '''
        

    return tp_bonus

tp_bonus = make_tp_bonus(7, 3, 10)



# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))
