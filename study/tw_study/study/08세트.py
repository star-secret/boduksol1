#집합은 중복이 안되고, 순서가 없다
sett = {1,2,3,3,3}      # 딕셔너리와 같이 중괄호로 묶지만 딕셔너리는 키:값 구조고 세트는 ,만 있는 구조이다
print(sett)     # 3이 여러번 들어가 있지만 한 번만 출력되는 것을 볼 수 있다

python = set(["김철수", "가나다", "아저씨"])
java = {"스탠드", "노트북", "가나다"}

#교집합
print(python & java)
print(python.intersection(java))

#합집합
print(python | java)
print(python.union(java))

#차집합
print(python - java)
print(python.difference(java))

#요소 추가
python.add("dsda")
print(python)

#요소 삭제
python.remove("김철수")
print(python)