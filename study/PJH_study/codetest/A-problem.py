#A-number
# x = int(input())
# y = x**2

# k = len(str(x))

# if str(x)==str(y)[-k:]:
#     print("1")
# else:
#     print("0")



#A-number for문
x = int(input())
temp = []
for i in range(x):
    y = i**2
    k = len(str(i))
    if str(i)==str(y)[-k:]:
        temp.append(i)
print(temp[-1])