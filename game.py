import time
from copy import deepcopy
import colorama
from matplotlib.pyplot import bar
from src.person import *
from src.map_generate import *
from src.input import *
from colorama import Fore, Back, Style
import sys
# from src.variables import *
from src.building import *
from src.spells import *
import os
DIR = 'replays'

file_num = len([name for name in os.listdir(
    DIR) if os.path.isfile(os.path.join(DIR, name))])
filename = str(file_num+1)
filename += ".txt"
script_dir = os.path.dirname(__file__)
rel_path = "replays/"+filename
abs_file_path = os.path.join(script_dir, rel_path)


class Tee(object):
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()  # If you want the output to be visible immediately

    def flush(self):
        for f in self.files:
            f.flush()


f = open(abs_file_path, 'w')

original = sys.stdout
sys.stdout = Tee(sys.stdout, f)


def display_king_health():
    global heal_spell_num
    global rage_spell_num
    # if(king.health<0):
    #     sys.stdout.write("\n")
    char = "King Health: "
    x = int((king.health/king.total_health)*100)
    for i in range(x):
        char += "|"
    sys.stdout.write(Fore.MAGENTA+char)
    print()
    print(Fore.GREEN + "Heal Spell Number: ", heal_spell_num,
          " Rage Spell Number: ", rage_spell_num, "King leviathan attack Num: ", leviathan_attack, end="")
    print(Style.RESET_ALL)


def run():
    global heal_spell_num
    global rage_spell_num
    global leviathan_attack
    kb_inp = KBHit()

    while True:
        input = None
        if(kb_inp.kbhit()):
            input = kb_inp.getch()
        if input is not None:
            # print("input is " ,input)
            if input is 's' and king.health > 0:
                king.move_down()
            if input is 'q':
                exit(0)
            if input is 'w' and king.health > 0:
                king.move_up()
            if input is 'a' and king.health > 0:
                king.move_left()
            if input is 'd' and king.health > 0:
                king.move_right()
            if input is " " and king.health > 0:
                king.do_attack()
            if input is "h" and heal_spell_num > 0:
                heal_spell.func()
                heal_spell_num -= 1
            if input is "r" and rage_spell_num > 0:
                rage_spell.func()
                rage_spell_num -= 1
            if input is "l" and leviathan_attack > 0:
                king.leviathan_attack()
                leviathan_attack -= 1
            if input is "1" and spawn_points[(0, 4)] == True and len(map.barbarians) <= 12:
                # spawn_points[(0,4)]=False
                map.barbarians.append(Barbarian(0, 4, map, 1, 200, 10))

            if input is "2" and spawn_points[(13, 10)] == True and len(map.barbarians) <= 12:
                # spawn_points[(13,10)]=False
                map.barbarians.append(Barbarian(13, 10, map, 1, 200, 10))
            if input is "3" and spawn_points[(13, 3)] == True and len(map.barbarians) <= 12:
                # spawn_points[(13,3)]=False
                map.barbarians.append(Barbarian(13, 3, map, 1, 200, 10))

        render_board()

        time.sleep(sleeper_time)


colour_grid = {0: Back.GREEN, 4: Back.CYAN, 2: Back.YELLOW,
               1: Back.BLACK, 5: Back.RED, 6: Back.LIGHTWHITE_EX, 3: Back.LIGHTRED_EX}
barb_list = {0: "    ", 1: " .  ", 2: " . .", 3: "... ", 4: "⁞   ", 5: "::. ",
             6: " :::", 7: "⋮ ::", 8: " ⋮⋮:", 9: " ⋮⋮⋮", 10: ".⋮⋮⋮", 11: ":⋮⋮⋮", 12: "⋮⋮⋮⋮"}
make_char_list = {0: " ", 1: ".", 2: ":", 3: "⋮", 4: "⁞"}


