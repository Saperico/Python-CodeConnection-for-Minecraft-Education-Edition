import numpy as np
from requester import Requester
from Directions import Directions

class Agent:
    def __init__(self):
        self.coordinates = [0, 0, 0]
        self.req = Requester()

    def move(self, direction):
        params = {'direction': direction.value}
        info = self.req.send("/move",params)
        return_code = info.json().get('sucess')
        if(return_code == True):
            self.coordinates[0] = self.coordinates[0]+1
        return return_code

    def turn(self, direction):
        params = {'direction': direction.value}
        info = self.req.send("/turn",params)
        return_code = info.json().get('sucess')
        return return_code
    
    #inventory slots are between 1-28
    def place(self, direction, inventory_slot):
        params = {'direction': direction.value, 'slotNum' : inventory_slot}
        info = self.req.send("/place",params)
        return_code = info.json().get('sucess')
        return return_code

    def till(self, direction):
        params = {'direction': direction.value}
        info = self.req.send("/till",params)
        return_code = info.json().get('sucess')
        return return_code

    def attack(self, direction):
        params = {'direction': direction.value}
        info = self.req.send("/attack",params)
        return_code = info.json().get('sucess')
        return return_code

    def collect(self, item):
        params = {'item': item.value}
        info = self.req.send("/collect",params)
        return_code = info.json().get('sucess')
        return return_code
    
    def drop(self, direction, inventory_slot):
        params = {'direction': direction.value, 'slotNum' : inventory_slot}
        info = self.req.send("/drop",params)
        return_code = info.json().get('sucess')
        return return_code
    
    def dropall(self, direction):
        params = {'direction': direction.value}
        info = self.req.send("/dropall",params)
        return_code = info.json().get('sucess')
        return return_code

    def detect(self, direction):
        params = {'direction': direction.value}
        info = self.req.send("/detect",params)
        return_code = info.json().get('result')
        return return_code

    def inspect(self, direction):
        params = {'direction': direction.value}
        info = self.req.send("/inspect",params)
        return_code = info.json().get('blockName')
        return return_code

    def inspectdata(self, direction):
        params = {'direction': direction.value}
        info = self.req.send("/inspectdata",params)
        return_code = info.json().get('data')
        return return_code
    
    def detectredstone(self, direction):
        params = {'direction': direction.value}
        info = self.req.send("/detectredstone",params)
        return_code = info.json().get('result')
        return return_code

    def getitemdetail(self,  inventory_slot):
        params = {'slotNum': inventory_slot.value}
        info = self.req.send("/getitemdetail",params)
        return_code = info.json().get('itemName')
        return return_code
    
    def getitemspace(self,  inventory_slot):
        params = {'slotNum': inventory_slot.value}
        info = self.req.send("/getitemspace", params)
        return_code = info.json().get('spaceCount')
        return return_code

    def getitemcount(self,  inventory_slot):
        params = {'slotNum': inventory_slot.value}
        info = self.req.send("/getitemcount", params)
        return_code = info.json().get('stackCount')
        return return_code

    def transfer(self,  inventory_slot_1, item_count, inventory_slot_2):
        params = {'srcslotNum': inventory_slot_1.value , 'quantity': item_count, 'dstlotNum': inventory_slot_2}
        info = self.req.send("/transfer", params)
        return_code = info.json().get('success')
        return return_code
    
    def tptoplayer(self):
        self.req.send("/tptoplayer")
        
a = Agent()
i = 0
a.move(Directions.UP)
while(True):
    print(a.move(Directions.FORWARD))
    a.turn(Directions.LEFT)
    for j in range(i):
        print(a.move(Directions.FORWARD))
        print(a.place(Directions.LEFT,1))
        
    i = i +1