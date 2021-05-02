gwansimlist = input("관심영역의 좌표를 입력하시오.\n").split(" ")
gwansimxy=[]
haeksimxy=[]
for i in gwansimlist:
    gwansimlista = i.split(",")
    gwansimlista[0]=gwansimlista[0].replace('(','')
    gwansimlista[1] = gwansimlista[1].replace(')','')
    gwansimxy.append([int(gwansimlista[0]),int(gwansimlista[1])])


haeksimlist = input("핵심시설의 좌표를 입력하시오.\n").split(" ")

for i in haeksimlist:
    haeksimlista = i.split(",")
    haeksimlista[0]=haeksimlista[0].replace('(','')
    haeksimlista[1] = haeksimlista[1].replace(')', '')
    haeksimxy.append([int(haeksimlista[0]),int(haeksimlista[1])])

def leftpanbeol(x1,y1,x2,y2,x,y):
    if(x-x1-(y-y1)*(x2-x1)/(y2-y1)<0):
        return 1
    else:
        return 0


for i in haeksimxy:
    count=0
    for j in range(len(gwansimxy)):
        if(j==len(gwansimxy)-1):
            if ((gwansimxy[j][1] <= i[1] and i[1] <= gwansimxy[0][1]) or (gwansimxy[j][1] >= i[1] and i[1] >= gwansimxy[0][1])):
                if(leftpanbeol(gwansimxy[j][0],gwansimxy[j][1],gwansimxy[0][0],gwansimxy[0][1],i[0],i[1])==1):
                    count=count+1
        else:
            if ((gwansimxy[j][1] <= i[1] and i[1] <= gwansimxy[j+1][1]) or (gwansimxy[j][1] >= i[1] and i[1] >= gwansimxy[j+1][1])):
                if (leftpanbeol(gwansimxy[j][0], gwansimxy[j][1], gwansimxy[j+1][0], gwansimxy[j+1][1], i[0], i[1]) == 1):
                    count=count+1
    if(count%2==0):
        print('핵심시설이 관심영역 밖에 있습니다')
    else:
        print('추가 완료')
            #프로그램 종료
