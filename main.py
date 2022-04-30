# Class of object called name that contains name, balance, present and placed
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


possibleCombos = []




f1 = Fitter("karen",[2,3,4,8], True, False)
f2 = Fitter("eye",[2,3,4,8], True, False)
f3 = Fitter("dani",[2,3,8], True, False)
f4 = Fitter("pika",[2,4,5,8], True, False)
f5 = Fitter("man",[9], True, False)

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


stations = []

# append every element in each team.station to the stations list
for team in teams:
    for station in team.station:
        stations.append(station)
print(stations)




# Add the all the object fitters in a loop
fitters.append(f1)
fitters.append(f2)
fitters.append(f3)
fitters.append(f4)
fitters.append(f5)


f3.name = "charlie"
print(f3.name)

# check in a loop if the name is charle and change it to shitface
for fitter in fitters:
    if fitter.name == "charlie":
        fitter.name = "shitface"
        print(fitter.name)

st = stations
tm = []

# If the fitter is present and the competency is in the st list and the fitter is not in the tm list add the fitter to the tm list 
for fitter in fitters:
    if fitter.present == True:
        for station in st:
            if station in fitter.competency:
                if fitter not in tm:
                    tm.append(fitter)
                    

                
# print every fitter.name in the list
for fitter in tm:
    print(fitter.name)
