# 월별 카메라 매출 데이터
months = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
sales_2025 = [120, 125, 130, 128, 140, 145, 150, 155, 160, 168, 175, 180]

# 1. 2025년 월별 매출 조회
def show_data():
    print(f"\n[2025년 월별 매출]")
    for i in range(len(months)):
        print(f"{months[i]} : {sales_2025[i]}")

# 2. 평균 매출 계산 함수
def show_average():
    average = sum(sales_2025) / len(sales_2025)
    print(f"2025년 평균 매출: {average:.2f}")

# 3. 최고 / 최저 매출 수치 찾기
def show_min_max():
    print(f"최고 매출: {max(sales_2025)}")
    print(f"최저 매출: {min(sales_2025)}")

# 4. 월별 변화량 계산 함수
def show_changes():
    print("\n[월별 변화량]")
    for i in range(1, len(sales_2025)):
        change = sales_2025[i] - sales_2025[i-1]
        print(
            f"{months[i-1]} -> {months[i]} : "
            f"{change:+}"
        )

# 5. 월별 증가 / 감소 확인
def show_trend():
    print("\n[월별 증가/감소]")
    for i in range(1, len(sales_2025)):
        change = sales_2025[i] - sales_2025[i-1]
        if change > 0:
            print(f"{months[i]} : 증가")
        elif change < 0:
            print(f"{months[i]} : 감소")
        else:
            print(f"{months[i]} : 변화 없음")

# 6. 평균 변화량 계산 함수 (모든 데이터에 사용 가능)
def calculate_average_change(data):
    changes = []
    for i in range(1, len(data)):
        change = data[i] - data[i-1]
        changes.append(change)

    average_change = sum(changes) / len(changes)
    return average_change

# 7. 2026년 매출 예측 (한 번의 예측)
def predict_2026():
    average_change = calculate_average_change(sales_2025)
    prediction = sales_2025[-1] + average_change
    print(f"\n[2026년 예산 분석]")
    print(f"평균 변화량: {average_change:.2f}")
    print(f"2025년 12월 매출: {sales_2025[-1]}")
    print(f"2026년 1월 예상 매출: {prediction:.2f}")

# 8. 다음 년도 매월 매출 예측
def predict_next_year(data):
    average_change = calculate_average_change(data)
    predicted = []
    current = data[-1]

    for i in range(12):
        current = current + average_change
        predicted.append(current)

    return predicted

# 2026년 매월 매출 예측
def month_predict_2026():
    sales_2026 = predict_next_year(sales_2025)

    print("\n[2026년 예상 매출]")

    for i in range(12):
        print(f"2026년 {months[i]} : {sales_2026[i]:.2f}")

    return sales_2026

# 2027년 매출 예측
def month_predict_2027():
    sales_2026 = predict_next_year(sales_2025)
    sales_2027 = predict_next_year(sales_2026)

    print("\n[2027년 예상 매출]")

    for i in range(12):
        print(f"2027년 {months[i]} : {sales_2027[i]:.2f}")


# 메뉴 프로그램
while True:
    print("=" * 30)
    print(" 2025년 매출 분석 프로그램")
    print("=" * 30)
    print("1. 월별 매출 조회")
    print("2. 평균 매출")
    print("3. 최고 / 최저 매출")
    print("4. 월별 변화량")
    print("5. 월별 증가/감소")
    print("6. 평균 변화량")
    print("7. 2026년 매출 예측")
    print("8. 2026년 매월 매출 예측")
    print("9. 2027년 매월 매출 예측")
    print("0. 종료")

    try:
        menu = int(input("메뉴 선택 : "))
        if menu == 1:
            show_data()
        elif menu == 2:
            show_average()
        elif menu == 3:
            show_min_max()
        elif menu == 4:
            show_changes()
        elif menu == 5:
            show_trend()
        elif menu == 6:
            average_change = calculate_average_change(sales_2025)
            print(
                f"\n평균 변화량: "
                f"{average_change:.2f}"
            )
        elif menu == 7:
            predict_2026()
        elif menu == 8:
            month_predict_2026()
        elif menu == 9:
            month_predict_2027()
        elif menu == 0:
            print("프로그램 종료")
            break
        else:
            print("0~9 중에 선택하세요.")

    except ValueError:
        print("숫자만 입력하세요.")