python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n")) # 이 함수는 찾을 값이 없을 땐 -1 반환
#python.index()함수에선 찾을 값이 없으면 오류가 남

print(python.count("n")) #찾을 문자열의 등장횟수 