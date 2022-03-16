import numpy as np


class Map:
    def __init__(self, row, height):
        self.row = row
        self.height = height
        self.map = np.zeros((row, height), dtype=int)
        self.spawn_points = 3
        self.huts = {}
        self.cannons = {}
        self.town_hall = {}
        self.walls = {}
        self.barbarians = []

    def return_row(self):
        return self.row

    def return_height(self):
        return self.height

    def initialise_walls(self):
        for i in range(1, self.row-1):
            self.map[i][1] = 4
            self.map[i][self.height-2] = 4
        for i in range(1, self.height-1):
            self.map[1][i] = 4
            self.map[self.row-2][i] = 4

    def initalise_town_hall(self):
        for i in range(((self.row)//2 - 1), (self.row)//2+2):
            for j in range((self.height//2)-2, (self.height//2)+2):
                self.map[i][j] = 2

    def spawn_point(self):
        self.map[0][0] = 1
        self.map[0][self.height-1] = 1
        self.map[self.row-1][self.height-1] = 1

    def make_cannon(self):
        self.map[self.row//2-2][self.height//2] = 5
        self.map[self.row//2+2][self.height//2] = 5

    def initialise_huts(self):
        self.map[2][2] = 3
        self.map[2][self.height-3] = 3
        self.map[self.row-3][2] = 3
        self.map[self.row-3][self.height-3] = 3
        self.map[self.row-4][self.height-4] = 3
