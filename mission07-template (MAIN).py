# CS1010S --- Programming Methodology
#
# Mission 7 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import datetime
import csv

###############
# Pre-defined #
###############

def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

###############
# Station ADT #
###############

def make_station(station_code, station_name):
    return (station_code, station_name)

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]

test_station1 = make_station('CC2', 'Bras Basah')
test_station2 = make_station('CC3', 'Esplanade')
test_station3 = make_station('CC4', 'Promenade')


############
## Task 1 ##
############

def make_train(train_code):
    ''' Do NOT modify this function'''
    return (train_code,)

test_train = make_train('TRAIN 0-0')

#############
# Task 1a   # #COMPLETED
#############

def get_train_code(train):
    return train[0]


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1A
# print("## Task 1a ##")
# print(get_train_code(test_train))

# Expected Output #
# TRAIN 0-0

#############
# Task 1b   # #COMPLETED 
#############

def make_line(name, stations):
    '''your code here'''
    return (name, stations)

def get_line_name(line):
    '''your code here'''
    return line[0]

def get_line_stations(line):
    '''your code here'''
    return line[1]

def get_station_by_name(line, station_name): #line is assigned by make_line, which returns a tuple of the line name (line[0]) and nested tuple of the stations within (line[1]) 
    '''your code here'''
    for station in get_line_stations(line):
        if station_name == station[1]:
            return station_name
        if station_name == ():
            return None 
                                              # Obtain the tuple of stations within the line 
   
                                               # check station_name exists within the line, notice that for each case the station is denoted like a nested tuple of 
                                               # (('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade')), thus station[1]
    
'''
def make_station(station_code, station_name):
    return (station_code, station_name)

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]

'''
                                             
def get_station_by_code(line, station_code):
    '''your code here'''
    for station in get_line_stations(line):
        if station_code == station[0]:
            return station
    return None     
    

def get_station_position(line, station_code):  
    '''your code here
    station code indexing should start from get_line_stations(line) tuple
    if it exists:
        return the index
    else:
        return -1 '''
    for station in get_line_stations(line):
        if station_code == station[0]:
            index = get_line_stations(line).index(station)
            return index 
    return -1 
''' ALTERNATIVE SOLUTION, ITERATIVE METHOD 
def get_station_position_alternative(line, station_code):
    count = 0
    for x in get_line_stations(line):
        if x[0] == station_code:
            return count
        else:
            count +=1
    return -1

def get_station_position_alternative_2(line, station_code):
    index = 0
    for station in get_line_stations(line):
        if station_code == station[0]:
            return index
        else:
            index += 1
    return -1         
'''           
# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1B
print("## Task 1b ##")
test_line = make_line('Circle Line', (test_station1, test_station2, test_station3))
print(get_line_name(test_line))
print(get_line_stations(test_line))
# print(get_station_by_name(test_line, 'Bras Basah'))
# print(get_station_by_code(test_line, 'CC4'))
# get_station_position(test_line, 'CC3')
# get_station_position_alternative(test_line, 'CC3')
'''
get_station_position takes in a Line and a station code, and returns the index of
Station with the given code inside the Line. The index starts from 0. If there is no
such Station, then it returns -1.'

'''
# Expected Output #
# Circle Line
# (('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade'))
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')
# 1
# 1 

#############
# Task 1c   # #COMPLETED 
#############

def make_train_position(is_moving, from_station, to_station):
    ''' Do NOT modify this function'''
    return (is_moving, from_station, to_station) #Returns a tuple 

def get_is_moving(train_position):
    '''your code here'''
    return train_position[0]

def get_direction(line, train_position): # print(get_direction(test_line, test_train_position1))
    '''0 means that the train is going along the line in ascending order (e.g. CC1 to CC2)
       while 1 means it is going in descending order (e.g. CC2 to CC1).
       While station codes contain running integers, you should not rely on it to determine
       the direction. Instead, you should use the Station sequence stored in the Line object 
       and the given function to get the position of the Station in the Line.'''# test_train_position1 = make_train_position(False, test_station1, test_station2)
    start = get_station_position(line, train_position[1][0])
    end = get_station_position(line, train_position[2][0])

    if start - end < 0:                    #index diff of from_station - to_station < 0:
        return 0
    else:
        return 1 
        

