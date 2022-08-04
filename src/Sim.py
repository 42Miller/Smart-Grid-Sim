from Grid import *
from Building import House

house1 = House(1,1)
house2 = House(1,1)
house3 = House(1,1)

grid = Grid()
grid.add(house1)
grid.add(house2)
grid.add(house3)

print(grid.getPowerReq())