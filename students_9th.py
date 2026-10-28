from pathlib import Path
from openpyxl import load_workbook

# 사용할 엑셀 파일과 시트 이름
FILE_NAME = "students_9th.xlsx"
STUDENT_SHEET_NAME = "학생정보"
SCORE_SHEET_NAME = "성적정보"
RESULT_SHEET_NAME = "성적결과"


# ------------------------------------------------
# 점수 또는 평균에 따라 등급을 계산하는 함수
# ------------------------------------------------
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ------------------------------------------------
# 학생정보 시트를 읽어 딕셔너리로 만드는 함수
# ------------------------------------------------
def read_student_info(student_sheet):
    students = {}

    # 1행은 제목이므로 2행부터 읽음
    for row in range(2, student_sheet.max_row + 1):
        student_id = student_sheet.cell(row=row, column=1).value
        name = student_sheet.cell(row=row, column=2).value
        department = student_sheet.cell(row=row, column=3).value

        # 학번이 없는 빈 행은 건너뜀
        if student_id is None:
            continue

        # 학번은 비교하기 쉽도록 문자열로 통일
        student_id = str(student_id).strip()

        # 학번을 기준으로 이름, 학과, 성적 목록을 저장
        students[student_id] = {
            "name": "" if name is None else str(name).strip(),
            "department": "" if department is None else str(department).strip(),
            "subjects": []
        }

    return students


# ------------------------------------------------
# 성적정보 시트를 읽어 학생정보에 과목 성적을 연결
# ------------------------------------------------
def connect_score_info(score_sheet, students):
    for row in range(2, score_sheet.max_row + 1):
        student_id = score_sheet.cell(row=row, column=1).value
        subject = score_sheet.cell(row=row, column=2).value
        score = score_sheet.cell(row=row, column=3).value

        # 필요한 값이 비어 있으면 건너뜀
        if student_id is None or subject is None or score is None:
            continue

        student_id = str(student_id).strip()
        subject = str(subject).strip()

        # 점수를 숫자로 변경
        try:
            score = float(score)
        except (ValueError, TypeError):
            print(f"성적정보 {row}행의 점수가 잘못되었습니다: {score}")
            continue

        # 학생정보에 없는 학번은 연결할 수 없음
        if student_id not in students:
            print(f"학생정보에 없는 학번입니다: {student_id}")
            continue

        # 점수에 맞는 과목 등급을 계산하여 D열에도 기록
        subject_grade = calculate_grade(score)
        score_sheet.cell(row=row, column=4).value = subject_grade

        # 해당 학생의 과목 목록에 과목, 점수, 등급 추가
        students[student_id]["subjects"].append({
            "subject": subject,
            "score": score,
            "grade": subject_grade
        })


# ------------------------------------------------
# 학생정보 + 성적정보를 이용해 성적결과 시트 작성
# ------------------------------------------------
def create_result_sheet(workbook, students):
    # 기존 성적결과 시트가 있으면 새로 작성하기 위해 삭제
    if RESULT_SHEET_NAME in workbook.sheetnames:
        del workbook[RESULT_SHEET_NAME]

    result_sheet = workbook.create_sheet(RESULT_SHEET_NAME)
    result_sheet.append(["학번", "이름", "학과", "국어", "영어", "수학", "총점", "평균", "최종등급"])

    # 학생 한 명씩 결과 작성
    for student_id, student in students.items():
        subject_scores = {}

        # 과목명을 키로, 점수를 값으로 저장
        for item in student["subjects"]:
            subject_scores[item["subject"]] = item["score"]

        scores = []
        for subject in ["국어", "영어", "수학"]:
            if subject in subject_scores:
                scores.append(subject_scores[subject])

        # 등록된 점수가 없는 학생 처리
        if len(scores) == 0:
            total = 0
            average = 0
            final_grade = "성적 없음"
        else:
            total = sum(scores)
            average = total / len(scores)
            final_grade = calculate_grade(average)

        result_sheet.append([
            student_id, student["name"], student["department"],
            subject_scores.get("국어", ""), subject_scores.get("영어", ""),
            subject_scores.get("수학", ""), total, round(average, 2),
            final_grade])

    return result_sheet


# ------------------------------------------------
# 학생 한 명의 정보를 화면에 출력하는 함수
# ------------------------------------------------
def print_student_info(student_id, student):
    print("\n==============================")
    print("          학생 조회 결과")
    print("==============================")
    print(f"학번: {student_id}")
    print(f"이름: {student['name']}")
    print(f"학과: {student['department']}")

    # 성적이 없는 경우
    if len(student["subjects"]) == 0:
        print("등록된 성적이 없습니다.")
        return

    print("\n[과목별 성적]")

    scores = []

    # 국어, 영어, 수학 순서로 출력
    for target_subject in ["국어", "영어", "수학"]:
        for item in student["subjects"]:
            if item["subject"] == target_subject:
                score = item["score"]
                grade = item["grade"]
                scores.append(score)
                print(f"{target_subject}: {score:g}점 / {grade}등급")
                break

    total = sum(scores)
    average = total / len(scores)
    final_grade = calculate_grade(average)

    print("\n[종합 결과]")
    print(f"과목 수: {len(scores)}개")
    print(f"총점: {total:g}점")
    print(f"평균: {average:.2f}점")
    print(f"최종등급: {final_grade}")


# ------------------------------------------------
# 학번 / 이름으로 학생 검색
# ------------------------------------------------
def search_by_id(students):
    student_id = input("조회할 학번: ").strip()
    if student_id in students:
        print_student_info(student_id, students[student_id])
    else:
        print("해당 학번의 학생이 없습니다.")


def search_by_name(students):
    name = input("조회할 학생 이름: ").strip()
    found = False
    for student_id, student in students.items():
        if student["name"] == name:
            print_student_info(student_id, student)
            found = True
    if not found:
        print("해당 이름의 학생이 없습니다.")


# ------------------------------------------------
# 전체 성적결과를 화면에 출력
# ------------------------------------------------
def print_all_results(result_sheet):
    print("\n==============================")
    print("        전체 성적 결과")
    print("==============================")
    for row in result_sheet.iter_rows(values_only=True):
        print("\t".join("" if v is None else str(v) for v in row))


# ------------------------------------------------
# 프로그램 시작
# ------------------------------------------------
def main():
    file_path = Path(__file__).parent / FILE_NAME

    if not file_path.exists():
        print(f"엑셀 파일을 찾을 수 없습니다: {file_path}")
        return

    workbook = load_workbook(file_path)
    student_sheet = workbook[STUDENT_SHEET_NAME]
    score_sheet = workbook[SCORE_SHEET_NAME]

    students = read_student_info(student_sheet)
    connect_score_info(score_sheet, students)
    result_sheet = create_result_sheet(workbook, students)

    # 엑셀에 등급/결과를 저장 (엑셀에서 파일이 열려 있으면 저장 실패)
    try:
        workbook.save(file_path)
    except PermissionError:
        print("엑셀 파일이 열려 있어 저장하지 못했습니다. 파일을 닫고 다시 실행하세요.")

    while True:
        print("\n==============================")
        print("        학생 성적 조회")
        print("==============================")
        print("1. 학번으로 검색")
        print("2. 이름으로 검색")
        print("3. 전체 성적결과 보기")
        print("0. 종료")
        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            search_by_id(students)
        elif choice == "2":
            search_by_name(students)
        elif choice == "3":
            print_all_results(result_sheet)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")


if __name__ == "__main__":
    main()