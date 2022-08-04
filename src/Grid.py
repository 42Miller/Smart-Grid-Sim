class Grid:
    def __init__(self):
        self.structures = []
        
    def add(self, building):
        self.structures.append(building)
        
    def getPowerReq(self):
        power_req = 0
        for building in self.structures:
            power_req = power_req + building.getPowerReq()
        return power_req