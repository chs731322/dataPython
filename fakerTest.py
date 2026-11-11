from faker import Faker
from openpyxl import Workbook, load_workbook
import random
from pathlib import Path

# 1. 기본 설정
FILE_NAME = "faker_students_result.xlsx"
STUDENT_SHEET = "학생 성적"
STATISTIC_SHEET = "통계결과"
EXCELLENT_SHEET = "우수학생"

# Faker 객체 생성
fake = Faker("ko_KR")

# 2. 평균 점수를 이용하여 등급 계산
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
# 3. 평균 점수를 이용하여 상태 계산
def calculate_status(average):
    if average >= 90:
        return "우수"
    elif average < 70:
        return "주의"
    else:
        return "일반"
    
# 4. Faker를 이용하여 학생 성적 데이터를 생성하고 Excel 파일로 저장
def create_student_data():
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = STUDENT_SHEET

    # 헤더 작성
    sheet.append([
        "학번", "이름", "학과", "국어", "영어", "수학", "총점", "평균", "등급", "상태"
    ])

    # 학생 데이터 생성
    for i in range(1, 15):
        student_id = 2026000 + i
        name = fake.name()
        department = random.choice([
            "멀티미디어학과", "컴퓨터공학과", "전자공학과"
        ])
        
        korean = random.randint(50, 100)
        english = random.randint(50, 100)
        math = random.randint(50, 100)
        total = korean + english + math
        average = total / 3
        grade = calculate_grade(average)
        status = calculate_status(average)
        
        sheet.append([
            student_id, name, department, korean, english, math, total, round(average, 2), grade, status
        ])
    
    workbook.save(FILE_NAME)
    workbook.close()
    print(f"{FILE_NAME} 파일이 생성되었습니다.")

# 5. 전체 학생 출력
def show_all_students(sheet):
    print("\n====================== 전체 학생 목록 ======================")
    # 2행부터 마지막 행까지 반복
    for row in range(2, sheet.max_row + 1):
        student_id = sheet.cell(row=row, column=1).value
        name = sheet.cell(row=row, column=2).value
        department = sheet.cell(row=row, column=3).value
        korean = sheet.cell(row=row, column=4).value
        english = sheet.cell(row=row, column=5).value
        math = sheet.cell(row=row, column=6).value
        total = sheet.cell(row=row, column=7).value
        average = sheet.cell(row=row, column=8).value
        grade = sheet.cell(row=row, column=9).value
        status = sheet.cell(row=row, column=10).value
        
        print(f"{student_id} / {name} / {department} / {korean}, {english}, {math} | 총점: {total}, 평균: {average:.2f}, 등급: {grade} | {status}")

# 6. 학생 이름 검색
def search_student(sheet):
    # 검색할 학생 이름 입력
    target_name = input("\n검색할 학생 이름을 입력하세요: ").strip()
    # 검색 여부 확인
    found = False
    
    for row in range(2, sheet.max_row + 1):
        name = sheet.cell(row=row, column=2).value
        if name == target_name:
            student_id = sheet.cell(row=row, column=1).value
            department = sheet.cell(row=row, column=3).value
            korean = sheet.cell(row=row, column=4).value
            english = sheet.cell(row=row, column=5).value
            math = sheet.cell(row=row, column=6).value
            total = sheet.cell(row=row, column=7).value
            average = sheet.cell(row=row, column=8).value
            grade = sheet.cell(row=row, column=9).value
            status = sheet.cell(row=row, column=10).value
            
            print("\n=== 학생 검색 결과 ===")
            print("학번:", student_id)
            print("이름:", name)
            print("학과:", department)
            print("국어:", korean)
            print("영어:", english)
            print("수학:", math)
            print("총점:", total)
            print(f"평균: {average:.2f}")
            print("등급:", grade)
            print("상태:", status)
            found = True
            # 학생을 찾았으므로 반복문 종료
            break

    if not found:
        print("\n검색 결과가 없습니다.")
        
# 7. 평균이 가장 높은 학생 찾기
def show_best_student(sheet):
    max_average = 0
    max_name = ""
    max_student_id = ""
    
    for row in range(2, sheet.max_row + 1):
        student_id = sheet.cell(row=row, column=1).value
        name = sheet.cell(row=row, column=2).value
        average = sheet.cell(row=row, column=8).value
        # 현재 평균이 기존 최고 평균보다 높으면
        if average > max_average:
            max_average = average
            max_name = name
            max_student_id = student_id
            
    print("\n=== 최고 평균 학생 ===")
    print("학번: ", max_student_id)
    print("이름: ", max_name)
    print(f"평균: {max_average:.2f}")
    
