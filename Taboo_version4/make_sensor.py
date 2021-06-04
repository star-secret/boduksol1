import split_coordinate as cs
import random as rd
import judge_sensor_position_main as sl

class area:
    def __init__(self, boundary_list):
        self.cordlist = boundary_list.split(" ")

    def makearea(self):
        cordxlist = []
        cordylist = []
        cs.split_coord3(self.cordlist, cordxlist, cordylist)

        #cs.split_coord1(cordxlist, cordylist)

        max_cordx = max(cordxlist)
        min_cordx = min(cordxlist)
        max_cordy = max(cordylist)
        min_cordy = min(cordylist)

        rand_x = rd.randint(min_cordx, max_cordx)
        rand_y = rd.randint(min_cordy, max_cordy)


        return "("+str(rand_x) + "," + str(rand_y)+")"

    def propercordinate(self):
        interest_list = []
        sensor_xy = []
        sensorlist = []
        sensorlist.append(self.makearea())

        sensor = sl.sel(self.cordlist, sensorlist, interest_list, sensor_xy)

        flag = sensor.inner_discrimination()




#area1 = area('(0,0) (3,0) (3,4) (0,4)')
#area1.propercordinate()