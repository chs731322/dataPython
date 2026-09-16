import random

print("숫자 맞추기 게임")

answer = random.randint(1, 100)

while True :
    a = int(input("숫자를 입력하세요 : "))
    if a == answer:
        print("정답입니다")
        break
    elif a > answer:
        print("down")
    elif a < answer:
        print("up")