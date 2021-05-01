def makearea():
    cordlist = input("좌표를 입력하시오.\n").split(" ")
    cordxlist = []
    cordylist = []

    for i in cordlist:
        cordlista = i.split(",")
        cordxlist.append(int(cordlista[0]))
        cordylist.append(int(cordlista[1]))

    tempxmax = 0
    tempxmin = 0
    tempymax = 0
    tempymin = 0
    for k in cordxlist:
        if tempxmax < k:
            tempxmax = k

        if tempxmin > k:
            tempxmin = k

    for m in cordylist:
        if tmepymax < m:
            tempymax = m
        
        if tempymin > m:
            tempymin = m

    print(tempxmin - 10, tempymax + 10)
    print(tempxmin - 10, tempymin - 10)
    print(tempxmax + 10, tempymax + 10)
    print(tempxmax + 10, tempymin - 10)

def splitarea():
    detectlist = input("탐지범위를 입력하시오.\n").split(" ")
    for i in dectectlist:
        



