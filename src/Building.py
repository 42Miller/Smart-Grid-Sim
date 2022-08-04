class Building:
    def __init__(self, area_sqr_ft, vol_cubic_ft):
        self.area = area_sqr_ft
        self.volume = vol_cubic_ft
        self.power_req = 100
        
    def getPowerReq(self):
        return self.power_req
        
        
class House(Building):
    pass