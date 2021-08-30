# 튜플은 리스트와 달리 내용 변경이나 추가가 안되지만
# 속도가 더 빠름

menu = ("돈까스", "치즈까쓰")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # tuple은 추가가 안됨
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = ("김종국", 20, "코딩")
print(name, age, hobby)