import coordinate_split as cs

class sel:
    def __init__(self, area_of_interest_list, sensor_position_list, area_of_interest_xy, sensor_position_list_xy):
        self.interest_list = area_of_interest_list
        self.interest_xy = area_of_interest_xy
        self.sensor_pos = sensor_position_list
        self.sensor_pos_xy = sensor_position_list_xy

    # left_discrimination(정수 기반):
    def left_discrimination(self, x1, y1, x2, y2, x, y):
        if (x - x1 - (y - y1) * (x2 - x1) / (y2 - y1) < 0):
            return 1
        else:
            return 0

    def inner_discrimination(self):
        cs.split_coord1(self.interest_list, self.interest_xy)
        cs.split_coord1(self.sensorpos, self.sensorpos_xy)

        for i in self.sensorpos_xy:
            count = 0
            for j in range(len(self.interest_xy)):
                if(j == len(self.interest_xy-1)):
                    if (self.interest_xy[j][1] <= i[1] <= self.interest_xy[0][1]) or (
                            self.interest_xy[j][1] >= i[1] >= self.interest_xy[0][1]):
                        if self.left_discrimination(self.interest_xy[j][0], self.interest_xy[j][1], self.interest_xy[0][0], self.interest_xy[0][1], i[0], i[1]) == 1:
                            count = count + 1

                else:
                    if (self.interest_xy[j][1] <= i[1] <= self.interest_xy[j + 1][1]) or (
                            self.interest_xy[j][1] >= i[1] >= self.interest_xy[j + 1][1]):
                        if self.left_discrimination(self.interest_xy[j][0], self.interest_xy[j][1], self.interest_xy[j + 1][0], self.interest_xy[j + 1][1], i[0], i[1]) == 1:
                            count = count + 1

            if count % 2 == 0:
                return 1
                print('센서가 관심영역 밖에 있습니다')
            else:
                return 2
                print('센서가 배치되었습니다.')