def check_game_end():
    victory = True
    defeat = True
    if(king.health > 0 or map.barbarians != []):
        victory = False
    if(map.cannons != {} or map.huts != {} or map.town_hall != {}):
        defeat = False
    if(defeat):
        display_king_health()
        if(king.health > 0):
            map.map[king.x][king.y] = 6
        for i in range(map.row):
            for j in range(map.height):
                if(map.map[i][j] == 0):
                    sys.stdout.write(Style.RESET_ALL + Back.GREEN)
                elif(map.map[i][j] == 6):
                    sys.stdout.write(Style.RESET_ALL+king.color)
                else:
                    for wall in map.walls:
                        if(wall == (i, j)):
                            sys.stdout.write(
                                Style.RESET_ALL+map.walls[wall].color)
                            break
                make_char(i, j)
            print(Style.RESET_ALL)
        print("Victory")
        exit(0)
    elif(victory):

        display_king_health()
        for i in range(map.row):
            for j in range(map.height):
                if(map.map[i][j] == 2):
                    sys.stdout.write(Style.RESET_ALL+map.town_hall.color)
                elif(map.map[i][j] == 0):
                    sys.stdout.write(Style.RESET_ALL + Back.GREEN)
                else:
                    for cannon in map.cannons:
                        if(cannon == (i, j)):
                            sys.stdout.write(
                                Style.RESET_ALL+map.cannons[cannon].color)
                            break
                    for hut in map.huts:
                        if(hut == (i, j)):
                            sys.stdout.write(
                                Style.RESET_ALL+map.huts[hut].color)
                            break
                    for wall in map.walls:
                        if(wall == (i, j)):
                            sys.stdout.write(
                                Style.RESET_ALL+map.walls[wall].color)
                            break
                make_char(i, j)
            print(Style.RESET_ALL)
        print("Defeat")
        exit(0)


def make_char(i, j):
    # if(map.map[i][j]==6):
    #     sys.stdout.write(Fore.GREEN+" K  ")
    #     return
    for point in spawn_points:
        if point[0] == i and point[1] == j:
            sys.stdout.write(Fore.YELLOW+"  S ")
            return
    if(map.map[i][j] == 5):
        cannon = map.cannons[(i, j)]

        if cannon.doing_attack == True:
            sys.stdout.write(Fore.CYAN+" || ")
        else:
            sys.stdout.write(Fore.WHITE+" || ")
        return ""
    white = 0
    red = 0
    yellow = 0
    for barbarian in map.barbarians:
        if(barbarian.x == i and barbarian.y == j):
            if(barbarian.color == Back.WHITE):
                white += 1
            elif(barbarian.color == Back.YELLOW):
                yellow += 1
            elif(barbarian.color == Back.RED):
                red += 1
    char = ""
    #     char=""
    appended_times = 0
    while(white > 0):
        x = white % 4
        if(x == 0):
            x = 4
        char += make_char_list[x]
        appended_times += 1
        white -= x
    sys.stdout.write(Fore.WHITE+char)
    char = ""
    while(red > 0):
        x = red % 4
        if(x == 0):
            x = 4
        char += make_char_list[x]
        appended_times += 1
        red -= x
    sys.stdout.write(Fore.RED+char)
    char = ""
    while(yellow > 0):
        x = yellow % 4
        if(x == 0):
            x = 4
        char += make_char_list[x]
        appended_times += 1
        yellow -= x
    sys.stdout.write(Fore.YELLOW+char)
    char = ""
    while(appended_times < 4):
        char += " "
        appended_times += 1
    sys.stdout.write(char)
    return char


