x = {}      #빈 딕셔너리
y = dict()  #빈 딕셔너리
print(x)        
print(y)        


hotel = {501 : "국", 501 : "방", "VVIP" : "Me"}     #dictionary는 이렇게 키와 값의 형태로 이루어져 있다
        #하나의 키와 값이 세트이고 이 세트는 ,로 구분해 준다
        #dictionary의 키에는 모든 자료형을 사용할 수 있지만, 리스트와 딕셔너리를 키 값으로 사용할 수는 없다
print(hotel[501])       #키 값이 중복일 때는 가장 뒤의 키 값만 사용한다는 것을 알 수 있다
print(hotel["VVIP"])
print(hotel.get("VVIP"))        #.get()일 이용해서도 키로부터 값을 얻을 수 있다
        #[]으로 값을 불러올 때와의 차이 : []로 불러올 때 만약 없는 값을 불러오면 프로그램이 종료되지만,
        #  .get()을 이용해 없는 값을 불러오면 프로그램이 종료되지 않고 None이라 출력된다
print(hotel.get(1,"없음"))  # 찾는 키 값이 없을 때 이 문구가 출력되도록 프로그래밍함

print(501 in hotel)     # 키 값이 딕셔너리에 있는지 확인
print(500 in hotel)
print(len(hotel))       # 키의 개수 ( 키와 값은 1:1 관계)

exam = dict(a=300)  #dict(키=값)으로 딕셔너리를 이용할 때 키 값에는 '' or ""을 사용하면 안된다.
                        # 이 경우 자동으로 키 값은 문자열 취급하기 때문
print(exam.get("a"))

exam[500] = 100         # 딕셔너리에 요소를 추가할 수 있다
print(exam)

del exam[500]           # 딕셔너리의 요소를 지울 수 있다
print(exam)

print(hotel.keys())     # key값들만 출력
print(hotel.values())   # value값들만 출력

print(hotel)            # key와 value 모두 출력
print(hotel.items())    # key와 value 모두 출력

hotel.clear()           # dictionary의 요소를 모두 없앰
print(hotel)