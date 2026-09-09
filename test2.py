print("=========================")
print("\t계산기")
print("=========================")

# 방법 1
a = int(input("첫 번째 숫자를 입력하세요 : "))

operator = input("연산자를 입력하세요 (+, -, *, /) : ")
if operator not in ["+", "-", "*", "/"]:
    print("잘못된 연산자입니다. 프로그램을 종료합니다.")
    exit()

b = int(input("두 번째 숫자를 입력하세요 : "))

if operator == "+":
    print(f"답 : {a} + {b} = {a+b}")
elif operator == "-":
    print(f"답 : {a} - {b} = {a-b}")
elif operator == "*":
    print(f"답 : {a} * {b} = {a*b}")
elif operator == "/":
    if b == 0:
        print("0으로 나눌 수 없습니다. 프로그램을 종료합니다.")
        exit()
    else:
        print(f"답 : {a} / {b} = {a/b}")

# 방법 2
"""
print("=========================")
s = input("계산식을 입력하세요 : ")
print(f"답 : {eval(s)}")
"""