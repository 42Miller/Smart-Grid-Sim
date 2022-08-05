import random
import time

class Building:
    def __init__(self):
        pass
        
    #returns power required in (kW-hr)
    def getPowerReq(self):
        return self.power_req
        
        
class House(Building):
    def __init__(self):
        # Average household usage based on data from US Energy Information Administration:
        # https://www.eia.gov/tools/faqs/faq.php?id=96&t=3
        # Value calc'd by us avg consumption / 123.53 million housing units
        # Electricity Only (kW-hr)
        self.electric_only = {}
        self.electric_only["Space_Cooling"] = 1902.37
        self.electric_only["Refrigeration"] = 704.28
        self.electric_only["Cooking"] = 129.52
        self.electric_only["Clothes_Dryers"] = 518.09
        self.electric_only["Freezers"] = 161.90
        self.electric_only["Lighting"] = 477.62
        self.electric_only["Clothes_Washers"] = 89.05
        self.electric_only["Dishwashers"] = 64.76
        self.electric_only["Televisions_and_Related_Equipment"] = 453.33
        self.electric_only["Computers_and_Related_Equipment"] = 291.43
        self.electric_only["Furnace_Fans_and_Boiler_Circulation_Pumps"] = 194.28
        self.electric_only["Other_Uses"] = 4209.50
        
        # Multiple Sources (kW-hr)
        # Percentage is based on electrical energy / total energy for each category
        # https://www.eia.gov/consumption/residential/data/2020/index.php?view=characteristics
        self.multiple_source = {}
        self.multiple_source["Space_Heating"] = 1675.71
        self.multiple_source["percent_Space_Heating"] = 0.4163 #41.63 percent of homes use electricity for space heating
        self.multiple_source["Water_Heating"] = 1424.76
        self.multiple_source["percent_Water_Heating"] = 0.4715
        
        random.seed(time.time())
        self.multiple_source["electric_Space_Heating"] = (random.random() <= self.multiple_source["percent_Space_Heating"])
        self.multiple_source["electric_Water_Heating"] = (random.random() <= self.multiple_source["percent_Water_Heating"])
        
        self.power_req = 0
        for key in self.electric_only.keys():
            self.power_req = self.power_req + self.electric_only[key]
            
        for key in self.multiple_source.keys():
            if not key.startswith("percent") and not key.startswith("electric"):
                self.power_req = self.power_req + self.multiple_source[key] * self.multiple_source["electric_" + key]
        
        Building.__init__(self)
