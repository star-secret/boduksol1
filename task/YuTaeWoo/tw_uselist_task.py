
w,h = map(int, input().split())     #판의 세로 h, 판의 가로 w
n = (int)(input())                    #놓을 막대 수

a = []      # 빈 리스트 생성

for i in range(h+1):      #h번 반복
    line = []           #a리스트의 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(w+1):  #w번 반복
        line.append(0)  #안쪽 리스트에 0이라는 요소가 추가된다. -> w번 추가될 것
    a.append(line)      #a라는 빈 리스트에 요소를 추가

for i in range(n):      #놓을 막대기 수 만큼 반복한다 
    d,e,x,y=map(int,input().split())  #길이, 방향, 좌표가 각각 입력
    for j in range(d):  #만약 방향이 0이면 y좌표에 j값만큼 더한다 그리고 그 배열값만큼 1로 채운다
        if e==0:
            a[x][y+j]=1
        else:a[x+j][y]=1 #방향이 0이 아니면 x좌표에 j값 만큼 더한다 마찬가지로 1로 채움
for i in range(1,w+1): #1 ~ 가로까지
    for j in range(1,h+1):# 1 ~ 세로까지
        print(a[i][j],end=' ') #2차원 배열 출력
    print() #줄바꿈
