from openpyxl import load_workbook

# 기존 Excel 파일 열기
workbook = load_workbook("students.xlsx")

# "학생 점수" 시트 선택
worksheet = workbook["학생 점수"]

# 새로운 학생 정보 추가
while True:
    name = input("추가할 학생 이름을 입력하세요: ")
    
    try:
        score = int(input("추가할 학생 점수를 입력하세요: "))
        
        worksheet.append([name, score])
            
    except ValueError:
        print("점수는 숫자로 입력해야 합니다.")

    end = input("계속 추가하시겠습니까? (y/n): ")
    if end.lower() != 'y':
        workbook.save("students.xlsx")
        print("학생 정보 추가를 종료합니다.")
        print("학생 정보가 추가되었습니다.")
        break 