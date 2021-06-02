import coordinate_split as cs
import random as rd


class area:
    def __init__(self, boundary_list):
        self.cordlist = boundary_list.split(" ")

    def makearea(self):
        cordxlist = []
        cordylist = []
        cs.split_coord2(self.cordlist, cordxlist, cordylist)

        max_cordx = max(cordxlist)
        min_cordx = min(cordxlist)
        max_cordy = max(cordylist)
        min_cordy = min(cordylist)

        rand_x = rd.randint(min_cordx, max_cordx)
        rand_y = rd.randint(min_cordy, max_cordy)

        return str(rand_x) + str(rand_y)