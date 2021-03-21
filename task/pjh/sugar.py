h, w = input().split()


first_list=[]
# [[0 0 0 0][0 0 0 0][0 0 0 0][0 0 0 0]]
for i in range(h+1):
    first_list.append([])
    for j in range(w+1):
        first_list[i].append(0)

n = map(int, input())

for i in range(n):
    l, d, x, y = map(int, input.split())
    x-=1
    y-=1
    for j in range(l):
        if d==0:
            first_list[x][y+j]=1
        else:
            first_list[x+j][y]=1

for i in range(h+1):
    for j in range(w+1):
        print(first_list[i][j], end='')
    print()
