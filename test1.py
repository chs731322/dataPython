num1= float(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
num2= float(input("첫 번째 숫자를 입력하세요: "))

if operator == "+":
    result = num1 + num2
    print(f"결과 : {num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"결과 : {num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"결과 : {num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0: 
        result = num1 / num2
        print(f"결과 : {num1} / {num2} = {result:.2f}")
    else : 
        print("0으로 나눌 수 없습니다.")
else :
    print("잘못된 연산자입니다. (+, -, *, /)중 하나 입력")