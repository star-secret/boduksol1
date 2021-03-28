def solution(dartResult):
    
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'*' : 2, '#' : -1}

    a = [0,0,0]
    flag = -1

    for idx, dart in enumerate(dartResult) :
        if dart.isdigit() :
            flag += 1
            if dart == '0' :
                continue
            elif dartResult[idx+1].isdigit() :    # 10일 때 처리
                a[flag] = int(dart)*10
                flag -= 1
            else :
                a[flag] = int(dart)

        elif dart in 'SDT':                        # SDT    
            a[flag] **= bonus[dart]

        else :
            if dart == "*" :                    # *인 경우
                a[flag-1] *= 2

            a[flag] *= option[dart]

    return sum(a)

#코드흐름
# 1S2D*3T

# idx, dart
# idx=0
# dart =1

# flag=0
# dartresult[1].isdigit()
# a[0] = 1

# idx=1
# dart = S
# a[0] **1

# idx=2
# dart = 2
# flag=1

# a[1] = 2

# idx=3
# dart = D
# a[1]**2
# flag=1

# idx=4
# a[0]*2
# a[1]*2

# idx=5
# flag=2
# a[2] = 3

# idx=6
# a[2]**3
# return sum(a)

