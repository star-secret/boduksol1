#딕셔너리
# 연관된 값을 묶어서 저장하는 용도로 사용한다.

lux = {'health' : 500, 'mana' : 300, 'melee': 550, 'armor':16}
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
#키 값에는 문자열, 정수, 실수, 불 모두 가능
#value에는 리스트, 딕셔너리 모두 가능

#딕셔너리 형성 방법
x={}
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux2 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux3 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
#zip 내장함수의 개념
#반복가능한 개체를 요소 순서대로 튜플로 반환한다.
#lux3 = dict([('health',490)...])


#딕셔너리의 키에 접근할 때는 딕셔너리 뒤에 [ ](대괄호)를 사용하며 [ ] 안에 키를 지정해주면 됩니다.
lux1['health']=490
#health key 에 접근하여 490으로 변경

#딕셔너리에 키가 있는 지 확인하기
'health' in lux
# ->boolean 값을 반환한다.

#딕셔너리 키 개수 구하기
len(lux)

#딕셔너리 조작하기
#딕셔너리의 중요한 기능 중 하나가 키값 쌍 추가이다.
#두가지 방법으로 추가가능하다.

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
#키만 추가
x.setdefault('e')
#키와 값 추가
x.setdefault('f',100)
#값 수정 update는 키가 없어도 setdefault처럼 사용된다.
x.update(a=90)
x.update(a=900, f=60)
#update는 키가 문자열일때만 사용할 수 있다. 키가 숫자일 경우
y.update({1: 'ONE', 3: 'THREE'})
y.update([[2, 'TWO'], [4, 'FOUR']])
y.update(zip([1, 2], ['one', 'two']))

#딕셔너리에서 키값 삭제하기
x.pop('a')
del x['a']
#삭제하려고 했는데 키가 없을 경우 기본값을 반환하고 싶을때
x.pop('z', 0)
#모든 키,값 삭제
x.clear()
#딕셔너리 키, 값 가져오기
x.get('a')
x.keys()
x.values()


#for 반복문을 사용해서 딕셔너리 생성
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

#오류코드
for key, value in x.items():
    if value == 20:    # 값이 20이면
        del x[key]     # 키-값 쌍 삭제

#for문으로 삭제하는 것이 아니라 20이 아닌 값들을 새로 딕셔너리 생성
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value!=20}

#중첩 딕셔너리 계층형 데이터를 저장하자
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8

#딕셔너리 복사
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy
#중첩 딕셔너리는 deepcopy로 해야함
import copy
y = copy.deepcopy(x)