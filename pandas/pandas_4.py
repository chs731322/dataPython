import pandas as pd

# 문제풀이 4
df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

print("[전체 학생의 평균 점수 출력]")
print(df["평균"])

best = df[df["평균"] >= 90]
bad = df[df["평균"] < 70]

sorted_df = df.sort_values(by="평균", ascending=False)
print("[평균 높은 순 정렬]")
print(sorted_df)

def get_status(avg):
    if avg >= 90:
        return "우수"
    elif avg < 70:
        return "주의"
    else:
        return "일반"

df["상태"] = df["평균"].apply(get_status)
print("[상태 열 추가]")
print(df)
