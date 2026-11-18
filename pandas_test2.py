import pandas as pd

df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

print("[전체 학생 데이터]")
print(df[["이름", "평균"]])

excellent = df[df["평균"] >= 80]
result = excellent[["이름", "학과", "평균"]]
result.to_excel(
        "high_students.xlsx",
        index=False
)