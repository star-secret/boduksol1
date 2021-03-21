size = list(map(int,input().split()))
tapejapyo = list(map(int,input().split()))
gaetsu: int = int(input())
morae = [list(map(int,input().split()))for _ in range(gaetsu)]
tapemorae=0
shortestdist=size[0]*size[1]
closestmorae=[]
"""
이거 테이프에 붙은 모래원소 제거하고 검사할 모래원소수 하나 줄여주는식으로 for 돌리는건데 왜 list index out of range 에러가 뜨는지 모르겠네

tempgaetsu=gaetsu
for i in range(tempgaetsu):
    if tapejapyo[0]<=morae[i][0]<=tapejapyo[2] and tapejapyo[1]<=morae[i][1]<=tapejapyo[3]:
        tapemorae+=1
        tempgaetsu-=1
        del morae[i]
"""
i=0
print(len(morae))
while i<len(morae):
    if tapejapyo[0] <= morae[i][0] <= tapejapyo[2] and tapejapyo[1] <= morae[i][1] <= tapejapyo[3]:
        tapemorae += 1
        del morae[i]
    i+=1

print(gaetsu-tapemorae)
def bigyo(i,dist):
    global shortestdist
    if dist<shortestdist:
        shortestdist=dist
        closestmorae.clear()
        closestmorae.append(morae[i])
    elif dist==shortestdist:
        closestmorae.append(morae[i])

def disthamsu1(i,temptapejapyo):
    return abs(morae[i][0]-temptapejapyo)
def disthamsu2(i,temptapejapyo):
    return abs(morae[i][1]-temptapejapyo)
def disthamsu3(i):
    a=pow(float(pow((morae[i][0]-tapejapyo[0]),2)+pow((morae[i][1]-tapejapyo[1]),2)),1/2)
    b=pow(float(pow((morae[i][0]-tapejapyo[0]),2)+pow((morae[i][1]-tapejapyo[3]),2)),1/2)
    c=pow(float(pow((morae[i][0]-tapejapyo[2]),2)+pow((morae[i][1]-tapejapyo[1]),2)),1/2)
    d=pow(float(pow((morae[i][0]-tapejapyo[2]),2)+pow((morae[i][1]-tapejapyo[3]),2)),1/2)
    return min(a,b,c,d)
for i in range(gaetsu-tapemorae):
    if morae[i][0]<tapejapyo[0] and tapejapyo[1]<morae[i][1]<=tapejapyo[3]:
        bigyo(i,disthamsu1(i,tapejapyo[0]))
    elif morae[i][0]>tapejapyo[2] and tapejapyo[1]<morae[i][1]<tapejapyo[3]:
        bigyo(i,disthamsu1(i,tapejapyo[2]))
    elif morae[i][1]<tapejapyo[1] and tapejapyo[0]<morae[i][0]<tapejapyo[2]:
        bigyo(i,disthamsu2(i,tapejapyo[1]))
    elif morae[i][1]>tapejapyo[3] and tapejapyo[0]<morae[i][0]<tapejapyo[2]:
        bigyo(i,disthamsu2(i,tapejapyo[3]))
    else:
        bigyo(i,disthamsu3(i))
print(format(shortestdist, ".6f"))
for i in range(len(closestmorae)):
    print(closestmorae[i][0],closestmorae[i][1],end="")