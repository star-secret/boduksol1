#입력 예시
#sensor_coordinate=[[30,30],[40,40],[50,50],[50,50]]
#move = [[1, 0, 0, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0],[0, 0, 0, 0, 0, 0, 1, 1, 0]]

def move_coordinate(sensor_coordinate, move):
    length=10
    for i in range(3):
        move_splice = move[3*i:3*i+3]
        if(move_splice == [0,0,0]):
            sensor_coordinate[0]+=length
        elif(move_splice == [0,0,1]):
            sensor_coordinate[0]-=length
        elif(move_splice == [0,1,0]):
            sensor_coordinate[1]-=length
        elif(move_splice == [0,1,1]):
            sensor_coordinate[1]+=length
        elif(move_splice == [1,0,0]):
            sensor_coordinate[0]+=length
            sensor_coordinate[1]-=length
        elif(move_splice == [1,0,1]):
            sensor_coordinate[0]-=length
            sensor_coordinate[1]-=length
        elif(move_splice == [1,1,0]):
            sensor_coordinate[0]+=length
            sensor_coordinate[1]+=length
        elif(move_splice == [1,1,1]):
            sensor_coordinate[0]-=length
            sensor_coordinate[1]+=length
    return sensor_coordinate

#move_coordinate(sensor_coordinate, move)
#print(sensor_coordinate)


