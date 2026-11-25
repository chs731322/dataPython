import pandas as pd

df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

# 문제풀이 1
# 평균 80점 이상 학생 찾기
high = df[df["평균"] >= 80]

print("[평균이 80점 이상인 학생]")
print(high)

high.to_excel(
    "high_results.xlsx",
    index=False
)