class spell():
    def __init__(self,power,map,king) -> None:
        self.power=power
        self.map=map
        self.king=king

class heal(spell):
    def __init__(self, power, map,king) -> None:
        super().__init__(power, map,king)
    
    def func(self):
        for barbarian in self.map.barbarians:
            if(barbarian.health>0):
                barbarian.health=min(self.power*barbarian.health,barbarian.total_health)
        if(self.king.health>0):
            self.king.health=min(self.power*self.king.health,self.king.total_health)

class rage(spell):
    def __init__(self, power, map,king) -> None:
        super().__init__(power, map,king)
    
    def func(self):
        for barbarian in self.map.barbarians:
            if(barbarian.health>0):
                # barbarian.speed*=self.power
                barbarian.attack*=self.power
        if(self.king.health>0):
            # self.king.speed*=self.power
            self.king.attack*=self.power
    def tone_down(self):
        for barbarian in self.map.barbarians:
            if(barbarian.health>0):
                barbarian.speed/=self.power
                barbarian.attack/=self.power
        if(self.king.health>0):
            self.king.speed/=self.power
            self.king.attack/=self.power
