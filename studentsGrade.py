from openpyxl import load_workbook

workbook = load_workbook("students.xlsx")
worksheet = workbook["학생 점수"]


def search_student(worksheet, target_name):
    scores = []
    print(f"\n{target_name} 학생 성적")

    for row in worksheet.iter_rows(min_row=2, values_only=True):
        student_id, name, subject, score, grade = row[:5]

        if name is not None and str(name).strip() == target_name.strip():
            print(f"{subject} : {score}점 / {grade}등급")
            if isinstance(score, (int, float)):
                scores.append(score)

    if scores:
        total = sum(scores)
        average = total / len(scores)

        print(f"\n성적 개수: {len(scores)}개")
        print(f"총점: {total}점")
        print(f"평균 점수: {average:.2f}점")
    else:
        print("해당 이름의 학생을 찾을 수 없습니다.")


name = input("조회할 학생 이름을 입력하세요: ")
search_student(worksheet, name)