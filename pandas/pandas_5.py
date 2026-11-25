import pandas as pd

# 문제풀이 5
df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

print("[전체 학생 평균]")
print(df[["이름", "평균"]])

dept = input("검색할 학과를 입력하세요: ").strip()

result = df[df["학과"] == dept]

if result.empty:
    print("검색 결과가 없습니다.")
else:
    print(result[["이름", "학과", "평균", "등급"]])