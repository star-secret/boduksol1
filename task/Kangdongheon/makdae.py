size=list(map(int,input().split()))
""" 
왜 이렇게 선언하면 안될까?

ppopgie=list([[0]*size[1]]*size[0])

"""
ppopgie = []
for i in range(size[0]):
        ppopgie.append([0]*size[1])
gaetsu=int(input())
for i in range(gaetsu):
    makdae=list(map(int,input().split()))
    if makdae[1]==0:
        for j in range(int(makdae[0])):
            ppopgie[int(makdae[2])-1][int(makdae[3])+j-1]=1
    else:
        for j in range(int(makdae[0])):
            ppopgie[int(makdae[2])+j-1][int(makdae[3])-1]=1
for i in range(size[0]):
        for j in range(size[1]):
            if ppopgie[i][j]==1:
                print(chr(152), end='')
            else:
                print(chr(153), end='')
        print("")