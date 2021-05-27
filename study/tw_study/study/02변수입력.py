
x = input()
print(x)
# x가 그대로 출력된다

x = input('입력 : ')
# input안에 ''로 문구를 적으면 문구가 먼저 출력되고 그 다음에 입력을 받는다

a,b = input().split()   #입력받은 값을 공백을 기준으로 분리해서 변수 a와 b에 넣는다
print(a + b)            #input()으로 입력을 받으면 자동으로 문자열로 된다는 것을 알 수 있다

a,b = input('.을 기준으로 분리').split('.')     #split()안에 문자를 넣으면 그 문자를 기준으로 입력받은 값을 분리할 수 있다.
print(str(a),str(b))

#정수 변환!!        input으로 입력받으면 문자열취급하기 때문에 정수로 사용하고 싶을 때는 이렇게 해야 함
a,b = map(int, input('정수로 변환 : ').split())

print(a+b)