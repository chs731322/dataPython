'''
energy는 [연도, 월, 전력사용량]을 저장한 2차원 리스트입니다.

python
energy = [[2026, 1, 310], [2026, 2, 295], [2026, 3, 320], [2026, 4, 350]]

사용자에게 연도와 월을 입력받아 다음 조건을 만족하는 코드를 작성하세요.

연도와 월에 해당하는 데이터가 있으면 2026년 3월 전력 사용량은 320입니다. 형태로 출력한다.
해당 데이터가 없으면 해당 데이터가 없습니다.를 출력한다.
숫자가 아닌 값을 입력하면 프로그램이 멈추지 않고 숫자만 입력하세요.를 출력한다.
'''
energy = [[2026, 1, 310], [2026, 2, 295], [2026, 3, 320], [2026, 4, 350]]

try:
    year = int(input("연도: "))
    month = int(input("월: "))

    found = False
    for item in energy:
        if item[0] == year and item[1] == month:
            print(f"{year}년 {month}월 전력 사용량은 {item[2]}입니다.")
            found = True
            break

    if not found:
        print("해당 데이터가 없습니다.")

except ValueError:
    print("숫자만 입력하세요.")

    '''
    1. try
    2. False
    3. sales
    4. and
    5. 2
    6. break
    7. not
    8. except
    '''

    '''
    1. openpyxl
    2. Workbook - 새 엑셀 파일을 만듦 workbook = Workbook()
    3. active
    4. title
    5. append
    6. save
    7. load_workbook - 이미 있는 파일을 불러옴 workbook = load_workbook("products.xlsx")
    8. "상품"

    새로 만들기:  Workbook()  → append → save
    열어서 수정:  load_workbook("파일") → 시트 선택 → append → save
    '''

    '''
    1. def
    2. return
    3. class
    4. __init__
    5. self
    6. show
    7-1. 매개변수 : a, b
    7-2. 인수: 80, 90
    7-3. 클래스 이름 : Student
    7-4. 객체: s1
    7-5. 메서드: __init__, show
    '''