# 튜플은 읽기 전용 리스트이다.

a = (25,42,41,53)

#튜플도 리스트처럼 여러 자료형을 섞어서 저장해도 된다.
person = ('james',40,182.5,True)

#튜플은 요소가 절대 변경되지 않고 유지되어야 할 때 사용한다.
#define

# 요소가 한개짜리인 튜플생성
(31,)

#튜플을 생성하는 여러가지 방법
a = tuple(range(10))
a = [1,2,3]
tuple(a)

tuple('hello')
('h','e','l','l','o')

y=(4,5,6)
d,e,f = y
print(d,e,f)
