# Class of object called name that contains name, balance, present and placed
class Fitter:
    def __init__(self, name, competency, present, placed):
        self.name = name
        self.competency = competency
        self.present = present
        self.placed = placed

f1 = Fitter("karen",[], False, False)
f2 = Fitter("eye",[], False, False)
f3 = Fitter("dani",[], False, False)
f4 = Fitter("pika",[], False, False)


fitters = []

# Add the all the object fitters in a loop
fitters.append(f1)
fitters.append(f2)
fitters.append(f3)
fitters.append(f4)


f3.name = "charlie"
print(f3.name)

# check in a loop if the name is charle and change it to shitface
for fitter in fitters:
    if fitter.name == "charlie":
        fitter.name = "shitface"
        print(fitter.name)



