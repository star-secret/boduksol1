import random

sensor_number=3
length = 9
def create_move(length):

    move_digit = []
    for i in range(length):
        move_digit.append(random.randrange(0,2))

    return move_digit

create_move(length)