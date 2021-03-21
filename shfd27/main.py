num = int(input())

for k in range(1,num+1):
    print(" "*(num-k)+"* "*k)
for k in range(num-1,0,-1):
    print(" "*(num-k)+"* "*k)

print("자구 드랍하자")