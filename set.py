# set (집합)
# 중복이 안됨, 순서 없음
my_set ={1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java & python)
print(java & python)
print(java.intersection(python))

# 합집합 (java or python)
print(java | python)
print(java.union(python))

# 차집합(java - python)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람 추가
python.add("김태호")
print(python)

#java를 잊어버림
java.remove("양세형")
print(java)