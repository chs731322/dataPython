import pandas as pd

df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

# 문제풀이 3
# 평균 점수 순위 만들기
sort = df.sort_values(by="평균", ascending=False).head(5)

print("[상위 5명 학생]")
print(sort)

sort.to_excel(
    "top5_students.xlsx",
    index=False
)