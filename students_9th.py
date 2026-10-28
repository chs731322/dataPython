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
# 1. 학번으로 검색하는 함수
# ------------------------------------------------
def search_by_student_id(students):
    student_id = input("조회할 학번: ").strip()

    if student_id in students:
        print_student_info(student_id, students[student_id])
    else:
        print("해당 학번의 학생이 없습니다.")


# ------------------------------------------------
# 2. 이름으로 검색하는 함수
# ------------------------------------------------
def search_by_name(students):
    name = input("조회할 학생 이름: ").strip()
    found = False

    # 같은 이름의 학생이 여러 명일 수 있으므로 끝까지 확인
    for student_id, student in students.items():
        if student["name"] == name:
            print_student_info(student_id, student)
            found = True

    if not found:
        print("해당 이름의 학생이 없습니다.")


# ------------------------------------------------
# 전체 성적결과를 화면에 출력하는 함수
# ------------------------------------------------
def show_all_results(result_sheet):
    print("\n[전체 성적결과]")

    for row in result_sheet.iter_rows(min_row=2, values_only=True):
        student_id, name, department, korean, english, math, total, average, grade = row
        print(
            f"{student_id} / {name} / {department} / "
            f"국어 {korean} / 영어 {english} / 수학 {math} / "
            f"총점 {total} / 평균 {average:.2f} / {grade}등급"
        )


# ------------------------------------------------
# 4. 과목별 통계를 화면에 출력하는 함수
# ------------------------------------------------
def show_subject_statistics(students):
    # 국어, 영어, 수학 점수를 각각 저장할 빈 리스트를 딕셔너리 안에 만듦.
    subject_scores = {"국어": [], "영어": [], "수학": []}
    # students.values()는 학생정보에서 학번을 제외한 학생 데이터만 하나씩 가져옴.
    for student in students.values():
        for item in student["subjects"]:  # 현재 학생의 과목별 성적을 하나씩 가져옴
            subject = item["subject"]  # 과목명을 가져옴.
            score = item["score"]  # 점수를 가져옴.
            # 해당 과목이 국어, 영어, 수학 중 하나인지 확인.
            if subject in subject_scores:
                # 과목에 맞는 리스트에 점수를 추가.
                subject_scores[subject].append(score)

    print("\n==============================")
    print("          과목별 통계")
    print("==============================")
    # items()를 사용하여 과목명과 점수 리스트를 함께 가져옴.
    for subject, scores in subject_scores.items():
        if len(scores) == 0:  # 해당 과목의 점수가 없는 경우
            print(f"\n[{subject}]")
            print("등록된 점수가 없습니다.")
            continue  # 다음 과목으로 이동합니다.
        # 과목 평균을 계산합니다.
        average = sum(scores) / len(scores)
        highest = max(scores)  # 가장 높은 점수를 구함.
        lowest = min(scores)  # 가장 낮은 점수를 구함.
        print(f"\n[{subject}]")
        print(f"응시자 수: {len(scores)}명")  # len()으로 해당 과목의 학생 수를 구함.
        print(f"평균 점수: {average:.2f}점")  # :.2f는 소수점 둘째 자리까지 출력.
        print(f"최고 점수: {highest:g}점")  # :g는 불필요한 소수점 0을 제거
        print(f"최저 점수: {lowest:g}점")


# ------------------------------------------------
# 5. 학생별 총점과 평균을 리스트로 만드는 함수
# ------------------------------------------------
def build_student_summary(students):
    results = []  # 학생별 계산 결과를 저장할 빈 리스트
    # 학번과 학생정보를 하나씩 가져옵니다.
    for student_id, student in students.items():
        scores = []  # 현재 학생의 점수를 저장할 리스트
        # 현재 학생의 과목별 성적을 하나씩 확인합니다.
        for item in student["subjects"]:
            scores.append(item["score"])  # 점수만 scores 리스트에 추가
        # 등록된 성적이 없는 학생은 석차 계산에서 제외
        if len(scores) == 0:
            continue
        # 총점을 계산
        total = sum(scores)
        average = total / len(scores)  # 평균을 계산.
        grade = calculate_grade(average)  # 평균에 따른 최종등급을 계산.
        results.append({  # 학생 한 명의 결과를 딕셔너리로 저장
            "student_id": student_id,  # 학생의 학번
            "name": student["name"],  # 학생의 이름
            "department": student["department"],  # 학생의 학과
            "total": total,  # 총점
            "average": average,  # 평균
            "grade": grade  # 최종등급
        })
    # 학생별 계산 결과가 들어 있는 리스트를 반환합니다.
    return results


# ------------------------------------------------
# 5. 학생 평균값을 반환하는 함수 정렬할 때 기준으로 사용.
# ------------------------------------------------
def get_average(student_result):
    # 학생 결과 딕셔너리에서 average 값을 반환.
    return student_result["average"]


