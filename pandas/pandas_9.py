import pandas as pd

df = pd.read_excel(
    "faker_students.xlsx",
    sheet_name="학생 성적"
)

def check_result(average):
    if average >= 70:
        return "합격"
    else:
        return "재검토"
    
df["합격여부"] = df["평균"].apply(check_result)

result = df[["이름", "평균", "등급", "합격여부"]]

print("[학생 합격여부 결과]")
print(result)

result.to_excel("student_pass_result.xlsx", index=False)