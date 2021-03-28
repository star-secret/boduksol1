def solution(n, arr1, arr2):
    #함수를 선언해서 입력을 받자
    answer =[]
    
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:]
        #이진수를 다루기
        answer.append(("0"*(n-len(bin_str))+bin_str).replace("1","#").replace("0"," "))
        #문자열 맞추기 위해 0을 앞에 삽입하고, replace함수
    return answer

print(solution(5, [9, 20, 28, 18, 11],	[30, 1, 21, 17, 28]))

