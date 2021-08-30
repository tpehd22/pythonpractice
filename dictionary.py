# cabinet = {3: "유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))

# #print(cabinet[5]) # 값이 없는 경우는 오류를 발생하고 프로그램이 종료되지만
# print(cabinet.get(5)) # get을 이용하면 None을 출력시키고 프로그램을 계속 진행시킨다.
# print(cabinet.get(5, "사용 가능")) # 5의 값이 없을 때 사용가능의 값을 출력시킴-> 쓸 수 있다는 말
# print("hi")

# print(3 in cabinet) # key in 변수 True
# print(5 in cabinet) # False

cabinet = {"A-3": "유재석", "B-100":"김태호"}
print(cabinet.get("A-3"))
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 추력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 모두 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)