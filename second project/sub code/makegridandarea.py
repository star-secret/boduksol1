cordlist = input("관심영역 좌표를 입력하시오.\n").split(" ")

def makeinterestregion():
    cordxlist = []
    cordylist = []

    for i in cordlist:
        cordlista = i.split(",")
        cordxlist.append(int(cordlista[0]))
        cordylist.append(int(cordlista[1]))

    return cordxlist,cordylist

def makegrid():
    cordxlist = []
    cordylist = []

    for i in cordlist:
        cordlista = i.split(",")
        cordxlist.append(int(cordlista[0]))
        cordylist.append(int(cordlista[1]))

    tempxmax = 0
    tempxmin = 10000
    tempymax = 0
    tempymin = 10000
    for k in cordxlist:
        if tempxmax < k:
            tempxmax = k

        if tempxmin > k:
            tempxmin = k

    for m in cordylist:
        if tempymax < m:
            tempymax = m

        if tempymin > m:
            tempymin = m

    print(tempxmin - 10, tempymax + 10)
    print(tempxmin - 10, tempymin - 10)
    print(tempxmax + 10, tempymax + 10)
    print(tempxmax + 10, tempymin - 10)

    return (tempxmin, tempxmax, tempymin, tempymax)