# ------------------------------------------------
# 5. 학생 평균 석차를 화면에 출력하는 함수
# ------------------------------------------------
def show_student_ranking(students):
    results = build_student_summary(students)  # 학생별 총점과 평균 결과
    if len(results) == 0:  # 석차를 계산할 학생이 없는 경우
        print("석차를 계산할 성적이 없습니다.")
        return
    # 평균 점수가 높은 순서로 정렬.
    # key=get_average: get_average 함수가 반환한 평균을 정렬 기준으로 사용.
    # reverse=True: 큰 값부터 작은 값 순서로 정렬.
    results.sort(key=get_average, reverse=True)
    print("\n==============================")
    print("          학생 평균 석차")
    print("==============================")
    # enumerate()는 순서 번호와 데이터를 함께 가져옴.
    # start=1을 사용하면 번호가 1부터 시작.
    for rank, result in enumerate(results, start=1):
        print(f"{rank}위 / "
              f"{result['student_id']} / "
              f"{result['name']} / "
              f"{result['department']} / "
              f"총점 {result['total']:g}점 / "
              f"평균 {result['average']:.2f}점 / "
              f"{result['grade']}등급"
        )


# ------------------------------------------------
# 6. 우수 학생과 주의 학생을 출력하는 함수
# ------------------------------------------------
def show_excellent_caution_students(students):
    # build_student_summary() 함수를 이용하여 학생별 학번, 이름, 학과, 총점, 평균, 등급을 가져옴.
    results = build_student_summary(students)
    excellent_students = []  # 우수 학생을 저장할 빈 리스트
    caution_students = []  # 주의 학생을 저장할 빈 리스트.
    for result in results:  # 학생별 결과를 하나씩 확인.
        average = result["average"]  # 현재 학생의 평균 점수를 가져옴.

        if average >= 90:  # 평균이 90점 이상이면 우수 학생
            excellent_students.append(result)
        elif average < 70:  # 평균이 70점 미만이면 주의 학생.
            caution_students.append(result)

    # 우수 학생은 평균이 높은 순서로 정렬.
    # key=get_average: 평균값을 정렬 기준으로 사용.
    # reverse=True: 큰 값부터 작은 값 순서로 정렬.
    excellent_students.sort(key=get_average, reverse=True)
    # 주의 학생은 평균이 낮은 순서로 정렬합니다.
    # reverse를 작성하지 않으면 기본적으로 작은 값부터 큰 값 순서로 정렬.
    caution_students.sort(key=get_average)
    print("\n==============================")
    print("      우수·주의 학생 조회")
    print("==============================")
    print("\n[우수 학생]")

    if len(excellent_students) == 0:  # 우수 학생이 한 명도 없는 경우
        print("우수 학생이 없습니다.")
    else:  # 우수 학생이 있는 경우
        # enumerate()는 순서 번호와 학생 데이터를 함께 가져오는 기능
        # start=1을 사용하면 번호가 1부터 시작.
        for number, student in enumerate(excellent_students, start=1):

            print(f"{number}. "
                  f"{student['student_id']} / "
                  f"{student['name']} / "
                  f"{student['department']} / "
                  f"평균 {student['average']:.2f}점 / "
                  f"{student['grade']}등급")
    # 주의 학생 출력
    print("\n[주의 학생]")

    if len(caution_students) == 0:  # 주의 학생이 한 명도 없는 경우
        print("주의 학생이 없습니다.")
    else:  # 주의 학생이 있는 경우
        for number, student in enumerate(caution_students, start=1):
            print(f"{number}. "
                  f"{student['student_id']} / "
                  f"{student['name']} / "
                  f"{student['department']} / "
                  f"평균 {student['average']:.2f}점 / "
                  f"{student['grade']}등급")
    # 우수 학생과 주의 학생의 인원을 출력합니다.
    print("\n[분류 결과]")
    print(f"우수 학생 수: "
          f"{len(excellent_students)}명")
    print(f"주의 학생 수: "
          f"{len(caution_students)}명")


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

    # 데이터를 학번 기준으로 연결
    students = read_student_info(student_sheet)
    connect_score_info(score_sheet, students)

    # 데이터를 이용해 성적결과 시트 작성
    result_sheet = create_result_sheet(workbook, students)

    # 등급과 성적결과를 엑셀에 저장 (엑셀에서 파일이 열려 있으면 저장 실패)
    try:
        workbook.save(file_path)
    except PermissionError:
        print("엑셀 파일이 열려 있어 저장하지 못했습니다. 파일을 닫고 다시 실행하세요.")

    # 검색 메뉴 반복 실행
    while True:
        print("\n==============================")
        print("       학생 성적 조회")
        print("==============================")
        print("1. 학번으로 검색")
        print("2. 이름으로 검색")
        print("3. 전체 성적결과 보기")
        print("4. 과목별 통계 보기")
        print("5. 학생 평균 석차 보기")
        print("6. 우수·주의 학생 보기")
        print("0. 종료")

        menu = input("메뉴 선택: ").strip()

        if menu == "1":
            search_by_student_id(students)
        elif menu == "2":
            search_by_name(students)
        elif menu == "3":
            show_all_results(result_sheet)
        # 4번: 과목별 평균, 최고점, 최저점 출력
        elif menu == "4":
            show_subject_statistics(students)
        # 학생 평균 석차 출력
        elif menu == "5":
            show_student_ranking(students)
        # 6번: 우수 학생과 주의 학생 출력
        elif menu == "6":
            show_excellent_caution_students(students)
        elif menu == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("0~6 중에서 선택하세요.")

    workbook.close()


if __name__ == "__main__":
    main()