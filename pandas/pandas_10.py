import pandas as pd

df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

def make_status(average):
    if average >= 90:
        return "우수"
    elif average < 70:
        return "주의"
    else:
        return "일반"
    
df["상태"] = df["평균"].apply(make_status)

result = df[["이름","학과", "국어", "영어", "수학", "평균", "등급", "상태"]].sort_values(by="평균", ascending=False)

print(result)

result.to_excel(
    "pandas_analysis_result.xlsx",
    index=False
)