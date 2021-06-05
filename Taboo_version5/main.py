import convert_png as cp
import split_area as sa
import make_sensor as ma
import save_png as sp
import split_coordinate as sc

#변하지 않는 값
area_of_interest_list = []
sc.split_coord1(input("관심영역의 좌표를 입력하시오.").split(' '), area_of_interest_list) #관심영역 좌표 리스트
#입력 예시 지금은 정삼각형만 입력해야함 (200,200) (600,200) (400,540)           // (286,39) (515,408) (58,410)
detect_range = int(input("센서의 탐지범위를 입력하시오.\n")) #센서 탐지범위

basic_png = sp.start(area_of_interest_list,[],detect_range)
basic_png.save_png()
total_pixel_of_interest = cp.convert_return_count("image_test0.png")

#변수
sensor_number = 6#센서 갯수 -> 추후 변경
max_coverage_percent = 0 #가장 큰 커버율 -> 이 커버율이 100퍼센트가 되면 종료
max_coverage_percent_section = 0 #센서 배치 함수 개수 section의 커버율

area_of_interest_center_coordinate = sa.getCenter("image_test0.png") #무게중심 x,y 리스트 반환환
area_of_interest_getContour= sa.getContour(sensor_number,"image_test0.png") #윤곽선에 sensor_number만큼의 점을 뽑는거
area_of_interest_spliced_list = sa.splitList(area_of_interest_getContour,area_of_interest_list,area_of_interest_center_coordinate,sensor_number)

#print(area_of_interest_spliced_list)

sensor_list_xy = []
for i in area_of_interest_spliced_list:

    make_area_object = ma.area(i)
    sensor_list_xy.append(make_area_object.propercordinate())  #좌표 뽑기
    print(sensor_list_xy)



'''
for i in boundary_list:
    for k in range(0,sensor_number):
        #"area" + str(k) = msp.area(i)

#areak.propercordinate()

sensor_list = areak.makearea()
while(max_coverage_percent != 100):
    for i in sensor_list:

    break


#sensor_position_list = []
#sensor_position_list = 어떤 애가 sensor 위치 무작위로 배열하는 그런게 있겠지 업데이트 될 듯

#구간을 나누고
#반복문 하나 돌때마다 나누는 갯수를 늘려
#구간 나누는 함수가 필요하고

#a = sl.sel(area_of_interest_list, sensor_position_list, area_of_interest_list_xy, sensor_position_list_xy)
#a.inner_discrimination()  #이 값이 1을 return 하면 그대로 가는거고 이 값이 2를 return하면 다시 loop를 돌게끔 해야함



#cp.convert("image_test0.png",total_pixel_of_interest)
#cp.convert("image_test1.png",total_pixel_of_interest)


'''
''''''