sentence1 = '작은 따옴표로 감싸도 된다'
sentence2 = "큰 따옴표로 감싸도 된다"
sentence3 = """큰 따옴표
3개를 이용해서
작성할 수도 있다"""
print(sentence1)
print(sentence2)
print(sentence3)

number = "12345-6789"
print(number[3])    #필요한 문자만 출력할 수 있다
print(number[0:2])  #0~2직전까지만 출력
print(number[:2])   # :으로 시작시 처음부터!
print(number[5:8])
print(number[3:])   # number[3]부터 끝까지!
print(number[-5:])  #뒤에서 5번째부터 끝까지

sentence = "Ajou University A grade"
print(sentence.upper()) #모든 문자 대문자
print(sentence.lower()) #모든 문자 소문자
print(sentence[0].isupper())    #0번째 문자가 대문자인지 확인
print(len(sentence))        #문자열의 길이
print(sentence.replace("Ajou", "Seoul"))    #문자열 바꿔치기    지금 이 순간에만 바꾸는 것이고 sentence는 그대로 "Ajou University A grade"
print(sentence.index("A"))          # 찾고자 하는 문자가 몇번째 위치에 있는지
print(sentence.index("A",sentence.index("A")+1))    #처음 나오는 A가 아닌 두번째 A의 위치를 찾음
print(sentence.index("A",3))            #   sentence[3]문자 이후 A가 어디에 있는지 찾음
print(sentence.find("u"))       #index와 같은 역할이지만 index함수는 찾지 못하면 프로그램이 종료되지만 find함수는 못 찾으면 -1을 출력하고 프로그램 계속
print(sentence.count("A"))      # "A"라는 문자가 몇 번 등장하는지 계산


print("{}".format(20))
print("{}띄어쓰기{}".format("아주", "국방"))
print("{0}띄어쓰기{1}".format("아주", "국방"))
print("{1}띄어쓰기{0}".format("아주", "국방"))  #중괄호 안에 숫자를 넣으면 원하는 순서대로 출력할 수 있다

print("{univ}띄어쓰기{maj}".format(univ ="아주", maj= "국방"))  #이렇게 키워드를 정할 수 있다

a = "아주"
b = "국방"
print(f"{a}대학교{b}디지털")        #이런 방식으로도 쓸 수 있다