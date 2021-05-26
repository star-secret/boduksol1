'''
for문의 구조는 큰 틀에서 다음과 같다
    for (변수) in (변수에 넣을 값):
        반복할 코드

    - for문은 이 구조를 따른다. 변수에 넣을 값을 [0,1,2,3,4]라고 했을 때
    변수에 0이 들어가고 반복할 코드 실행, 1이 들어가고 반복할 코드 실행,
     이렇게 계속 반복되다가 변수에 4가 들어가고 코드 실행하고 반복문이 종료된다
    
'''
for i in [0,1,2,3,4]:   # list를 이용하여 반복할 수 있다
    print(i)

for i in range(1,13,3):  # range를 이용할 수 있다.
    print(i, end = " ")

fruits = ("apple", "orange", "grape")   #튜플을 이용할 수 있다
for fruit in fruits:
    print(fruit)

                                        #역 순서로 출력할 수 있다
for fruit in reversed(fruits):
    print(fruit)