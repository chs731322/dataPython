from datetime import datetime

energy = [[2025, 1, 320], [2025, 2, 300], [2025, 3, 310], [2025, 4, 340],
         [2025, 5, 360], [2025, 6, 390], [2025, 7, 430], [2025, 8, 450],
         [2025, 9, 410], [2025, 10, 380], [2025, 11, 350], [2025, 12, 330],
         [2026, 1, 335], [2026, 2, 315], [2026, 3, 325], [2026, 4, 355],
         [2026, 5, 375], [2026, 6, 405], [2026, 7, 445], [2026, 8, 465],
         [2026, 9, 425], [2026, 10, 395], [2026, 11, 365], [2026, 12, 345]]

# 특정 연도의 매출 가져오기
def get_year_data(year):
    data = []
    for item in energy:
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

# 다음 연도 예상 사용량 생성
def predict_year(current_year):
    current_energy = get_year_data(current_year)
    average_change = calculate_average_change(current_energy)
    current = current_energy[-1]
    next_year = current_year + 1

    for month in range(1, 13):
        current = current + average_change
        # 예상값 반올림
        prediction = round(current)
        # energy에 새로운 데이터 추가
        energy.append(
            [next_year, month, prediction]
        )
        current = prediction

# 2026년 예상 데이터 생성
predict_year(2025)

# 2027년 예상 데이터 생성
predict_year(2026)

# 연도와 월을 입력받아 매출 검색
def search_energy(year, month):
    # 현재 날짜 가져오기
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # energy에서 데이터 검색
    for item in energy:
        if item[0] == year and item[1] == month:
            energy_value = item[2]

            # 데이터 타입 판정
            if year < current_year or (year == current_year and month <= current_month):
                data_type = "전력 사용량"
            else:
                data_type = "예상 전력 사용량"

            print(f"{year}년 {month}월 {data_type}은 {energy_value}입니다.")
            return


# 사용자 입력
while True:
    try:
        year = int(input("연도를 입력하세요: "))
        month = int(input("월을 입력하세요: "))

        if 1 <= month <= 12:
            search_energy(year, month)
        else:
            print("월은 1~12 사이로 입력하세요.")

        answer = input("종료할까요? : (y/n) ")

        if answer.lower() == 'y': 
            break
        else:
            continue

    except ValueError:
        print("숫자만 입력하세요.")