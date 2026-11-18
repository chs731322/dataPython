import pandas as pd

df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)
'''
print(df.head())
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df["이름"])
print(df["평균"])

result = df[["이름", "학과", "평균"]]
print(result)

print(df["평균"].mean()) # 평균
print(df["평균"].max())
print(df["평균"].min())
print(df["평균"].sum())
print(df["평균"].count())

korean = df["국어"].mean()
english = df["영어"].mean()
math = df["수학"].mean()

print(f"국어 평균: {korean:.2f}")
print(f"영어 평균: {english:.2f}")
print(f"수학 평균: {math:.2f}")

print(df["평균"] >= 90)  # 각 행이 90 이상인지 True/False로만 출력
print(df[df["평균"] >= 90])  # 평균 90 이상인 학생의 행(모든 열)만 골라서 출력

excellent = df[df["평균"] >= 80]
warning = df[df["평균"] < 70]

print("[전체 학생 데이터]")
print(df)
print("[평균 80점 이상 학생 데이터]")
print(excellent)
print("[평균 70점 이하 학생 데이터]")
print(warning)

result = df.sort_values(by="평균", ascending=False) # 평균 열을 기준으로 정렬, 내림차순

print(result)

department = input("검색할 학과: ")

result = df[df["학과"] == department]

if result.empty:
    print("검색 결과가 없습니다.")
else:
    print(result)

df["합격여부"] = "합격"

print(df.head())

result = df[(df["평균"] >= 80) & (df["학과"] == "멀티미디어학과")]

print("[전체 학생 데이터]")
print(df.head())

def check_result(average):
    if average >= 70:
        return "합격"
    else:
        return "재검토"

df["합격여부"] = df["평균"].apply(check_result)

print("\n[합격여부 추가 결과]")
print(df[["이름", "학과", "평균", "등급", "합격여부"]])
'''
'''
def get_status(avg):
    if avg >= 90:
        return "우수"
    elif avg < 70:
        return "주의"
    else:
        return "일반"

df["상태"] = df["평균"].apply(get_status)

print(df[["이름", "평균", "상태"]])
'''
'''
def make_status(average):
    if average >= 90:
        return "우수"
    elif average < 70:
        return "주의"
    else:
        return "일반"
    
df["상태"] = df["평균"].apply(make_status)

result = df[["이름", "평균", "상태"]]

print(result)

result.to_excel(
    "pandas_result.xlsx",
    index=False
)
'''
def check_result(average):
    if average >= 70:
        return "합격"
    else:
        return "불합격"

df["합격여부"] = df["평균"].apply(check_result)

print("\n[합격여부 추가 결과]")
print(df[["이름", "학과", "평균", "등급", "합격여부"]])