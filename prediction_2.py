from datetime import datetime

# 2025년 실제 매출 데이터 [연도, 월, 매출]
sales = [
    [2025, 1, 120], [2025, 2, 125], [2025, 3, 130],
    [2025, 4, 128], [2025, 5, 140], [2025, 6, 145],
    [2025, 7, 150], [2025, 8, 155], [2025, 9, 160],
    [2025, 10, 168], [2025, 11, 175], [2025, 12, 180]
]

# 특정 연도의 매출 가져오기
def get_year_sales(year):
    data = []
    for item in sales:
        if item[0] == year:
            data.append(item[2])
    return data

# 평균 변화량 계산
def calculate_average_change(data):
    changes = []
    for i in range(1, len(data)):
        change = data[i] - data[i - 1]
        changes.append(change)

    average_change = sum(changes) / len(changes)
    return average_change

# 다음 연도 예상 매출 생성
def predict_year(current_year):
    current_sales = get_year_sales(current_year)
    average_change = calculate_average_change(current_sales)
    current = current_sales[-1]
    next_year = current_year + 1

    for month in range(1, 13):
        current = current + average_change
        # 예상값 반올림
        prediction = round(current)
        # sales에 새로운 데이터 추가
        sales.append(
            [next_year, month, prediction]
        )
        current = prediction

# 2026년 예상 데이터 생성
predict_year(2025)

# 2027년 예상 데이터 생성
predict_year(2026)

# 연도와 월을 입력받아 매출 검색
def search_sales(year, month):
    # 현재 날짜 가져오기
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # sales에서 데이터 검색
    for item in sales:
        if item[0] == year and item[1] == month:
            sales_value = item[2]

            # 데이터 타입 판정
            if year < current_year or (year == current_year and month <= current_month):
                data_type = "매출"
            else:
                data_type = "예상 매출"

            print(f"{year}년 {month}월 {data_type}은 {sales_value}입니다.")
            return


# 사용자 입력
try:
    year = int(input("연도를 입력하세요: "))
    month = int(input("월을 입력하세요: "))

    if 1 <= month <= 12:
        search_sales(year, month)
    else:
        print("월은 1~12 사이로 입력하세요.")

except ValueError:
    print("숫자만 입력하세요.")