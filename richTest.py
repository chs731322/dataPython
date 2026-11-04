from openpyxl import load_workbook
from rich.console import Console
from rich.table import Table

FILE_NAME = "students.xlsx"
SHEET_NAME = "성적결과"

try:
    workbook = load_workbook(FILE_NAME)
except FileNotFoundError:
    print(f"{FILE_NAME} 파일을 찾을 수 없습니다.")
    print("Python 파일과 Excel 파일이 같은 폴더에 있는지 확인하세요.")
    exit()

if SHEET_NAME not in workbook.sheetnames:
    print(f"{SHEET_NAME} 시트를 찾을 수 없습니다.")
    print("현재 시트 목록:", workbook.sheetnames)
    workbook.close()
    exit()

sheet = workbook[SHEET_NAME]

console = Console()

def make_table(title):
    table = Table(
        title=title,
        show_header=True, header_style="bold"
    )
    table.add_column("학번", justify="center")
    table.add_column("이름", justify="center")
    table.add_column("학과", justify="left")
    table.add_column("국어", justify="right")
    table.add_column("영어", justify="right")
    table.add_column("수학", justify="right")
    table.add_column("총점", justify="right")
    table.add_column("평균", justify="right")
    table.add_column("등급", justify="center")
    table.add_column("상태", justify="center")
    return table

def all_students():

    table = make_table("학생 성적 관리 프로그램")

    for row in range(2, sheet.max_row + 1):
        student_id = sheet.cell(row=row, column=1).value
        name = sheet.cell(row=row, column=2).value
        department = sheet.cell(row=row, column=3).value
        korean = sheet.cell(row=row, column=4).value
        english = sheet.cell(row=row, column=5).value
        math = sheet.cell(row=row, column=6).value
        total = sheet.cell(row=row, column=7).value
        average = sheet.cell(row=row, column=8).value
        grade = sheet.cell(row=row, column=9).value

        if average >= 90:
            status = "[yellow]우수[/yellow]"
        elif average < 70:
            status = "[magenta]주의[/magenta]"
        else:
            status = "[blue]일반[/blue]"

        if grade == "A":
            grade_text = f"[green]{grade}[/green]"
        elif grade == "D" or grade == "F":
            grade_text = f"[yellow]{grade}[/yellow]"
        else:
            grade_text = str(grade)

        table.add_row(
            str(student_id), str(name),
            str(department), str(korean), str(english),
            str(math), str(total), f"{average:.2f}", grade_text, status
        )
            
    console.print(table)

def good_students():
    good_table = make_table("우수 학생 목록")

    for row in range(2, sheet.max_row + 1):
        average = sheet.cell(row=row, column=8).value
        if average >= 90:
            student_id = sheet.cell(row=row, column=1).value
            name = sheet.cell(row=row, column=2).value
            department = sheet.cell(row=row, column=3).value
            korean = sheet.cell(row=row, column=4).value
            english = sheet.cell(row=row, column=5).value
            math = sheet.cell(row=row, column=6).value
            total = sheet.cell(row=row, column=7).value
            grade = sheet.cell(row=row, column=9).value

            status = "[yellow]우수[/yellow]"
            grade_text = f"[green]{grade}[/green]"

            good_table.add_row(
                str(student_id), str(name),
                str(department), str(korean), str(english),
                str(math), str(total), f"{average:.2f}",
                grade_text, status
            )

    console.print(good_table)

def caution_students():
    caution_table = make_table("주의 학생 목록")

    for row in range(2, sheet.max_row + 1):
        average = sheet.cell(row=row, column=8).value
        if average < 70:
            student_id = sheet.cell(row=row, column=1).value
            name = sheet.cell(row=row, column=2).value
            department = sheet.cell(row=row, column=3).value
            korean = sheet.cell(row=row, column=4).value
            english = sheet.cell(row=row, column=5).value
            math = sheet.cell(row=row, column=6).value
            total = sheet.cell(row=row, column=7).value
            grade = sheet.cell(row=row, column=9).value

            status = "[magenta]주의[/magenta]"
            grade_text = f"[yellow]{grade}[/yellow]"

            caution_table.add_row(
                str(student_id), str(name),
                str(department), str(korean), str(english),
                str(math), str(total), f"{average:.2f}",
                grade_text, status
            )

    console.print(caution_table)

while True:
    
    menu = input("1. 전체 학생 조회\n2. 우수학생 조회\n3. 주의학생 조회\n4. 종료\n메뉴를 선택하세요: ").strip()

    try:
        menu = int(menu)
    except ValueError:
        print("잘못된 입력입니다.")
        exit()

    if menu == 1:
        all_students()
    elif menu == 2:
        good_students()
    elif menu == 3:
        caution_students()
    elif menu == 4:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")

    workbook.close()