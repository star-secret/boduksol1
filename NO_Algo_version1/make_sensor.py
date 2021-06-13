import random as rd
import judge_sensor as sl

class area:
    def __init__(self, boundary_list):
        self.cordlist = boundary_list

    def makearea(self):
        cordxlist = []
        cordylist = []
        #print("test")
        #print(self.cordlist)
        for i in self.cordlist:
            #print(i)
            cordxlist.append(i[0])
            cordylist.append(i[1])

            #print(cordxlist)
            #print(cordylist)

        max_cordx = max(cordxlist)
        min_cordx = min(cordxlist)
        max_cordy = max(cordylist)
        min_cordy = min(cordylist)

        rand_x = rd.randint(min_cordx, max_cordx)
        rand_y = rd.randint(min_cordy, max_cordy)

        return[rand_x,rand_y]


    def propercordinate(self):
        while True:
            sensorlist = self.makearea()
            param = sl.inner_discrimination(self.cordlist, sensorlist)
            if param == 2:
                #print(sensorlist)
                return sensorlist #string (x,y) 형태여서 coordinate_split으로 고쳐주자
                break


#a = area([[200,200], [600,200], [400,540]])
#a.propercordinate()