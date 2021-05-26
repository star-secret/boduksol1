'''
if문은 큰 틀에서 다음과 같은 규칙을 갖는다
    if 조건문:      C언어와 다르게 꼭 콜론을 붙여주어야 한다
        실행 명령문
'''
weather = input()
if weather == "비":
    print("비라니")
elif weather == "미세먼지":     #C언어에서 else if문과 같은 역할을 한다
    print("마스크챙기기")
else:
    pass                       #파이썬에서 if 다음 줄에 아무 코드도 넣지 못하면 에러가 발생하므로 pass를 넣어주어야한다

if True:
    print("True")

if False:
    print("False")             #조건문에서 False는 실행되지 않는다

if None:
    print("None")              # None은 False로 취급되므로 조건문이 실행된다. 변수의 값이나 함수의 결과가 None인 경우가 있으므로 알아두어야 함.

if 0:
    print("0")                 # 조건문에서 0은 False와 같고, 0이 아닌수는 True와 같다
if (not 0):
    print("not 0")

if 'Hello':                    # 조건문에서 빈 문자열이아니면 True와 같고 빈 문자열을 False와 같다
    print("Hello")

if '':
    print("''")