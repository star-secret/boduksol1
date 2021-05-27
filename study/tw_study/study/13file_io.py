
# 파이썬 언어로 컴퓨터에 존재하는 실제 파일을 다루는 방법
'''
    [파일 입출력] - file input/output
        - 실제 파일 생성/쓰기/삭제/읽기 등의 행위

        - 파일의 이해
            디렉토리(Directory)
                > 폴더 또는 디렉토리라고 부른다.
                > 폴더 안에는 파일과 또 다른 폴더를 포함할 수 있다.
                > 용량이 없다.
                > 폴더 안으로 들어가는 일 밖에 못함(실행 개념 없음)

            파일(File)
                > 컴퓨터에서 정보(data)를 저장하는 논리적인 단위
                > 파일은 실제 물리 disk(HDD, SSD)에 저장이 되고, 용량이 존재
                > 파일은 파일명과 확장자로 식별된다. (09_file_io.py)
                    >> 파일명.확장자 (파일전체이름에서 맨 오른쪽 . 기준으로 확장자)
                    >> test.txt.xlsx --> 엑셀 확장자
                    >> 확장자 : 이 파일이 어떤 형식의 파일인지 써놓는 것.
                > 실행, 쓰기, 읽기 등을 할 수 있다.

                > 기본적으로 모든 파일은 메모장으로 열 수 있다.
                    우리가 파이썬으로 소스파일 다루는 것도, 메모장으로 열어서 수정해도 된다.
                    단, 파이썬 편집기는 '코드 실행'기능이 있고, 메모장은 없다. 

                - Binary 파일
                    > 메모장으로 열었을때, 알아볼 수 없다.(내용이 깨져보임)
                    >> 확장자에 맞는 전용 프로그램으로 열어야 알아볼 수 있다.
                    > 확장자 : 엑셀(xlsx), 워드(docx), 한글(hwp) 등...

                - Text 파일
                    > 메모장으로 열었을 때, 우리가 알아볼 수 있는 파일
                    > 확장자 : txt, py, html, xml 등...

                - 우리는 코드로 파일을 다룰 때, 기본적으로 메모장으로 여는 것 처럼
                  파일을 읽는다. --> Binary파일의 내용은 읽어도 깨진다.

    [파일 다루는 기본 구조]
    파일객체 = open("파일이름", "파일 열기 모드")

        파일객체 : 변수와 비슷하다. (그냥 변수라고 생각)
        파일이름 : 컴퓨터에 존재하는 파일명(내가 열고 싶은 파일)
        파일 열기 모드 : 열었을 때, 어떤 행위를 할 것인지 미리 모드를 결정
            r : 읽기모드 (read)
                > 내용을 읽기만 할 때

            w : 쓰기모드(write)
                > 내용을 쓰기만 할 때

            a : 추가모드 (add)
                > 파일의 내용 끝에 내용을 추가할 때

            w+, r+, a+  이런 혼합 모드들고 있지만, 우리는 r과 w만 해볼 것
'''
print("[파일 입출력]")

# 파일의 절대 경로 : 드라이브문자를 포함하여, 전체 경로를 작성
# Windows 운영체제에서는 드라이브문자를 사용 -> 드라이브문자명: ex) C:, D:
#   D드라이브의 테스트 폴더의 test.txt --> D:\\테스트\\test.txt
# 상대 경로 : 실행된 프로그램 실행파일 위치가 기준(현재 위치)

# 파일 읽기
'''
file = open("C:\\test.txt", "r") # 절대 경로를 사용한다.
# read(): 파일의 전체 내용을 '문자열'로 반환
text = file.read()
print(text)
# 사용을 다 한 파일은 열었기(open) 때문에 반드시 닫아줘야한다.(close)
# 닫지 않으면.. 프로그램이 계속 사용 중이기 때문에 다른곳에서 파일을 다룰 수 없다. 
file.close()
print()
'''
# with 를 이용하여 close() 생략하기

with open("C:\\test.txt", "r") as file : # open한 파일을 file 변수로 다루겠다.
    text = file.read()
    print(text)

# close()를 생략해도 with 문법 안에서 자동으로 close를 해준다. (open을 사용한 경우)

# 파일 내용을 한 줄 씩 읽기
# readlines() : 한 줄 씩 문자열로 나눠서 리스트 반환 (개행의 \n포함)

with open("C:\\test.txt","r") as file:
    text = file.readlines()
    print(text)

# 파일 내용을 한 줄 씩 읽기
# readline() : 한 줄을 문자열로 읽기 (\n있으면 포함)
with open("C:\\test.txt", "r") as file:
    text = file.readline()
    print(text)  # print의 end='\n'에 의해 개행이 2번된다.

print()

with open("C:\\test.txt", "r") as file:
    while True: # 무한반복
        text = file.readline()
        
        if not text:  # 문자열은 비어있으면 False
            break  # text가 비면 False -> not False -> True (빈 문자열이면 break)
        
        print(text, end='')

# 다음 줄을 읽어라! 라는 명령을 따로 하지 않았는데 자동으로 다음 줄이 읽어졌다.
# 프로그래밍언어에서 file을 다룰 때 공통적인 사항
# > 한 번 읽거나, 쓰고 나면 자동으로 그 다음위치로 이동
# > 처음 파일을 열면 처음 위치 -> 한 줄 읽었다. -> 자동으로 다음 줄로 이동 
print("\n")
# 통계 산출(파일의 단어 개수, 라인수)
with open("C:\\test.txt", "r") as file:
    text = file.read() # 파일의 전체 내용 읽기
    word_list = text.split() # 공백을 기준으로 문자를 나눠서 '단어'라는 개념으로 쓰겠다. 
    line_list = text.split("\n") # 개행 기준으로 나눠서 리스트에 추가 

print(line_list)
print("라인 수 :", len(line_list))

print(word_list)
print("단어 수 :", len(word_list))
