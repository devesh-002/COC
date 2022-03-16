import numpy as np
from colorama import init, Fore, Back, Style


class Person:
    def __init__(self, x, y, map, speed, health, attack):
        self.map = map
        self.x = x
        self.y = y
        self.speed = speed
        self.alive = True
        self.direction = 0
        self.health = health
        self.attack = attack
        self.total_health = health
        self.color = Back.LIGHTWHITE_EX
        # self.color needs to be defined
    # 0 is up, 1 is right,2 down and 3 left

    def x_setter(self, x):
        self.x = x

    def y_setter(self, y):
        self.y = y

    def get_map(self):
        return self.map

    def get_x(self):
        return self.x

    def move_down(self):
        self.direction = 2
        last_lett = 0
        map = self.map.map
        check = True
        for i in range(self.x+1, self.x+self.speed+1):
            if(((i >= self.map.row) or (map[i][self.y] != 0))):
                check = False
                last_lett = i-1
                break
        if(check == False):
            self.x = last_lett
            return
        self.x += self.speed
        return

    def move_up(self):
        self.direction = 0
        last_lett = 0

        map = self.map.map
        check = True
        for i in range(self.x-self.speed, self.x):
            if(i < 0 or map[i][self.y] != 0):
                check = False
                last_lett = i+1
                break
        if(check == False):
            self.x = last_lett
            return
        self.x -= self.speed
        return

    def move_left(self):
        self.direction = 3
        last_lett = 0
        map = self.map.map
        check = True
        for i in range(self.y-self.speed, self.y):
            if(i < 0 or map[self.x][i] != 0):
                check = False
                last_lett = i+1
                break

        if(check == False):
            self.y = last_lett
            return
        self.y -= self.speed
        return

    def move_bottom_left(self):
        self.direction = 6
        map = self.map.map
        check = True
        i = self.x
        j = self.y
        for x in range(0, self.speed+1):
            if((x+i) >= self.map.row or (j-x) < 0 or map[i+x][j-x] != 0):
                check = False
                break
        if(check == False):
            return
        self.x += self.speed
        self.y -= self.speed

    def move_bottom_right(self):
        self.direction = 5
        map = self.map.map
        check = True
        i = self.x
        j = self.y
        for x in range(0, self.speed+1):
            if((x+i) >= self.map.row or (j+x) >= self.map.height or map[i+x][j+x] != 0):
                check = False
                break
        if(check == False):
            return
        self.x += self.speed
        self.y += self.speed

    def move_up_left(self):
        self.direction = 7
        map = self.map.map
        check = True
        i = self.x
        j = self.y
        for x in range(0, self.speed+1):
            if((i-x) < 0 or (j-x) < 0 or map[i-x][j-x] != 0):
                check = False
                break
        if(check == False):
            return
        self.x -= self.speed
        self.y -= self.speed

    def move_up_right(self):
        self.direction = 4
        map = self.map.map
        check = True
        i = self.x
        j = self.y
        for x in range(0, self.speed+1):
            if((i-x) < 0 or (j+x) >= self.map.height or map[i-x][j+x] != 0):
                check = False
                break
        if(check == False):
            return
        self.x -= self.speed
        self.y += self.speed

    def move_right(self):
        self.direction = 1
        last_lett = 0
        map = self.map.map
        check = True
        for i in range(self.y+1, self.y+self.speed+1):

            if((i >= self.map.height) or map[self.x][i] != 0):
                last_lett = i-1
                check = False
                break
        if(check == False):
            self.y = last_lett
            return
        self.y += self.speed
        return

    def check_color(self):
        x = self.health/self.total_health
        if(x > 0.5):
            self.color = Back.WHITE
        elif(x <= 0.5 and x > 0.3):
            self.color = Back.YELLOW
        elif(x < 0.3 and x > 0):
            self.color = Back.RED

    def do_attack(self):
        # up
        attack_cords = ()
        if(self.direction == 0 and (self.x == 0 or self.map.map[self.x-1][self.y] == 0)):
            return
        elif(self.direction == 0):
            attack_cords = (self.x-1, self.y)
        # right
        if (self.direction == 1 and (self.y == self.map.height-1 or self.map.map[self.x][self.y+1] == 0)):
            return
        elif(self.direction == 1):
            attack_cords = (self.x, self.y+1)
        # down
        if (self.direction == 2 and (self.x == self.map.row-1 or self.map.map[self.x+1][self.y] == 0)):
            return
        elif(self.direction == 2):
            attack_cords = (self.x+1, self.y)
        # left
        if (self.direction == 3 and (self.y == 0 and (self.y == 0 or self.map.map[self.x][self.y-1] == 0))):
            return
        elif(self.direction == 3):
            attack_cords = (self.x, self.y-1)
        # up-right
        if(self.direction == 4 and (self.x == 0 or self.y == self.map.height-1 or self.map.map[self.x-1][self.y+1] == 0)):
            return
        elif(self.direction == 4):
            attack_cords = (self.x-1, self.y+1)
        # down right
        if(self.direction == 5 and (self.x == self.map.row-1 or self.y == self.map.height-1 or self.map.map[self.x+1][self.y+1] == 0)):
            return
        elif(self.direction == 5):
            attack_cords = (self.x+1, self.y+1)
        # down left
        if(self.direction == 6 and (self.x == self.map.row-1 or self.y == 0 or self.map.map[self.x+1][self.y-1] == 0)):
            return
        elif(self.direction == 6):
            attack_cords = (self.x+1, self.y-1)
        # up left
        if(self.direction == 7 and (self.x == 0 or self.y == 0 or self.map.map[self.x-1][self.y-1] == 0)):
            return
        elif(self.direction == 7):
            attack_cords = (self.x-1, self.y-1)
        # print(attack_cords,self.direction)

        if(self.map.map[attack_cords[0]][attack_cords[1]] == 2):
            self.map.town_hall.health -= self.attack
            if(self.map.town_hall.health <= 0):
                self.map.town_hall = {}
                for i in range(((self.map.row)//2 - 1), (self.map.row)//2+2):
                    for j in range((self.map.height//2)-2, (self.map.height//2)+2):
                        self.map.map[i][j] = 0
            return
        elif(self.map.map[attack_cords[0]][attack_cords[1]] == 5):

            self.map.cannons[attack_cords].health -= self.attack
            if(self.map.cannons[attack_cords].health <= 0):
                self.map.map[attack_cords[0]][attack_cords[1]] = 0
                self.map.cannons.pop(attack_cords)
            return
        else:
            if(attack_cords in self.map.huts):
                self.map.huts[attack_cords].health -= self.attack
                if(self.map.huts[attack_cords].health <= 0):
                    self.map.map[attack_cords[0]][attack_cords[1]] = 0
                    self.map.huts.pop(attack_cords)
            elif(attack_cords in self.map.walls):
                self.map.walls[attack_cords].health -= self.attack
                if(self.map.walls[attack_cords].health <= 0):
                    self.map.map[attack_cords[0]][attack_cords[1]] = 0
                    self.map.walls.pop(attack_cords)
        return


class King(Person):

    def __init__(self, x, y, map, speed, health, attack):
        super().__init__(x, y, map, speed, health, attack)
        self.num = 6

    def leviathan_attack(self):
        buildings_in_range = []
        x_min = max(self.x-7, 0)
        x_max = min(self.x+7, self.map.row)
        y_min = max(self.y-7, 0)
        y_max = min(self.x+7, self.map.height)
        for cannon in self.map.cannons:
            build = self.map.cannons[cannon]
            cord = build.cord
            if(cord[0] >= x_min and cord[0] <= x_max and cord[1] <= y_max and cord[1] >= y_min):
                buildings_in_range.append(build)
        for hut in self.map.huts:
            build = self.map.huts[hut]
            cord = build.cord
            if(cord[0] >= x_min and cord[0] <= x_max and cord[1] <= y_max and cord[1] >= y_min):
                buildings_in_range.append(build)
        for i in range(x_min, x_max):
            for j in range(y_min, y_max):
                if self.map.map[i][j] == 2:
                    buildings_in_range.append(self.map.town_hall)
                    break

        for wall in self.map.walls:
            build = self.map.walls[wall]
            cord = build.cord
            if(cord[0] >= x_min and cord[0] <= x_max and cord[1] <= y_max and cord[1] >= y_min):
                buildings_in_range.append(build)
        for building in buildings_in_range:
            building.health -= self.attack
            cord = building.cord
            if(building.health <= 0):
                if(building.num == 3):
                    self.map.map[cord[0]][cord[1]] = 0
                    self.map.huts.pop(cord)
                elif(building.num == 4):
                    self.map.map[cord[0]][cord[1]] = 0
                    self.map.walls.pop(cord)
                elif(building.num == 5):
                    self.map.map[cord[0]][cord[1]] = 0
                    self.map.cannons.pop(cord)
                elif(building.num == 2):
                    if(self.map.map[cord[0]][cord[1]] == 2):
                        self.map.town_hall = {}
                        for i in range(((self.map.row)//2 - 1), (self.map.row)//2+2):
                            for j in range((self.map.height//2)-2, (self.map.height//2)+2):
                                self.map.map[i][j] = 0


class Barbarian(Person):
    def __init__(self, x, y, map, speed, health, attack):
        super().__init__(x, y, map, speed, health, attack)
# using manhattan distance

    def distance(self, obj):
        barb = np.array((self.x, self.y))
        obj = np.array(obj)
        dist = np.linalg.norm(barb - obj)
        return dist

    def movement(self):
        nearest_building_cords = ()
        nearest_building_num = ()
        nearest_building_distance = 10000
        for hut in self.map.huts:
            dist = self.distance(hut)
            if(dist < nearest_building_distance):
                nearest_building_distance = dist
                nearest_building_cords = hut
                nearest_building_num = 3
        for cannon in self.map.cannons:
            dist = self.distance(cannon)
            if(dist < nearest_building_distance):
                nearest_building_distance = dist
                nearest_building_cords = cannon
                nearest_building_num = 3
        if(self.map.town_hall != {}):
            for i in range(((self.map.row)//2 - 1), (self.map.row)//2+2):
                for j in range((self.map.height//2)-2, (self.map.height//2)+2):
                    dist = self.distance((i, j))
                    if(dist < nearest_building_distance):
                        nearest_building_distance = dist
                        nearest_building_cords = (i, j)
                        nearest_building_num = 2

        # print(nearest_building_num)
        # Target is fixed and now we need it to move to next cell either diagnolly or vertically horizontally depending on the position
        # Algo is to find target cell, check if it is a wall and if not then move there else attack
        # We need to run this every iteration because while running the building might get destroyed and hence it will become an issue.
        if(nearest_building_distance == 1):
            if(nearest_building_cords[0] > self.x):
                self.direction = 2
            elif(nearest_building_cords[0] < self.x):
                self.direction = 0
            elif(nearest_building_cords[1] > self.y):
                self.direction = 1
            else:
                self.direction = 3
            self.do_attack()
            return
        if(nearest_building_cords == None or nearest_building_cords == ()):
            return
        # self.diretion=5
        if(self.x < nearest_building_cords[0] and self.y < nearest_building_cords[1]):

            self.move_bottom_right()
            if(self.map.map[self.x+1][self.y+1] != 0):
                self.do_attack()

        elif(self.x > nearest_building_cords[0] and self.y > nearest_building_cords[1]):
            self.move_up_left()
            if(self.map.map[self.x-1][self.y-1] != 0):
                self.do_attack()

        elif(self.x < nearest_building_cords[0] and self.y > nearest_building_cords[1]):
            self.move_bottom_left()
            if(self.map.map[self.x+1][self.y-1] != 0):
                self.do_attack()
        elif(self.x > nearest_building_cords[0] and self.y < nearest_building_cords[1]):
            self.move_up_right()
            if(self.map.map[self.x-1][self.y+1] != 0):
                self.do_attack()

        elif(self.y > nearest_building_cords[1]):
            self.move_left()
            if(self.map.map[self.x][self.y-1] == 4):
                self.do_attack()
        elif(self.y < nearest_building_cords[1]):
            self.move_right()
            if(self.map.map[self.x][self.y+1] == 4):
                self.do_attack()
        elif(self.y == nearest_building_cords[1] and self.x < nearest_building_cords[0]):
            self.move_down()
            if(self.map.map[self.x+1][self.y] == 4):
                self.do_attack()
        else:
            self.move_up()
            if(self.map.map[self.x-1][self.y] == 4):
                self.do_attack()
        pass
