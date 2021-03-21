import math

X,Y = map(int, input().split())
a,b,c,d = map(int, input().split())
N=int(input())

number=list()       # 모래알 위치 리스트   
cnt = 0             # 테이프 안에 있는 녀석들 세기
distance = list()   # 테이프 안에 없는 녀석들 거리 리스트
number2 = list()    # 테이프 안에 없는 녀석들 리스트

for i in range(N):
    x,y = map(int, input().split())
    number.append([x,y])
    
    #모래알이 테이프에 있는지 판단
    if ((a <= x <=c) & (b <= y <=d)):
        cnt += 1

    #모래알이 테이프에 없을경우 테이프와의 최단거리 계산하고 그것을 distance 리스트에 넣음
    else:
        number2.append([x,y])     #모래알이 테이프에 없을 경우 그 모래알의 좌표를 number2 리스트에 넣음
        if(x < a):
            if(y<b):
                distance.append(math.sqrt(pow(x-a,2)+pow(y-b,2)))
            elif(y>d):
                distance.append(math.sqrt(pow(x-a,2)+pow(y-d,2)))
            else:
                distance.append(a-x)
        elif(a<=x<=c):
            if(y<b):
                distance.append(b-y)
            else:
                distance.append(y-d)     
        else:   
            if(y<b):
                distance.append(math.sqrt(pow(x-c,2)+pow(y-b,2)))
            elif(y>d):
                distance.append(math.sqrt(pow(x-c,2)+pow(y-d,2)))
            else:
                distance.append(x-c)

#테이프에 떼지지 않은 모래알 개수 세기
M = N - cnt
print(M)

#최단거리가 무엇인지 결정
min = distance[0]
for i in range(len(distance)):
    if (min > distance[i]):
        min = distance[i]

#최단거리 출력
print(float(min))

#최단거리와 같은 거리를 지닌 점들을 찾아서 모두 출력
for i in range(len(distance)):    
    if (min == distance[i]):
        print(str(number2[i][0]),str(number2[i][1]))


