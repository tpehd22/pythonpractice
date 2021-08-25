sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬 쏘 이지"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쏘 이지
"""
print(sentence3)

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0번째 인덱스부터 2번째 인덱스 직전까지(0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지 
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리(뒤에서 부터) : " + jumin[-7:])
# 뒤에서부터 계산할 땐 맨 뒤가 -1번째가 된다. 왼쪽으로 갈수록 -2

