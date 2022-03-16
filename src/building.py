from colorama import init, Fore, Back, Style
import numpy as np


class building():
    def __init__(self, num, damage, cord, health, map, king, color) -> None:
        self.num = num
        self.damage = damage
        self.cord = cord
        self.health = health
        self.color = color
        self.map = map
        self.king = king
        self.total_health = health
        self.save_this = color
        self.doing_attack = False

    def check_color(self):
        x = self.health/self.total_health
        if(x > 0.5):
            self.color = self.save_this
        elif(x <= 0.5 and x > 0.3):
            self.color = Back.LIGHTCYAN_EX
        elif(x < 0.3 and x > 0):
            self.color = Back.RED
        # elif(x<=0):
        #     self.map.map[self.cord[0]][self.cord[1]]=0

    def distance(self, obj):
        barb = np.array((self.cord[0], self.cord[1]))
        obj = np.array(obj)
        dist = np.linalg.norm(barb - obj)
        return dist

    def attack(self):
        min_dist = 10000
        if(self.king.health > 0):
            min_dist = self.distance((self.king.x, self.king.y))
        troop = self.king
        index = -1
        i = 0
        for barbarian in self.map.barbarians:

            dist = self.distance((barbarian.x, barbarian.y))
            if(dist < min_dist and dist < 10):
                min_dist = dist
                troop = barbarian
                index = i
            i += 1
        # print(troop.health,min_dist)
        if(min_dist < 7 and troop.health >= 0):
            troop.health -= self.damage
            self.doing_attack = True
        else:

            self.check_color()
            self.doing_attack = False
        if(troop.health < 0 and index >= 0):
            del self.map.barbarians[index]
        elif(troop.health < 0 and index == -1):
            self.map.map[self.king.x][self.king.y] = 0
        pass
