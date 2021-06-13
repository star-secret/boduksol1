import random


def random_nextMove_change1(move):
    random_index=random.randrange(0,9)
    if(move[random_index] == 0):
        move[random_index] = 1
    elif(move[random_index] == 1):
        move[random_index] = 0
    return move
"""
def random_nextMove_change2(move):
    for k in range(len(move)):
        random_index_one=random.randrange(0,9)
        random_index_two=random.randrange(0,9)
        if(move[k][random_index_one] == 0):
            move[k][random_index_one] = 1
        elif(move[k][random_index_one] == 1):
            move[k][random_index_one] = 0
        if(move[k][random_index_two] == 0):
            move[k][random_index_two] = 1
        elif(move[k][random_index_two] == 1):
            move[k][random_index_two] = 0
    return move
"""