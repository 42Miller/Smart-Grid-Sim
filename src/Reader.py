import csv
import random
from datetime import datetime
import time
import matplotlib.pyplot as plt

# FILENAME = "C:/Users/User/Desktop/Smart-Grid-Sim/data/house2_power_blk1.csv"
COLORS = ['red', 'darkorange', 'orange', 'gold', 'yellow', 'limegreen', 'green', 'teal', 'blue', 'indigo', 'purple', 'mediumvioletred']
LINES = ['solid', 'dashed', 'dotted', 'dashdot']
DAYS = {"SUN":0, "MON":1, "TUE":2, "WED":3, "THU":4, "FRI":5, "SAT":6}
        


def createVariants(source_filepath, num_variants, percent_variation, target_filepath):
    count = 1
    while count <= num_variants:
        #read source file
        random.seed(time.time())
        with open(source_filepath) as fin:
            output = ""
            csv_reader = csv.reader(fin, delimiter=",")
            row_num = -1
            for row in csv_reader:
                row_num = row_num + 1
                #if first row, this is the header
                if row_num == 0:
                    #save headers
                    headers = row
                    for h in range(len(headers)):
                        output = output + str(headers[h])
                        if h == len(headers)-1:
                            output = output + "\n"
                        else:
                            output = output + ","
                else:
                    for i in range(len(row)):
                        if not i == 0:  
                            offset = random.uniform(1-percent_variation, 1+percent_variation)
                            output = output + str(int(row[i])*offset)
                            if i == len(row)-1:
                                output = output + "\n"
                            else:
                                output = output + ","
                        else:
                            output = output + str(row[i]) + ","
        #print(output)
        #write to file
        if target_filepath.upper().endswith(".CSV"):
            output_filepath = target_filepath[:-4] + str(count) + ".csv"
        else:
            output_filepath = target_filepath + str(count) + ".csv"
            
        with open(output_filepath, "wt") as fout:
            fout.write(output)
    
    print("Done.")
        
    
#not working yet
def readSection(start_index, end_index, file_pointer, percent_variation):
    output = ""
    csv_reader = csv.reader(file_pointer, delimiter=",")
    for row_index in range(start_index, end_index+1):
        #if first row, this is the header
        if row_index == 0:
            #save headers
            headers = csv.reader[row_index]
            for h in range(len(headers)):
                output = output + str(headers[h])
                if h == len(headers)-1:
                    output = output + "\n"
                else:
                    output = output + ","
        else:
            for i in range(len(csv.reader[row_index])):
                if not i == 0:  
                    offset = random.uniform(1-percent_variation, 1+percent_variation)
                    output = output + str(int(row[i])*offset)
                    if i == len(row)-1:
                        output = output + "\n"
                    else:
                        output = output + ","
                else:
                    output = output + str(row[i]) + ","
    return output
    
    

#     data = [] #data[day][header][time]
#     day_dup = [False, False, False, False, False, False, False]
        
#     #load source file
#     with open(source_filepath) as fptr:
#         csv_reader = csv.reader(fptr, delimiter=",")
#         row_num = -1
#         for row in csv_reader:
#             row_num = row_num + 1
#             current_day = "None"
#             #if first row, this is the header
#             if row_num == 0:
#                 #save headers
#                 headers = row
#                 #init data
#                 for day in range(7):
#                     array = []
#                     for time in range(len(headers)-1):
#                         array.append([])
#                     data.append(array)
#                 print(data)
#                         
#                     
#             else:
#                 #check if day is beginning
#                 timestamp = int(row[0])
#                 current_time = int(row[0][:-5])
#                 if (datetime.fromtimestamp(timestamp).strftime("%H:%M.%S") == "00:00.00") or (current_day == "None"):
#                     start_time = current_time
#                     if current_day != "None":
#                         day_dup[DAYS[current_day]] = True
#                     current_day = datetime.fromtimestamp(timestamp).strftime("%a").upper()
# 
#                 
#                 #add to day average
#                 if current_day != "None":
#                     time_diff = current_time - start_time
#                     for col in range(len(headers)-1):
#                         #check if current day already has data
#                         if day_dup[DAYS[current_day]]:
#                             data[int(DAYS[current_day])][int(col)][int(time_diff)] = int(row[col+1])
#                         else:
#                             #print("data[%d][%d][%d] = %d" % (int(DAYS[current_day]), int(col), int(time_diff), int(row[col+1])))
#                             data[int(DAYS[current_day])][int(col)].append(int(row[col+1]))
#                             #print(data)
#                         
#     #print(data)
#     #data is loaded, now create variations
#     for v in num_variations:
        




def displayPowerUsage(filename):
    with open(filename) as fptr:
        csv_reader = csv.reader(fptr, delimiter=",")
        row_num = -1
    #     current_date = datetime.fromtimestamp(int(list(csv_reader)[1][0])).strftime("%a %d %b %Y")
        current_date = ""
        x = []
        y_arrays = [[]]
        count = 0
        num_days = 0
        for row in csv_reader:
            row_num = row_num + 1
            if row_num == 0:
                headers = row
                print(headers)
                for n in range(len(headers)-1):
                    y_arrays.append([])
            else:
                if datetime.fromtimestamp(int(row[0])).strftime("%a %d %b %Y") != current_date:
                    num_days = num_days + 1
                    current_date = datetime.fromtimestamp(int(row[0])).strftime("%a %d %b %Y")
                    print(datetime.fromtimestamp(int(row[0])).strftime("%a %d %b %Y   %H:%M.%S"))
                    print("Showing " + str(int(count/(5*60))) + "/" + str(count) + " data points.")
                    try:
                        c = 0
                        for i in range(len(headers)-1):
                            plt.plot(x, y_arrays[i], color = COLORS[c%len(COLORS)], linestyle = LINES[int(c/len(COLORS))%len(LINES)], label=headers[i+1])
                            c = c + 1
                            y_arrays[i].clear()
                        plt.legend()
                        plt.show()
                        x.clear()
                    except Exception as e:
                        print(e)
                    count = 0
                else:
                    count = count + 1
                    if count % (5*60) == 0:
                        x.append(datetime.fromtimestamp(int(row[0])).strftime("%a %d %b %Y   %H:%M.%S"))
                        base = 0
                        for i in range(len(headers)-1):
                            y_arrays[i].append(base + int(row[i+1]))
                            base = base + int(row[i+1])

# createVariants("C:/Users/User/Desktop/Smart-Grid-Sim/data/test.csv", 1, 0.1, "C:/Users/User/Desktop/Smart-Grid-Sim/data/output.csv")
displayPowerUsage("C:/Users/User/Desktop/Smart-Grid-Sim/data/house1_power_blk1.csv")
# displayPowerUsage("C:/Users/User/Desktop/Smart-Grid-Sim/data/output1.csv")