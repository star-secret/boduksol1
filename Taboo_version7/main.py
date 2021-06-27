import convert_png as cp
import split_area as sa
import make_sensor as ma
import save_png as sp
import split_coordinate as sc
import random as rd
import move_sensor as ms
import judge_sensor as js
import copy

# 변하지 않는 값
area_of_interest_list = []
sensor_list_xy = []
sc.split_coord1(input("관심영역의 좌표를 입력하시오.").split(' '), area_of_interest_list)  # 관심영역 좌표 리스트
# 입력 예시 지금은 정삼각형만 입력해야함 (200,200) (600,200) (400,540)   // (300,200) (400,200) (500,540) (100,540)
detect_range = int(input("센서의 탐지범위를 입력하시오.\n"))  # 센서 탐지범위

basic_png = sp.start(area_of_interest_list, [], detect_range)
basic_png.save_png()
total_pixel_of_interest = cp.convert_return_count("image_test0.png")

# 변수
max_coverage_percent = 0  # 가장 큰 커버율 -> 이 커버율이 100퍼센트가 되면 종료
max_coverage_percent_section = []  # 센서 배치 함수 개수 section 의 커버율

length = 1

# for sensor_number in range(3,8):  # 센서 갯수 -> 초기값은 3부터
sensor_number = 6
area_of_interest_center_coordinate = sa.getCenter("image_test0.png")  # 무게중심 x,y 리스트 반환환
area_of_interest_getContour = sa.getContour(sensor_number, "image_test0.png")  # 윤곽선에 sensor_number 만큼의 점을 뽑는거

area_of_interest_spliced_list = sa.splitList(area_of_interest_getContour, area_of_interest_list,
                                            area_of_interest_center_coordinate, sensor_number)

print(area_of_interest_spliced_list)

for i in area_of_interest_spliced_list:
    make_area_object = ma.area(i)
    sensor_list_xy.append(make_area_object.propercordinate())  # 좌표 뽑기
print("initial sensor list")
print(sensor_list_xy)

basic_png.change_polygon(sensor_list_xy)
basic_png.save_png()
count = cp.convert_return_count("image_test" + str(length) + ".png")
ak = cp.convert_return_portion(count, total_pixel_of_interest)
max_coverage_percent_section.append(ak)
length = length + 1

print(max_coverage_percent_section)


randnumlist = [1,2,3,4,5,6,7,8]
execeptionlist = [1,2,3,4,5,6,7,8]
tempsensor_list_xy = []
key = 0

#count_confirm = 0

for k in range(1,50):
    print(k,"번째")
    tempsensor_list_xy = copy.deepcopy(sensor_list_xy)
    if execeptionlist == []:
        print("더이상 움직일 수 없습니다.")
        break
    print(execeptionlist)
    for i in range(1, sensor_number + 1):

        print("센서 변경 시작")
        for j in range(100):

            if key == 1:
                # print(randnumlist[(randnum - 1) % 8: (randnum + 2) % 8])
                #print((randnum - 1) % 8, (randnum + 2) % 8)
                if randnum == 1:
                    randnum = rd.choice([8, 1, 2])
                elif randnum == 8:
                    randnum = rd.choice([7, 8, 1])
                elif randnum == 7:
                    randnum = rd.choice([6,7,8])

                else:
                    randnum = rd.choice(randnumlist[(randnum - 2) % 8: (randnum + 1) % 8])

            elif key == 0:
                randnum = rd.choice(execeptionlist)

            print(randnum)
            ms.move_coordinate(tempsensor_list_xy[i - 1], randnum)
            param = js.inner_discrimination(area_of_interest_spliced_list[i - 1], tempsensor_list_xy[i - 1])
            #print(param)
            if param == 2:
                break
            else:
                tempsensor_list_xy[i-1] = copy.deepcopy(sensor_list_xy[i-1])


    basic_png.change_polygon(tempsensor_list_xy)
    basic_png.save_png()
    count = cp.convert_return_count("image_test" + str(length) + ".png")
    ak = cp.convert_return_portion(count, total_pixel_of_interest)
    max_coverage_percent_section.append(ak)


    sub = max_coverage_percent_section[length -1] - max_coverage_percent_section[length - 2]

    if sub > 0:
        print(k,"pass")
        sensor_list_xy = copy.deepcopy(tempsensor_list_xy)
        key = 1
        m = max_coverage_percent_section[length-1]
        kasd = length -1
        best_sensor_list_xy = copy.deepcopy(sensor_list_xy)

    else:
        max_coverage_percent_section[length - 1] = max_coverage_percent_section[length - 2]
        try:
            execeptionlist.remove(randnum)
        except:
            pass
        key = 0

    length = length + 1


#print(max(max_coverage_percent_section))
print(max_coverage_percent_section)
print(max(max_coverage_percent_section))
print(m)
print(best_sensor_list_xy)
print(sensor_list_xy)
print(tempsensor_list_xy)
print(kasd)
print(max_coverage_percent_section[kasd])