# 8. 과목별 평균 계산
def calculate_subject_statistics(sheet):
    korean_total = 0
    english_total = 0
    math_total = 0
    count = 0
    
    for row in range(2, sheet.max_row + 1):
        korean = sheet.cell(row=row, column=4).value
        english = sheet.cell(row=row, column=5).value
        math = sheet.cell(row=row, column=6).value
        korean_total += korean
        english_total += english
        math_total += math
        count += 1
        
    # 학생 데이터가 없는 경우
    if count == 0:
        return 0, 0, 0
    # 국어 평균
    korean_average = (korean_total / count)
    # 영어 평균
    english_average = (english_total / count)
    # 수학 평균
    math_average = (math_total / count)
    # 세 개의 평균값 반환
    return (korean_average, english_average, math_average)

# 9. 과목별 평균 화면 출력
def show_subject_statistics(sheet):
    # 함수가 반환한 세 개의 값을 각각 저장
    korean_average, english_average, math_average = calculate_subject_statistics(sheet)
    print("\n=== 과목별 평균 ===")
    print(f"국어 평균: {korean_average:.2f}")
    print(f"영어 평균: {english_average:.2f}")
    print(f"수학 평균: {math_average:.2f}")
    
# 10. 통계결과 시트 생성
def create_statistics_sheet(workbook, student_sheet):
    # 기존 통계결과 시트가 있다면 삭제
    if STATISTIC_SHEET in workbook.sheetnames:
        del workbook[STATISTIC_SHEET]
    # 새로운 통계결과 시트 생성
    statistics_sheet = workbook.create_sheet(STATISTIC_SHEET)
    # 첫 행에 제목 추가
    statistics_sheet.appent(["구분", "결과"])
    # 과목별 평균 계산
    korean_average, english_average, math_average = calculate_subject_statistics(student_sheet)
    # 최고 평균
    max_average = 0
    # 최고 평균 학생 이름
    max_name = ""
    for row in range(2, student_sheet.max_row + 1):
        name = student_sheet.cell(row=row, column=2).value
        average = student_sheet.cell(row=row, column=8).value
        if average > max_average:
            max_average = average
            max_name = name
    # 통계결과 작성
    statistics_sheet.append(["국어 평균", round(korean_average, 2)])
    statistics_sheet.append(["영어 평균", round(english_average, 2)])
    statistics_sheet.append(["수학 평균", round(math_average, 2)])
    statistics_sheet.append(["최고 평균 학생", max_name])
    statistics_sheet.append(["최고 평균 점수", round(max_average, 2)])

# 11. 우수학생 시트 생성
def create_excellent_sheet(workbook, student_sheet):
    # 기존 우수학생 시트가 있다면 삭제
    if EXCELLENT_SHEET in workbook.sheetnames:
        del workbook[EXCELLENT_SHEET]
    # 새로운 우수학생 시트 생성
    excellent_sheet = workbook.create_sheet(EXCELLENT_SHEET)
    # 첫 행 제목 작성
    excellent_sheet.append(["학번", "이름", "학과", "국어", "영어",
                            "수학", "총점", "평균", "등급"])
    for row in range(2, student_sheet.max_row + 1):
        average = student_sheet.cell(row=row, column=8).value
        # 평균 90점 이상인 학생만 저장
        if average >= 90:
            student_id = student_sheet.cell(row=row, column=1).value
            name = student_sheet.cell(row=row, column=2).value
            department = student_sheet.cell(row=row, column=3).value
            korean = student_sheet.cell(row=row, column=4).value
            english = student_sheet.cell(row=row, column=5).value
            math = student_sheet.cell(row=row, column=6).value
            total = student_sheet.cell(row=row, column=7).value
            grade = student_sheet.cell(row=row, column=9).value
            excellent_sheet.append([student_id, name, department,
                korean, english, math, total, average, grade])
    
# 12. 우수 학생 화면 출력
def show_excellent_students(sheet):
    print("\n==============================")
    print("          우수 학생")
    print("==============================")
    count = 0    # 우수 학생 수
    for row in range(2, sheet.max_row + 1):
        average = sheet.cell(row=row, column=8).value
        # 평균 90점 이상
        if average >= 90:
            name = sheet.cell(row=row, column=2).value
            department = sheet.cell(row=row, column=3).value
            grade = sheet.cell(row=row, column=9).value
            print(f"{name} / " f"{department} / " f"평균 {average:.2f} / "
                  f"{grade}등급")

            count += 1
    print(f"\n우수 학생 수: {count}명")

