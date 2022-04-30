
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
f4 = Fitter("pika",[2,4,5,8], True, False)
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

    return arr
sort_comp = []
nested_arr(stations, sort_comp)
print(sort_comp)

# function that tries every combination of single element in the stations list but only one name per station
def try_combination(st, arr):
    # clear arr
    arr.clear()
    # loop through all the stations
    for i in range(len(st)):
        # add every fitter.name based on shared competency to the array
        for fitter in fitters:
            if fitter.present == True: # if the fitter is present
                for station in fitter.competency:
                    if station == st[i]:
                        arr.append(fitter.name)
    return arr
try_combination(stations, sort_comp)
print(sort_comp)
