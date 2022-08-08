class Grid:
    def __init__(self):
        self.structures = []
        
    def add(self, building):
        self.structures.append(building)
        
    def getPowerYear(self):
        power_req = 0
        for building in self.structures:
            power_req = power_req + building.getPowerYear()
        return power_req
    
    def getPowerDate(self, date):
        power_req = 0
        for building in self.structures:
            power_req = power_req + building.getPowerDate(date)
        return power_req