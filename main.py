
from xml.etree.ElementInclude import include


class Fitter:
    def __init__(self, name, competency, present, placed):
        self.name = name
        self.competency = competency
        self.present = present
        self.placed = placed

# Class of objects called Team that contains teamname, station and fitter
class Team:
    def __init__(self, teamname, station, fitter):
        self.teamname = teamname
        self.station = station
        self.fitter = fitter


f1 = Fitter("karen",[2,3,4,8], True, False)
f2 = Fitter("eye",[2,3,4,8], True, False)
f3 = Fitter("dani",[2,3,8], True, False)
f4 = Fitter("pika",[2,3,4], True, False)
f5 = Fitter("man",[5], True, False)

t1 = Team("team1", [8], [])
t2 = Team("team2", [2], [])
t3 = Team("team3", [3], [])
t4 = Team("team4", [4,5], [])

fitters = []
teams = []

teams.append(t1)
teams.append(t2)
teams.append(t3)
teams.append(t4)


# function that returns an array of all the stations
def get_stations(st):
    # remove every element in stations
    st.clear()
    # add all the stations to stations
    for team in teams:
      for station in team.station:
        st.append(station)
    return st

# append every element in each team.station to the stations list
stations = []
get_stations(stations)
print(stations)

# Add the all the object fitters in a loop
fitters.append(f1)
fitters.append(f2)
fitters.append(f3)
fitters.append(f4)
fitters.append(f5)

# function that returns an array of all the fitters in group of their competency
def nested_arr(st, arr):  
    # clear arr
    arr.clear()
    # loop through all the stations
    for i in range(len(st)):
        arr.append([])
        # add every fitter.name based on shared competency to the array
        for fitter in fitters:
            if fitter.present == True: # if the fitter is present
                for station in fitter.competency:
                    if station == st[i]:
                        arr[i].append(fitter.name)
        # if a station is empty, add None to the array
        if len(arr[i]) == 0:
            arr[i].append(None)
    
        
                    

    return arr
sort_comp = []
nested_arr(stations, sort_comp)
print(sort_comp)
 

# function that rotates a array a given number of times
def rotate_arr(arr, n):
    from collections import deque
    # create a deque
    d = deque()
    # loop through the array
    for i in range(len(arr)):
        # add the elements to the deque
        d.append(arr[i])
    # loop through the number of rotations
    for i in range(n):
        # remove the first element and add it to the end
        d.append(d.popleft())
    # loop through the deque
    for i in range(len(d)):
        # add the deque elements to the array
        arr[i] = d[i]
    return arr

# function to check if there is duplicate in an array
def check_duplicate(arr):
    # create a set
    s = set()
    # loop through the array
    for i in range(len(arr)):
        # add the elements to the set
        s.add(arr[i])
    # check if the size of the set is equal to the length of the array
    if len(s) == len(arr):
        return False
    else:
        return True

# function that returns every first sub element of a nested array
def get_first_item_to_arr(arr):
    # create a new array
    new_arr = []
    # loop through the array
    for i in range(len(arr)):
        # add the first element to the new array
        # if arr[i][0] is empty
        if arr[i] == [None]:
            new_arr.append('0')
        else:
            new_arr.append(arr[i][0])
    return new_arr

def try_combo(arr):
    import itertools
    new_arr = []
    '''
    count = len(arr)
    new_arr = []
    
    if [None] in arr: # if there is a None in the array
        return "Shiet"
    # loop through all the stations
    for k in range(len(arr)):
        rotate_arr(arr[k], 1)  
        # loop trough all the elements in the array
        for i in range(len(arr[k])):
            temp_list = get_first_item_to_arr(arr)      # get the first element of each sub array
            if check_duplicate(temp_list) == False:     # if there is no duplicate
                print(temp_list)
            else:
                rotate_arr(arr[k], 1)                    # rotate the array
                print(temp_list)'''
    count = 0
    for combination in itertools.product(*arr):
        if check_duplicate(combination) == False:     # if there is no duplicate                
            new_arr.append(combination)
            count += 1
    return new_arr

            
        


print(try_combo(sort_comp))
import itertools

a = [1]
b = [2,3]
c = [4,5,6]

args = [a,b,c]
print(args)
for combination in itertools.product(*args):
    print (combination)