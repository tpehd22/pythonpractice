# print('풍선')
# print("나비")
# print("ㅋ"*9)

# 참/거짓
# print(5>10)
# print(5>10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not(5>10))

#애완동움을 소개해주세요

# print("우리집 강아지의 이름은 연탄이에요")
# print("연탄이는 4살이며, 산책을 아주 좋아해요")
# print("연탄이는 어른일까요? True")

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

''' 이건 여러문장 주석하기 
'''


print("우리집"+ animal +"의 이름은 " + name + "이에요")
hobby = "공놀이"
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", str(age), "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))