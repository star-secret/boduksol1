x, y = map(int,(input().split()))
a, b, c, d = map(int,(input().split()))
n = int(input())

x_list = []
y_list = []
dist = []
count = 0
temp = 0
dist_min = 1000000

for i in range(n):
    x1, y1 = map(int,(input().split()))
    x_list.append(x1)
    y_list.append(y1)
    dist.append(100000)
    #append

for i in range(n):
    if(a<=x_list[i] and x_list[i] <= c and b <= y_list and y_list <= d):
        continue   
    else:
        count+=1
        if(a<= x_list[i] and x_list[i]<=c):
            if(y_list>=d):
                dist[i] = y_list[i] - d
            else:
                dist[i] = b - y_list[i]
        elif(y_list[i] >=b and y_list[i] <= d):
            if(x_list[i] >= c):
                dist[i] = x_list[i]-c
            elif(x_list[i] <= a):
                dist[i] = a - x_list[i]
            else:
                dist[i] = ((a-x_list[i])**2+(b-y_list[i])**2)**0.5
                temp = ((a-x_list[i])**2+(d-y_list[i])**2)**0.5
                if (dist[i]>=temp):
                    dist[i] = temp
                temp = ((c-x_list[i])**2+(b-y_list[i])**2)**0.5
                if(dist[i]>=temp):
                    dist[i] = temp
                temp = ((c-x_list[i])**2+(d-y_list[i])**2)**0.5
                if(dist[i]>temp):
                    dist[i] = temp
    if(dist_min >= dist[i]):
        dist_min = dist[i]

# if(count==0):
#     return 0
# print(dist_min)

for i in range(n):
    if(dist_min == dist[i]):
        print(dist[i])
        print(x_list[i],y_list[i])
