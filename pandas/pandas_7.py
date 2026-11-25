import pandas as pd

# 문제풀이 7
df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

normal = df[(df["평균"] >= 70) & (df["평균"] < 90)]

result = normal[["이름", "학과", "평균", "등급"]]

result = result.sort_values(by="평균", ascending=False)

print("[평균 70~89점 일반 학생]")
print(result)