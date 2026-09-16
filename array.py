import random

print("숫자 맞추기 게임")

answer = random.randint(1, 100)

while True :
    try:
        a = int(input("숫자를 입력하세요 : "))
    except ValueError:
        print("1~100 숫자만 입력")
        continue

    if a < 1 or a > 100:
        print("1~100사이의 숫자만 입력")
        continue

    n += 1

    if a == answer:
        print("정답입니다")
        print(f"{n}회 만에 성공")
        break
    elif a > answer:
        print("down")
    elif a < answer:
        print("up")
