def solution(N, stages):
    ans=[]
    length = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)
        
        if count ==0:
            fail = 0
        else:
            fail = count/length
        ans.append((i,fail))
        
        length -=count
        
ans = sorrted(ans, key=lambda t:t[1], reverse =True)
ans = 