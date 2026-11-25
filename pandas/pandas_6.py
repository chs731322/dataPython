import pandas as pd

# 문제풀이 6
df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

good = df[(df["국어"] >= 80) & (df["영어"] >= 80)]

result = good[["이름", "국어", "영어", "평균"]]

print("[국어, 영어 모두 80점 이상 학생]")
print(result)

result.to_excel(
    "good_language_students.xlsx", 
    index=False
)

print("\ngood_language_students.xlsx 파일로 저장되었습니다.")