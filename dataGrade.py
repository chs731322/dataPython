from openpyxl import load_workbook, Workbook

workbook = load_workbook("students.xlsx")
worksheet = workbook["학생 점수"]

# 등급 열 추가
worksheet.cell(row=1, column=3, value="등급")
# worksheet["C1"] = "등급"

for row in range(2, worksheet.max_row + 1):
    score = worksheet.cell(row=row, column=2).value
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    worksheet.cell(row=row, column=3, value=grade)

# 저장
workbook.save("students.xlsx")

# 학생 점수와 등급 출력
for row in range(2, worksheet.max_row + 1):
    name = worksheet.cell(row=row, column=1).value
    score = worksheet.cell(row=row, column=2).value
    grade = worksheet.cell(row=row, column=3).value
    print(f"{name} : {score}점 -> {grade}등급")