import convert_png as cp
import make_sensor as ma
import save_png as sp
import split_coordinate as sc

# 변하지 않는 값
area_of_interest_list = []
#sensor_list_xy = []
sc.split_coord1(input("관심영역의 좌표를 입력하시오.").split(' '), area_of_interest_list)  # 관심영역 좌표 리스트
# 입력 예시 지금은 정삼각형만 입력해야함 (200,200) (600,200) (400,540)           // (286,39) (515,408) (58,410)
detect_range = int(input("센서의 탐지범위를 입력하시오.\n"))  # 센서 탐지범위

basic_png = sp.start(area_of_interest_list, [], detect_range)
basic_png.save_png()
total_pixel_of_interest = cp.convert_return_count("image_test0.png")

# 변수
max_coverage_percent = 0  # 가장 큰 커버율 -> 이 커버율이 100퍼센트가 되면 종료
max_coverage_percent_section = [0]  # 센서 배치 함수 개수 section 의 커버율

count = 1
sensor_count = []
sensor_number = 6
tempobj_portion = 0
print(area_of_interest_list)

#max(max_coverage_percent_section) <= 94

while len(max_coverage_percent_section) <= 7:
    sensor_list_xy = []
    make_area_object = ma.area(area_of_interest_list)
    for i in range(0, sensor_number):
        sensor_list_xy.append(make_area_object.propercordinate())  # 좌표 뽑기

    basic_png.change_polygon(sensor_list_xy)
    basic_png.save_png()
    obj = cp.convert_return_count("image_test" + str(count) + ".png")
    obj_portion = cp.convert_return_portion(obj, total_pixel_of_interest)
    print(obj_portion)

    if obj_portion >= tempobj_portion:
        tempobj_portion = obj_portion
        max_coverage_percent_section.append(tempobj_portion)
        sensor_count.append(count)
        print(count)

    count = count + 1

print(max_coverage_percent_section)
print(max(max_coverage_percent_section))
print(sensor_count)
print(len(max_coverage_percent_section))






