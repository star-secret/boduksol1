
num = list(range(10))       # range를 이용해서 list를 만들 수 있다
print(num)
num = list(range(5,9))
print(num)
num = list(range(10,0,-2))      
print(num)
num = [10, 20, 30]      # list는 []를 이용해서 만들 수 있다
a = []; b = list()      # 빈 리스트를 만드는 방법


print(num.index(20))    #20의 위치를 알려줌 = 특정 값의 인덱스를 알 수 있다
print("list의 요소의 개수 : "+ str(len(num)))       # 리스트에 들어있는 요소의 개수를 알 수 있다



name = ["sky", "sky", "blue", "sky"]
print(name.count("sky"))        # 리스트에 몇 번 등장하는지 알 수 있다

num = [4,2,3,6,1,7,5]
num.sort()          # 리스트 정렬 가능
print(num)
num.sort(reverse=True)  #리스트의 값을 큰 순서대로 정렬
print("큰 순서대로 정렬 : "+str(num))

num.reverse()       # 순서 뒤집기 가능
print(num)

num.clear()         # 빈 리스트로 만들기 = 리스트의 모든 요소를 삭제
print(num)

                    
a = [10,20,30]
a.append(40)        # 리스트에 값을 추가하기 리스트의 제일 마지막에 추가가 된다
a.append([50,60])   # 리스트에 리스트를 추가하기
print(a)

a.extend([70,80])   # 리스트를 확장! 리스트를 추가시키는 것이 아니라 다른 리스트의 각 요소를 연결하여 기존 리스트를 확장 시키는 것
print(a)

a.insert(0,0)       # 리스트의 특정 인덱스에 요소 추가
print(a)

print(a.pop())            #.pop()함수는 맨 뒤의 요소를 제거하고, 제거된 요소를 반환함.
print(a)                  # 제거한 요소가 아예 없어진 것을 알 수 있음

print(a.pop(0))           #리스트에서 특정 인덱스의 요소를 제거할 수 있다
print(a)

a.remove([50,60])         #리스트에서 특정 값을 찾아서 삭제할 수 있다
print(a)

b = a.copy()              #리스트의 복사는 .copy()함수를 써야 한다. b = a형식으로 지정해 버리면 2개의 리스트가 될 것 같지만
                          # 이렇게 해버리면 변수 이름만 다를 뿐 리스트 a와 b는 같은 객체이다. 그래서 b의 요소를 변경하면 a의 요소도 변경된다
                          # 이것은 2개의 리스트가 만들어 진 것이 아니다. 하나의 객체를 공유하는 것이다.

for index, value in enumerate(a):   #enumerate를 이용해 반복문을 이용하면 인덱스도 같이 출력할 수 있다
    print(index, value)             #index는 0부터 시작인데 1부터 시작하는 것처럼 보이게 하려면 그냥 index + 1 하면된다

for id, va in enumerate(a, start = 1):  #이러면 인덱스가 1부터 시작하도록 만든 것이다
    print(id, va)