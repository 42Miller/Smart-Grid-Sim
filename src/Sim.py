from Grid import *
import Building
import matplotlib.pyplot as plt
import json
from datetime import date, timedelta

#get range of dates
def getDateRange(start_date, stop_date):
    for i in range(int((stop_date - start_date).days)):
        yield start_date + timedelta(i)

#plot daily use of power over the specified period
def showPowerUsage(grid, start_date, stop_date):
    plot_x = []
    plot_y = []
    for day in getDateRange(start_date, stop_date):
        plot_x.append(day)
        plot_y.append(grid.getPowerDate(day))
    
    #add total power
    plt.figure(num="Total: " + str(round(sum(plot_y))) + " kW-Hrs")
    
    #draw line
    plt.plot(plot_x, plot_y)
    
    #naming the x axis
    plt.xlabel('Date')
    #naming the y axis
    plt.ylabel('Power Used (kW-Hr)')
      
    #title
    plt.title("Power Used from " + start_date.strftime("%a %b %d, %Y") + " to " + stop_date.strftime("%a %b %d, %Y"))
      
    # function to show the plot
    plt.show()


house1 = Building.House()

grid = Grid()
grid.add(house1)
print(grid.getPowerYear())
showPowerUsage(grid, date(2022, 1, 1), date(2023, 1, 1))



# # x axis values
# x = [1,2,3]
# # corresponding y axis values
# y = [2,4,1]
#   
# # plotting the points 
# plt.plot(x, y)
#   
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
#   
# # giving a title to my graph
# plt.title('My first graph!')
#   
# # function to show the plot
# plt.show()