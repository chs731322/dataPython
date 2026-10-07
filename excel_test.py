from openpyxl import Workbook

# 새로운 Excel 파일 만들기
workbook = Workbook()

worksheet = workbook.active
worksheet.title = "학생 점수"

worksheet.append(["이름", "점수"])

worksheet.append(["홍길동", 85])
worksheet.append(["김철수", 92])
worksheet.append(["이영희", 78])

# Excel 파일 저장
workbook.save("students.xlsx")
print("Excel 파일이 생성되었습니다.")