a = int(input())
k = 1
for i in range(1,a*2):
    if(i<=a):
        for j in range(a-i):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
            print(" ",end="")
        print()
    else:
        for j in range(k):
            print(" ",end="")
        for j in range(a-k):
            print("*",end="")
            print(" ",end="")
        k += 1
        print()