def get_stopped_station(train_position):
    '''your code here'''
    if train_position[0] == True:
        return None
    else:
        return train_position[1]
        

def get_previous_station(train_position):
    '''your code here'''
    if train_position[0] == False:
        return None
    else:
        return train_position[1]

def get_next_station(train_position):
    '''your code here'''
    return train_position[2]


# From previous qn: 
def get_station_position(line, station_code):  
    '''your code here
    station code indexing should start from get_line_stations(line) tuple
    if it exists:
        return the index
    else:
        return -1 '''
    for station in get_line_stations(line):
        if station_code == station[0]:
            index = get_line_stations(line).index(station)
            return index 
    return -1

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1C
# print("## Task 1c ##")
test_train_position1 = make_train_position(False, test_station1, test_station2)
test_train_position2 = make_train_position(True, test_station3, test_station2)
# print(get_is_moving(test_train_position2))
# print(get_direction(test_line, test_train_position1))
# print(get_stopped_station(test_train_position1))
# print(get_previous_station(test_train_position2))
# print(get_next_station(test_train_position2))

# Expected Output #
# True
# 0
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')
# ('CC3', 'Esplanade')

'''
test_station1 = make_station('CC2', 'Bras Basah')
test_station2 = make_station('CC3', 'Esplanade')
test_station3 = make_station('CC4', 'Promenade')
test_line = make_line('Circle Line', (test_station1, test_station2, test_station3))

def make_station(station_code, station_name):
    return (station_code, station_name)

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]
    
'''




#############
# Task 1d   # #COMPLETED 
#############
#datetime.datetime(2017 , 2, 28 , 13 , 5) represents 28 Feb 2017, 1.05 pm.
#Refer to Python's datetime module in Mission 07 PDF   
def make_schedule_event(train, train_position, time):
    '''your code here'''
    return (train, train_position, time) 

def get_train(schedule_event):
    '''your code here'''
    return schedule_event[0]

def get_train_position(schedule_event):
    '''your code here'''
    return schedule_event[1]

def get_schedule_time(schedule_event):
    '''your code here'''
    return schedule_event[2]


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1D
# print("## Task 1d ##")
test_bd_event1 = make_schedule_event(test_train, test_train_position2, datetime.datetime(2016, 1, 1, 9, 27))
test_bd_event2 = make_schedule_event(test_train, test_train_position1, datetime.datetime(2016, 1, 1, 2, 25))
# print(get_train(test_bd_event1))
# print(get_train_position(test_bd_event1))
# print(get_schedule_time(test_bd_event1))

# Expected Output #
# ('TRAIN 0-0',)
# (True, ('CC4', 'Promenade'), ('CC3', 'Esplanade'))
# 2016-01-01 09:27:00


############
## Task 2 ## #DONE 
############

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

#############
# Task 2a   # #DONE 
#############
# the output of parse_lines should look like (line1, line2, ...)
# where line1 and line2 are also tuples
'''
def make_line(name, stations):
    # your code here
    return (name, stations)

def make_station(station_code, station_name):
    return (station_code, station_name)

'''

def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]
    curr_line_stations = () #Only the stations within the current line!!!!!!
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            curr_line_stations = curr_line_stations + (make_station(code, station_name),)
        
        else: # This happens when line_name != curr_line_name, so we add make_line, an overall tuple for all the stations of the particular line 
            # Addition #2
            lines = lines + (make_line(curr_line_name, curr_line_stations),)
            curr_line_name = line_name
            curr_line_stations = (make_station(code, station_name),)                  

    # Addition #3
    lines = lines + (make_line(curr_line_name, curr_line_stations),)
    return lines


#UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2A. THIS IS NOT OPTIONAL TESTING!
LINES = parse_lines('station_info.csv')
CCL = filter(lambda line: get_line_name(line) == 'Circle Line', LINES)[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2A
# print("## Task 2a ##")
# print(get_line_stations(CCL)[5:8])

# Expected Output #
# (('CC6', 'Stadium'), ('CC7', 'Mountbatten'), ('CC8', 'Dakota'))

#############
# Task 2b   # #DONE 
#############

def parse_events_in_line(data_file, line):
    rows = read_csv(data_file)[1:]
    events = ()
    for row in rows:
        # Your code here
        train_code, is_moving, from_code, to_code, date, time = row
        # events = events + ((train_code, is_moving, from_code, to_code, date, time),)
        # Somehow the time needs to be split and formatted???
        x = date.split('/')
        y = time.split(':')
        my_datetime = datetime.datetime(int(x[2]),int(x[1]),int(x[0]),int(y[0]),int(y[1]))
        #datetime.datetime(2017, 1, 6, 7, 9)
        train_pos_tuple =  make_train_position(is_moving, get_station_by_code(line, from_code), get_station_by_code(line, to_code)) 
        event = (make_train(train_code), make_train_position(eval(get_is_moving(train_pos_tuple)), get_station_by_code(line, from_code), get_station_by_code(line, to_code)), my_datetime)
        events = events + (event,)
    return events
'''

def parse_events_in_line(data_file, line):
    rows = read_csv(data_file)[1:]
    events = ()
    for row in rows:
        train_code, is_moving, from_code,to_code,date,time = row
        if is_moving == 'True':
            is_moving = True
        else:
            is_moving = False
        event = make_schedule_event((train_code,),(is_moving,(get_station_by_code(line,from_code)),(get_station_by_code(line,to_code))), datetime.datetime(int(date[6:10]),int(date[3:5]),int(date[0:2]),int(time[0:2]),int(time[3:5])))
        events += (event,)
    return events
'''

     



# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2B. THIS IS NOT OPTIONAL TESTING!
BD_EVENTS = parse_events_in_line('breakdown_events.csv', CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2B
print("## Task 2b ##")
print(BD_EVENTS[9])

# Expected Output #
# (('TRAIN 1-11',), (False, ('CC23', 'one-north'), ('CC22', 'Buona Vista')), datetime.datetime(2017, 1, 6, 7, 9))



############
## Task 3 ##
############


#############
# Task 3a   # #OKAY DONE LIKE FINALLY 
#############
#test_bd_event1 = make_schedule_event(test_train, test_train_position2, datetime.datetime(2016, 1, 1, 9, 27))
#test_train_position1 = make_train_position(False, test_station1, test_station2)
#test_train_position2 = make_train_position(True, test_station3, test_station2)
#get_station_position(line, station_code)

def is_valid_event_in_line(bd_event, line):
    
    get_schedule_string = bd_event[2].ctime() #Making use of the time string function provided in the PDF 
    if get_station_position(line, bd_event[1][1][0]) - get_station_position(line, bd_event[1][2][0]) == 1 or get_station_position(line, bd_event[1][1][0]) - get_station_position(line, bd_event[1][2][0]) == -1: #Adjacency check! 
        if int(get_schedule_string[11:13]) >= 7 and int(get_schedule_string[11:13]) < 23: #can go beyond 7 but cannot go beyond 2300! 
            return True
        elif (int(get_schedule_string[11:13]) == 23 and int(get_schedule_string[14:16]) == 00) :
            return True 
        else:
            return False
    else: #For non-adjacent cases
        return False 
    
    

def get_valid_events_in_line(bd_events, line):
    ''' Do NOT modify this function'''
    return filter(lambda ev: is_valid_event_in_line(ev, line), bd_events)


# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 3A. THIS IS NOT OPTIONAL TESTING!
VALID_BD_EVENTS = get_valid_events_in_line(BD_EVENTS, CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3A
# print("## Task 3a ##")
#print(is_valid_event_in_line(test_bd_event1, CCL))
# print(is_valid_event_in_line(test_bd_event2, CCL))

# Expected Output #
# True
# False
'''
def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

test_bd_event1 = make_schedule_event(test_train, test_train_position2, datetime.datetime(2016, 1, 1, 9, 27))
test_bd_event2 = make_schedule_event(test_train, test_train_position1, datetime.datetime(2016, 1, 1, 2, 25))

'''
#############
# Task 3b   # #DONE, Make use of wishful thinking 
#############

def get_location_id_in_line(bd_event, line):
    '''your code here'''
    station_a_index = get_station_position(line,bd_event[1][1][0])
    station_b_index = get_station_position(line,bd_event[1][2][0])
    if bd_event[1][0] == True:
        if station_a_index > station_b_index:
            return station_b_index + 0.5
        else:
            return station_a_index + 0.5
    else:
        return get_station_position(line,bd_event[1][1][0]) #When stationary, this bd_event[1][0] == False i.e is_moving == False 
  

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3B
print("## Task 3b ##")
test_loc_id1 = get_location_id_in_line(test_bd_event1, CCL)
test_loc_id2 = get_location_id_in_line(test_bd_event2, CCL)
print(test_loc_id1)
print(test_loc_id2)

# Expected Output #
# 2.5
# 1
'''
def get_station_position(line, station_code):  
    your code here
    station code indexing should start from get_line_stations(line) tuple
    if it exists:
        return the index
    else:
        return -1 
    for station in get_line_stations(line):
        if station_code == station[0]:
            index = get_line_stations(line).index(station)
            return index 
    return -1
'''
############
## Task 4 ##
############

# UNCOMMENT the following to read the entire train schedule
FULL_SCHEDULE = parse_events_in_line('train_schedule.csv', CCL)    # this will take some time to run

#############
# Task 4a   #OK
#############
'''In this task, we will write some functions to filter the train schedule. Before we do
that, we would need to read the entire train schedule data. Uncomment the code in the
template file so that the entire train schedule is read using the parse_events function
from Task 2(b) and stored in the global variable FULL_SCHEDULE. Note that this operation
might take some time.
Task 4a: Filter by Time (2 marks)
Implement the function get_schedules_at_time that takes in a tuple of ScheduleEvents and
a Python datetime.datetime. You may assume that the ScheduleEvent given in train_schedule
belongs to the correct Line being evaluated currently. Hence, you do not need to check
if the ScheduleEvent belongs to the current Line.
Your function should return a tuple of ScheduleEvents which occur at the given time.'''

def get_schedules_at_time(train_schedule, time):
    ls = () #Create empty tuple first
    for individual_schedule_event in train_schedule:
        if individual_schedule_event[2] == time:
            ls = ls + (individual_schedule_event,)
        else:
            ls = ls 
    
    
    return ls 

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4A
print("## Task 4a ##")
test_datetime = datetime.datetime(2017, 1, 6, 6, 0)
test_schedules_at_time = get_schedules_at_time(FULL_SCHEDULE[:5], test_datetime)
print(test_schedules_at_time[1])

# Expected Output #
# (('TRAIN 1-0',), (False, ('CC29', 'HarbourFront'), ('CC28', 'Telok Blangah')), datetime.datetime(2017, 1, 6, 6, 0))

#############
# Task 4b   #
#############

'''
Task 4b: Filter by Location (2 marks)
Implement the function get_schedules_near_loc_id_in_line that takes in a tuple of ScheduleEvents
and a location ID as defined in Task 3(b).
Your function should return a tuple of ScheduleEvents whose positions are a maximum
of 0.5 away from the given position in the given Line.

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res


'''

def get_schedules_near_loc_id_in_line(train_schedule, line, loc_id):
    event = ()

    for individual_schedule_event in train_schedule:
        if get_location_id_in_line(individual_schedule_event, line)- loc_id <= 0.5 and get_location_id_in_line(individual_schedule_event, line)- loc_id >= -0.5:
            event = event + (individual_schedule_event,)
        else:
            event = event 
    return event 

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4B
print("## Task 4b ##")
test_schedules_near_loc_id = get_schedules_near_loc_id_in_line(FULL_SCHEDULE[:10], CCL, test_loc_id1)
print(test_schedules_near_loc_id[1])

# Expected Output #
# (('TRAIN 0-0',), (True, ('CC3', 'Esplanade'), ('CC4', 'Promenade')), datetime.datetime(2017, 1, 6, 6, 5))
'''test_loc_id1 = get_location_id_in_line(test_bd_event1, CCL)

def get_location_id_in_line(bd_event, line):
    station_a_index = get_station_position(line,bd_event[1][1][0])
    station_b_index = get_station_position(line,bd_event[1][2][0])
    if bd_event[1][0] == True:
        if station_a_index > station_b_index:
            return station_b_index + 0.5
        else:
            return station_a_index + 0.5
    else:
        return get_station_position(line,bd_event[1][1][0]) #When stationary, this bd_event[1][0] == False i.e is_moving == False 

'''
#############
# Task 4c   # #CLEAR 
#############
'''
Task 4c: Filter by Time and Location (2 marks)
Let’s put the two functions from Tasks 4(a) and 4(b) together. Implement the function
get_rogue_schedules_in_line that takes in a tuple of ScheduleEvents, a Python datetime.datetime
and a position.
Your function should return a tuple of the ScheduleEvents which occur at the given time
and whose location IDs are a maximum of 0.5 away from the given location ID.
Your code must make use of the two functions written earlier. ZERO marks will be awarded
for solutions that do not call get_schedules_at_time and get_schedules_near_loc_id_in_line,
or call and discard the results without using them.

'''

def get_rogue_schedules_in_line(train_schedule, line, time, loc_id):
    time_tuple = get_schedules_at_time(train_schedule, time)
    nearby_loc_id_tuple = get_schedules_near_loc_id_in_line(time_tuple, line, loc_id)
    return nearby_loc_id_tuple

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4C
print("## Task 4c ##")
test_bd_event3 = VALID_BD_EVENTS[0]
test_loc_id3 = get_location_id_in_line(test_bd_event3, CCL)
test_datetime3 = get_schedule_time(test_bd_event3)
test_rogue_schedules = get_rogue_schedules_in_line(FULL_SCHEDULE[1000:1100], CCL, test_datetime3, test_loc_id3)
print(test_rogue_schedules[2])

# Expected Output #
# (('TRAIN 1-11',), (True, ('CC24', 'Kent Ridge'), ('CC23', 'one-north')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 5 ##
############

###############
# Scorer ADT  #
###############

def make_scorer():
    return {}

def blame_train(scorer, train_code):
    scorer[train_code] = scorer.get(train_code, 0) + 1
    return scorer

def get_blame_scores(scorer):
    return tuple(scorer.items())

'''
You do not need to understand how it works, but you do need to know how to use it.
• make_scorer returns a Python dictionary.
• blame_train takes in the Scorer and a train code. It increments the blame score of
the given train (identified by the train code) by 1.
• get_blame_scores takes in the Scorer and returns a nested tuple of train codes and
their corresponding blame scores.

'''


# Use this to keep track of each train's blame score.
SCORER = make_scorer()

#############
# Task 5a   # #PAINFULLY COMPLETED 
#############
'''
Write a function calculate_blame_in_line that takes in the full train schedule tuple and the tuple of valid breakdown events. The function then goes through all the valid breakdown events,
finds which trains were in the vicinity at the time of the breakdown, and assigns 1 point of blame to each nearby train.
The Scorer ADT and all function and ADTs from the previous tasks have already been defined for you.

get_rogue_schedules_in_line(train_schedule, line, time, loc_id)

'''
##(('TRAIN 0-0',), (True, ('CC3', 'Esplanade'), ('CC4', 'Promenade')), datetime.datetime(2017, 1, 6, 6, 5))



def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    # your code here
    for event in valid_bd_events:
        time_frame = get_schedule_time(event)
        loc_id = get_location_id_in_line(event,line)
        rogue_schedules_tuple = get_rogue_schedules_in_line(full_schedule, line, time_frame, loc_id)
        train_code_records = ()
        for individual_rogue_schedule in rogue_schedules_tuple:
            if get_train_code(get_train(individual_rogue_schedule)) not in train_code_records:
                blame_train(scorer,get_train_code(get_train(individual_rogue_schedule)))
                train_code_records = train_code_records + (get_train_code(get_train(individual_rogue_schedule)),)
            else:
                train_code_records = train_code_records
    return scorer






         

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 5A. THIS IS NOT OPTIONAL TESTING!
calculate_blame_in_line(FULL_SCHEDULE, VALID_BD_EVENTS, CCL, SCORER)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5A
print("## Task 5a ##")
print(sorted(get_blame_scores(SCORER))[7])

# Expected Answer
# ('TRAIN 0-5', 2)


'''
Suggested Dauntless Wolf method:
def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    # your code here
    #Establish the rogue_schedules in line, then somehow the train, then blame the train and store it?
    for event in valid_bd_events:
        time_of_event = get_schedule_time(event)
        loc_id = get_location_id_in_line(event, line)
        rogue_schedules = get_rogue_schedules_in_line(full_schedule, line, time_of_event, loc_id)
        train_codes_tuple = ()
        for individual_rogue_event in rogue_schedules:
            if get_train_code(get_train(individual_rogue_event))in train_codes_tuple:
                continue 
            else:
                blame_train(scorer, get_train_code(get_train(individual_rogue_event)))
                train_codes_tuple += (get_train_code(get_train(individual_rogue_event)),)
    return scorer

2nd attempt:
def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    # your code here
    for event in valid_bd_events:
        time_frame = get_schedule_time(event)
        loc_id = get_location_id_in_line(event,line)
        rogue_schedules_tuple = get_rogue_schedules_in_line(full_schedule, line, time_frame, loc_id)
        train_code_records = ()
        for individual_rogue_schedule in rogue_schedules_tuple:
            if get_train_code(get_train(individual_rogue_schedule)) not in train_code_records:
                blame_train(scorer,get_train_code(get_train(individual_rogue_schedule)))
                train_code_records = train_code_records + (get_train_code(get_train(individual_rogue_schedule)),)
            else:
                train_code_records = train_code_records
    return scorer
                      
'''


#############
# Task 5b   #
#############
'''
Write a function find_max_score that takes in a Scorer. Using the map function, and
Python’s built-in max function, return the maximum score.
You should not write your own loops for this task. However, you can use indexing to get
the blame score from each (‘Train Code’, blame_score) tuple

def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

###############
# Scorer ADT  #
###############

def make_scorer():
    return {}

def blame_train(scorer, train_code):
    scorer[train_code] = scorer.get(train_code, 0) + 1
    return scorer

def get_blame_scores(scorer):
    return tuple(scorer.items())


You do not need to understand how it works, but you do need to know how to use it.
• make_scorer returns a Python dictionary.
• blame_train takes in the Scorer and a train code. It increments the blame score of
the given train (identified by the train code) by 1.
• get_blame_scores takes in the Scorer and returns a nested tuple of train codes and
their corresponding blame scores.

    
'''

'''
def find_max_score(scorer):
    #your code here
    blame_score_tuple = get_blame_scores(scorer) 
    max_score = 0
    for element in blame_score_tuple:
        if int(element[1]) > max_score:
            max_score = int(element[1])
        else:
            continue
    return max_score

  def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res
  
'''
def getterfx(tuple_input):
    return tuple_input[1]
      


def find_max_score(scorer):
    return max(map(getterfx, get_blame_scores(scorer)))

    



# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5B
print("## Task 5b ##")
test_max_score = find_max_score(SCORER)
print(test_max_score)

# Expected answer
# 180

#############
# Task 5c   # done 
#############

# UNCOMMENT THE CODE BELOW TO VIEW ALL BLAME SCORES. THIS IS NOT OPTIONAL TESTING!
# print("## Task 5c ##")
# train_scores = get_blame_scores(SCORER)
# print("############### Candidate rogue trains ###############")
# for score in train_scores:
#     print("%s: %d" % (score[0], score[1]))
# print("######################################################")

''' Please type your answer into the Task 5c textbox on Coursemology '''

#############
# Task 5d   #
#############
'''
Task 5d: Find the Rogue Train (2 marks)
Now that we know the maximum “blame score” and have also verified the rogue train
hypothesis, we can finally find the rogue train (programmatically).
Write a function find_rogue_train that takes in the Scorer and the maximum score found
in Task 5(b). The function should return the train code of the rogue train whose score
matches the maximum score



'''
def find_rogue_train(scorer, max_score):
    '''your code here'''
    blame_score_tuple = get_blame_scores(scorer)
    for element in blame_score_tuple:
        if int(element[1]) == max_score:
            return element[0]
        else:
            continue 

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5D
print("## Task 5d ##")
print("Rogue Train is '%s'" % find_rogue_train(SCORER, test_max_score))

# Expected Answer
# Rogue Train is 'TRAIN 0-4'
