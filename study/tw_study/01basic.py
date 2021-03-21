#파이썬에서는 들여쓰기 자체가 문법이므로, 같은 블록이라면 들여쓰기 칸 수가 같아야 한다.

print('Hello'); print('1234')
#파이썬은 세미콜론을 붙이지 않아도 되지만, 세미콜론을 붙여도 문법 에러는 없다

print()
#기본적으로 print()함수는 ()안의 내용을 화면에 출력하고 줄바꿈이 발생한다.
print(1, end='')            # ''안에 공백조차 없으므로 다음번문자는 옆에 붙어서 쳐짐
                            # end=''은 원래 print의 마자막엔 자동으로 \n이 붙는데 이것을 다르게 끝내게 해주는 방법이다.
print(12,23,34, sep='\n')  # ,로 구분된 문자 사이에 개행을 발생
print('1\n2\n3')            # 문자열 안에 \n을 이용하여 개행 발생


#변수 입력
x, y, z = 10, 3.3, '강아지'
print("x"+z+str(x)+z*5+3*str(y))    # 문자열이 들어가있을 때 +을 하려면 정수를 str자료형으로 바꾸어 주어야함. 문자열과 곱셈연산은 가능
print(z,"는","귀엽다")          # ,로 문자열을 이어줄 경우 자동으로 띄어쓰기가 들어간다.

#자료형과 연산자
print(3)
print(3+8)
print(4-3)
print(3*4)
print(10/3) #C언어에서는 /연산자의 반환값은 정수타입이지만 파이썬에서는 실수타입으로 반환된다
print(10//3); # 몫을 반환하는 연산자이다.
print(11.1//3)  #실수를 //연산자로 계산할 경우 소수점 이하는 버린다.
print(10%3)
print(3**4) # 파이썬에는 거듭제곱 연산자가 있다. 결과 값은3^4이 된다.
print(abs(-5))  #절대값을 의미한다
print(pow(4,2)) #  4^2를 의미
print(max(5,12))    # 둘 중 큰 값을 구하는 함수
print(min(5,12))    # 둘 중 작은 값을 구하는 함수
print(round(3.14))  # 반올림하는 함수

type(10)    #type()함수는 객체의 타입을 알아내는 함수이다
print(type(int(10/3)))     #int()로 계산식을 감싸주었기 때문에 float이 아닌 int타입이라고 나올 것
print(type(int('10')))      #str이 아닌 int라 나옴

print(type(float(3)))       # int가 아닌 float이라고 나옴
print(type(float('5.3')))   # str이 아닌 float이라고 나옴
print(type('dd'))

print('풍선')
print('ㅋ'*9)   #이렇게 문자열과 정수를 섞어 계산해서 출력할 수 있다


print(5>10)
print(5 > 4 > 3)    #True
print(5 >4 > 7)     #False
print(5<10)
print(3==3) 
print(True)
print(False)
print("1과 1.0이 같은지 비교 :"+str(1 is 1.0))
print(1 is not 1.0)
print(not True) #앞에 not을 붙일 수 있다.
print(not(5>10))    #True가 출력될 것이다
print(1!=3)         # True가 나올 것
print((3 > 0) and (3 < 5)); print((3 > 0) & (3 < 5))    #두 식 모두 같은 의미이고 둘 다 참일 경우에만 True가 출력
print((3 > 0) or (3 > 5)); print((3 > 0) | (3 > 5))     # 두 식 모두 같고, 둘 중 하나만 참이면 True 출력
