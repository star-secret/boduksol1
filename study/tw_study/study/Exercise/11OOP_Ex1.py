
'''
    1. 학생 클래스 만들기 (Student)
        속성(변수) : 이름(name), 나이(age), 전화번호(phone), 과목(sub)
        기능(함수)
            1. 생성자 __init__
                > 매개변수로 이름,나이,전화번호,과목을 전달 받고, 각 속성 생성 및 대입
            2. 정보 출력 (print_info)
                > 객체에 만들어져 있는 이름,나이,전화번호 를 출력
                    이름 : 홍길동
                    나이 : 20세
                    전화번호 : 010-1234-5678
            3. 공부하기 (study)
                > 객체에 만들어져 있는 이름,과목 출력
                    홍길동 님이 파이썬 공부를 시작합니다.

        - 학생 3명 만들어서 '정보출력', '공부하기' 메서드를 호출해서 출력 결과 확인
            hong.print_info() <-- 이런거 하자는 얘기
'''
class Student :
    def __init__(self, name, age, phone, sub) :
        self.name = name
        self.age = age
        self.phone = phone
        self.sub = sub

    def print_info(self) :
        print("이름 :", self.name)
        print("나이 :", self.age)
        print("전화번호 :", self.phone)

    def study(self) :
        print("{} 님이 {} 공부를 시작합니다.".format(self.name, self.sub))

stu1 = Student("홍길동", 20, "010-1234-5678", "파이썬")
stu1.print_info()
stu1.study()

'''
    2. 계산기 클래스 (Calc)
        속성 : 각 사칙연산의 계산(기능)이 수행된 횟수를 누적
                add_count, min_count, mul_count, div_count

        기능
            1. 생성자 __init__
                > 속성 만들기  (생성자에서 속성을 만든다 = 모든 인스턴스가 공통적으로 속성을 가진다.)
            2. 각 사칙연산을 계산하는 메서드 4개
                > 계산하고 싶은 2개의 값을 전달 받고, 계산 결과를 출력 (반환 X)
                    1 + 2 = 3
            3. 정보 출력(print_info)
                > 각 계산의 수행 횟수 출력

        ex) 덧셈 함수 3번 호출, 나눗셈 함수 2번 호출 후 print_info를 호출하면,
            1 + 2 = 3
            2 + 5 = 7
            10 / 2 = 5.0
            10 / 2 = 5.0
            3 + 9 = 12
            덧셈 : 3
            뺄셈 : 0
            곱셈 : 0
            나눗셈 : 2
'''
class Calc:

    def __init__(self) :
        self.addCount = 0
        self.minCount = 0
        self.mulCount = 0
        self.divCount = 0

    def add(self,num1,num2):
        self.addCount += 1
        print("{} + {} = {}".format(num1, num2, num1 + num2))

    def min(self,num1,num2):
        self.minCount += 1
        print("{} - {} = {}".format(num1, num2, num1 - num2))

    def mul(self,num1,num2):
        self.mulCount += 1
        print("{} * {} = {}".format(num1, num2, num1 * num2))

    def div(self,num1,num2):
        self.divCount += 1
        print("{} / {} = {}".format(num1, num2, num1 / num2))

    def print_info(self) :
        print("덧셈 :", self.addCount)
        print("뺄셈 :", self.minCount)
        print("곱셈 :", self.mulCount)
        print("나눗셈 :", self.divCount)
    
my_calc = Calc()
my_calc.add(1,3)
my_calc.add(10,5)
my_calc.min(10,5)

my_calc.print_info()





'''
        3. 책을 의미하는 Book 클래스
           전자책을 의미하는 EBook 클래스
        
            Book
                변수 : 제목, 정가
            EBook
                변수 : 보안키

    20000원짜리 "파이썬 최고" 책 1권
    15000원짜리 "파이썬 최고 - ebook" 전자책 1권 (보안키 1234)

            각각 인스턴스를 생성하여 정보 출력하기
            print_info()를 오버라이딩하고, super()를 활용하기
'''

class Book :
    def __init__(self, name, price) :
        self.name = name
        self.price = price

    def print_info(self) :
        print("이름 :", self.name)
        print("가격 :", self.price)

class EBook(Book) :
    def __init__(self, name, price, key) :
        super().__init__(name, price)
        self.key = key

    def print_info(self) :
        super().print_info()
        print("보안키 :", self.key)

book = Book("파이썬 최고", 20000)
book.print_info()

ebook = EBook("파이썬 최고 - ebook", 15000, 1234)
ebook.print_info()


'''

        4. 사각형을 의미하는 Rectangle 클래스
           정사각형을 의미하는 Squre 클래스

           (1) 사각형 클래스를 정의
           (2) 사각형을 상속받는 정사각형 클래스 정의
           (3) 아래와 같은 결과가 나오도록 클래스 만들기
'''
class Rectangle :
    def __init__(self, row, col) :
        self.area = row * col

    def print_area(self) :
        print( "면적 :", self.area )

class Square(Rectangle) :
    def __init__(self, row) :
        super().__init__(row, row)

rect = Rectangle(3, 4) # 가로, 세로 입력
rect.print_area() # 면적 : 12

sqr = Square(7)
sqr.print_area() # 면적 : 49

