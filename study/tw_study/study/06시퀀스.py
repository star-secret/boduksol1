a = list(range(0,100,10))

#list, tuple,range,문자열과 같이 연속적으로 이루어진 자료형들의 공통적인 특징

#특정 값이 있는지 확인이 가능하다

print(30 in a)
print(57 in a)
print(57 not in a)

b = list(a)
print(a + b)    #같은 자료형끼리면 연결이 가능 (리스트와 튜플 연결은 불가능)

c = (100, 110, 120)
print(a+list(c))    #자료형이 다를경우 바꾸어주면 된다

#시퀸스 객체는 *연산자를 이용한 반복이 가능. 음수를 곱하면 빈 객체가 나오고, 실수는 곱할 수 없다
a = [1,2,3,4,5]
print(a*3)

#요소 개수 구하기
print(len(a))       

name = "Ji Hwan"
#index 기능
print(a[0])
print(c[1])
print(name[1])

#시퀀스 객체는 []로 요소에 접근한 뒤 =로 값을 할당할 수 있다
#범위를 벗어난 인덱스는 지정할 수 없다
a[3] = "A"
print(a)
#튜플의 경우 이렇게 값을 변경하면 오류가 남

#del 이름[인덱스]를 이용해 요소를 삭제할 수 있다
del a[3]
print(a)

#슬라이스 -     이름[시작인덱스:끝인덱스]  
print(a[0:3])

# 슬라이스할 요소를 시작인덱스,끝인덱스, 인덱스 증가폭을 설정해줄 수 있다
a = list(range(15))
print(a[3:11:2])

#슬라이스할 요소를 선택해 그 부분을 바꿀 수 있다
a[3:11:2] = ["Three", "Five", "Seven", "Nine"]
print(a)

#슬라이스할 요소를 선택해 지울 수 있다
del a[:3]
print(a)