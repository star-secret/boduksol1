import coordinate_split as cs
import random as rd
import sensorlocation as sl

class area:
    def __init__(self, boundary_list):
        self.cordlist = boundary_list.split(" ")

    def makearea(self):
        cordxlist = []
        cordylist = []
        cs.split_coord3(self.cordlist, cordxlist, cordylist)

        max_cordx = max(cordxlist)
        min_cordx = min(cordxlist)
        max_cordy = max(cordylist)
        min_cordy = min(cordylist)

        rand_x = rd.randint(min_cordx, max_cordx)
        rand_y = rd.randint(min_cordy, max_cordy)

        return "(" +str(rand_x) + "," + str(rand_y)+ ")"





    def propercordinate(self):
        interest_list = []
        sensor_xy = []
        sensorlist = []
        i = 0
        while True:
            sensorlist.append(self.makearea())
            param = sl.inner_discrimination(self.cordlist, [sensorlist[i]], interest_list, sensor_xy)
            if param == 2:
                print(sensorlist[i])
                return sensorlist[i] #string (x,y) 형태여서 coordinate_split으로 고쳐주자
                break
            interest_list = []
            sensor_xy = []
            i=i+1


        #print(sensorlist)