def render_board():
    xmap = deepcopy(map.map)
    if(king.health > 0):
        xmap[king.x][king.y] = 6
    check_game_end()
    print()

    display_king_health()
    for i in range(map.row):
        for j in range(map.height):
            if(xmap[i][j] == 2):
                sys.stdout.write(Style.RESET_ALL+map.town_hall.color)
            elif(xmap[i][j] == 0):
                sys.stdout.write(Style.RESET_ALL + Back.GREEN)
            elif(xmap[i][j] == 6):
                sys.stdout.write(Style.RESET_ALL+king.color+Fore.BLUE+"KKKK")
                continue
            else:
                for cannon in map.cannons:
                    if(cannon == (i, j)):
                        sys.stdout.write(
                            Style.RESET_ALL+map.cannons[cannon].color)
                        break
                for hut in map.huts:
                    if(hut == (i, j)):
                        sys.stdout.write(Style.RESET_ALL+map.huts[hut].color)
                        break
                for wall in map.walls:
                    if(wall == (i, j)):
                        sys.stdout.write(Style.RESET_ALL+map.walls[wall].color)
                        break
            # sys.stdout.write(Fore.WHITE+char[0]+Fore.RED+char[1]+Fore.YELLOW+char[2])
            make_char(i, j)
        print(Style.RESET_ALL)

    if(king.health > 0):
        king.check_color()
    if(map.town_hall != {}):
        map.town_hall.check_color()
    for cannon in map.cannons:
        map.cannons[cannon].check_color()
        map.cannons[cannon].attack()
    for hut in map.huts:
        map.huts[hut].check_color()
    for wall in map.walls:
        map.walls[wall].check_color()
    for barbarian in map.barbarians:
        barbarian.movement()
        barbarian.check_color()

    return


def lol(map, king):
    walls = {}
    for i in range(1, map.row-1):
        map.map[i][1] = 4
        map.map[i][map.height-2] = 4
        walls[(i, 1)] = (building(1, 0, (i, 1), 80, map, king, Back.BLACK))
        walls[(i, map.height-2)] = (building(1, 0,
                                             (i, map.height-2), 80, map, king, Back.BLACK))
    for i in range(1, map.height-1):
        map.map[1][i] = 4
        map.map[map.row-2][i] = 4
        walls[(1, i)] = (building(1, 0, (1, i), 80, map, king, Back.BLACK))
        walls[(map.row-2, i)] = (building(1, 0,
                                          (map.row-2, i), 80, map, king, Back.BLACK))

    town_hall = building(2, 0, ((map.row)//2 - 1, map.height //
                         2-2), 200, map, king, Back.BLACK)

    canons = {}
    canons[(map.row//2-2, map.height//2)] = building(5, 25,
                                                     (map.row//2-2, map.height//2), 110, map, king, Back.MAGENTA)
    canons[(map.row//2+2, map.height//2)] = building(5, 25,
                                                     (map.row//2+2, map.height//2), 110, map, king, Back.MAGENTA)
    huts = {}
    huts[(2, 2)] = building(3, 0, (2, 2), 100, map, king, Back.LIGHTBLUE_EX)
    huts[(2, map.height-3)] = building(3, 0,
                                       (2, map.height-3), 100, map, king, Back.LIGHTBLUE_EX)
    huts[(map.row-3, 2)] = building(3, 0, (map.height-3, 2),
                                    100, map, king, Back.LIGHTBLUE_EX)
    huts[(map.row-3, map.height-3)] = building(3, 0,
                                               (map.row-3, map.height-3), 100, map, king, Back.LIGHTBLUE_EX)
    huts[(map.row-4, map.height-4)] = building(3, 0,
                                               (map.row-4, map.height-4), 100, map, king, Back.LIGHTBLUE_EX)
    # huts[(map.row)]
    map.barbarians = []
    # for i in range(5):
    #     map.barbarians.append(Barbarian(0, 4, map, 1, 200, 10))
    barbarian = Barbarian(0, 4, map, 1, 5000, 10)
    map.walls = walls
    map.town_hall = town_hall
    map.cannons = canons
    map.huts = huts


    # map.barbarians=[barbarian]
sleeper_time = 1/4
rage_spell_num = 2
heal_spell_num = 2
leviathan_attack = 1
map = Map(14, 12)
map.initialise_walls()
map.initalise_town_hall()
# map.spawn_point()
map.make_cannon()
map.initialise_huts()
king = King(0, 0, map, 1, 1000, 30)
lol(map, king)
king.map = map
heal_spell = heal(1.5, map, king)
rage_spell = rage(2, map, king)
spawn_points = {(0, 4): True, (13, 10): True, (13, 3): True}
run()