# 13. 주의 학생 화면 출력
def show_warning_students(sheet):
    print("\n==============================")
    print("          주의 학생")
    print("==============================")
    count = 0    # 주의 학생 수

    for row in range(2, sheet.max_row + 1):
        average = sheet.cell(row=row, column=8).value
        # 평균 70점 미만
        if average < 70:
            name = sheet.cell(row=row, column=2).value
            department = sheet.cell(row=row, column=3).value
            grade = sheet.cell(row=row, column=9).value
            print(f"{name} / " f"{department} / " f"평균 {average:.2f} / "
                  f"{grade}등급")
            
            count += 1
            
        print(f"\n주의 학생 수 : {count}명")
        
# 14. main 함수
def main():
    # Excel 파일 존재 여부 확인
    if not Path(FILE_NAME).exists():
        print("Excel 파일이 없습니다.")
        print("새로운 학생 데이터를 생성합니다.")
        # Faker를 이용하여 새로운 Excel 데이터 생성
        create_student_data()
    # Excel 파일 불러오기
    workbook = load_workbook(FILE_NAME)
    # 학생성적 시트 확인
    if STUDENT_SHEET not in workbook.sheetnames:
        print("학생성적 시트가 없습니다.")
        workbook.close()
        return

    student_sheet = workbook[STUDENT_SHEET] # 학생성적 시트 선택
    create_statistics_sheet(workbook, student_sheet) # 통계결과 시트 생성
    create_excellent_sheet(workbook, student_sheet) # 우수학생 시트 생성

    try: # Excel 파일 저장
        workbook.save(FILE_NAME)
    except PermissionError:
        print("Excel 파일이 열려 있어 저장할 수 없습니다.")
        print("Excel 파일을 닫은 후 다시 실행하세요.")
        workbook.close()
        return

    # 메뉴 반복
    while True:
        print("\n==================================")
        print("        학생 성적 관리 프로그램")
        print("==================================")
        print("1. 전체 학생 보기")
        print("2. 학생 이름 검색")
        print("3. 최고 평균 학생 보기")
        print("4. 과목별 평균 보기")
        print("5. 우수 학생 보기")
        print("6. 주의 학생 보기")
        print("0. 종료")
        # 메뉴 선택
        menu = input("메뉴 선택: ").strip()
        if menu == "1": # 1번
            show_all_students(student_sheet)
        elif menu == "2": # 2번
            search_student(student_sheet)
        elif menu == "3": # 3번
            show_best_student(student_sheet)
        elif menu == "4": # 4번
            show_subject_statistics(student_sheet)
        elif menu == "5": # 5번
            show_excellent_students(student_sheet)
        elif menu == "6": # 6번
            show_warning_students(student_sheet)
        elif menu == "0": # 0번
            print("프로그램을 종료합니다.")
            break
        else: # 잘못된 메뉴
            print("0~6 중에서 선택하세요.")
    # Excel 파일 닫기
    workbook.close()
# 15. 프로그램 실행
main()
'''
for i in range(1, 6):  # Generate 5 fake profiles
    print("=== " + str(i) + "번째 데이터 ===")
    print("이름: ", fake.name())
    print("주소: ", fake.address())
    print("이메일: ", fake.email())
    print("전화번호: ", fake.phone_number())
    print()
'''

'''
students = []
for _ in range(5):  
    student = {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }
    students.append(student)
    print(student)
    
print("\n" + str(students))
'''
'''
students = []

for i in range(10):
    student = {
        "name": fake.name(),
        "department": random.choice([
            "컴퓨터공학과", 
            "전자공학과",
            "멀티미디어학과"
        ]),
        "korean": random.randint(50, 100),
        "english": random.randint(50, 100),
        "math": random.randint(50, 100)
    }
    students.append(student)
    
print("\n=== 학생 성적 리스트 ===")
for student in students:
    print(f"[{student['department']}] {student['name']} | 국어: {student['korean']}, 영어: {student['english']}, 수학: {student['math']} - 총점: {student['korean'] + student['english'] + student['math']}, 평균: {(student['korean'] + student['english'] + student['math']) / 3:.2f}")
    print()

print(students)

import json
print(f"]\n{json.dumps(students, ensure_ascii=False, indent=4)}\n")
'''