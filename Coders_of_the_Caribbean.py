import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Barell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __init__(self, x, y, rotation, speed, rum):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.speed = speed
        self.rum = rum


counter = 0
# game loop
while True:
    barells = []
    ships = []
    my_ships = []

    my_ship_count = int(input())  # the number of remaining ships
    entity_count = int(input())  # the number of entities (e.g. ships, mines or cannonballs)

    for i in range(entity_count):
        entity_id, entity_type, x, y, arg_1, arg_2, arg_3, arg_4 = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)

        if entity_type == "BARREL":
            barells.append(Barell(x, y))

        elif entity_type == "SHIP" and arg_4 == 1:
            my_ships.append(Ship(x, y, arg_1, arg_2, arg_3))

        elif entity_type == "SHIP" and arg_4 == 0:
            ships.append(Ship(x, y, arg_1, arg_2, arg_3))

    for i in range(my_ship_count):

        my_ship = my_ships[my_ship_count-1]
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # Any valid action, such as "WAIT" or "MOVE x y"
        # or my_ship.rum >= 80
        if (counter == 3 ) and ships:
            counter = 0

            mak = 100
            ma = Ship(0, 0, 0, 0, 0)
            for j in ships:
                foo = math.sqrt((my_ship.x - j.x) ** 2 + (my_ship.y - j.y) ** 2)
                if foo < mak:
                    mak = foo
                    ma = j

            print("FIRE", ma.x, ma.y)

        else:
            mak = 100
            ma = Barell(0, 0)
            for j in barells:
                foo = math.sqrt((my_ship.x - j.x) ** 2 + (my_ship.y - j.y) ** 2)
                if foo < mak:
                    mak = foo
                    ma = j

            counter += 1
            print("MOVE", ma.x, ma.y)
        # for i in barells: print("sss", i.x, i.y, file=sys.stderr)
