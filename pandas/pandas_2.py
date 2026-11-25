import pandas as pd

df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

# 문제풀이 2
# 수학 우수 학생 찾기
math_best = df[df["수학"] >= 90]

print("[수학 점수가 90점 이상인 학생]")
print(math_best)

math_best.to_excel(
    "math_best.xlsx",
    index=False
)