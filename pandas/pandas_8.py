import pandas as pd

# 문제풀이 8
df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

max_korean = df["국어"].max()
max_english = df["영어"].max()
max_math = df["수학"].max()

print("[교과목별 최고점]")
print(f"국어 최고점: {max_korean}")
print(f"영어 최고점: {max_english}")
print(f"수학 최고점: {max_math}")