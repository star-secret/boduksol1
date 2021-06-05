# 동헌이가 짜서 줄거고
import random as rd


def make_coord(food_list,cordxlist,cordylist):
    max_cordx = max(cordxlist)
    min_cordx = min(cordxlist)
    max_cordy = max(cordylist)
    min_cordy = min(cordylist)
    rand_x = rd.randint(int(min_cordx), int(max_cordx))
    rand_y = rd.randint(int(min_cordy), int(max_cordy))

    food_list.append([rand_x, rand_y])
    return food_list