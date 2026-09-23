values = []

def show_average(data):
    if len(data) == 0:
        print("데이터가 없습니다.")
    else:
        average = sum(data) / len(data)
        print(f"평균: {average:.2f}")

def add_data():
    try:
        number = int(input("숫자를 입력하세요: "))
        values.append(number)
        print("저장되었습니다.")
    except ValueError:
        print("숫자만 입력하세요.")

def show_data():
    print(values)

def show_max_min():
    if len(values) == 0:
        print("데이터가 없습니다.")
    else:
        print(f"최대값: {max(values)}")
        print(f"최소값: {min(values)}")

def search_data():
    if len(values) == 0:
        print('데이터 없음')
    else:
        try:
            number = int(input("찾을 숫자를 입력하세요: "))

            if number in values:
                print(f"{number}이 있습니다.")
            else:
                print(f"{number}이 없습니다.")
        except ValueError:
            print("숫자만 입력")

def delete_data():
    if len(values) == 0:
        print("데이터가 없습니다.")
    else:
        try:
            number = int(input("삭제할 숫자를 입력하세요: "))

            if number in values:
                values.remove(number)
                print(f"{number}을(를) 삭제했습니다.")
            else:
                print("해당 숫자가 없습니다.")

        except ValueError:
            print("숫자만 입력하세요.")

def sort_ascending():
    if len(values) == 0:
        print("데이터가 없습니다.")
    else:
        values.sort()
        print("오름차순으로 정렬했습니다.")
        print(values)

def sort_descending():
    if len(values) == 0:
        print("데이터가 없습니다.")
    else:
        values.sort(reverse=True)
        print("내림차순으로 정렬했습니다.")
        print(values)

def update_data():
    if len(values) == 0:
        print("데이터가 없습니다.")
        return

    try:
        index = int(input("수정할 위치 번호: "))
        new_value = int(input("새로운 값: "))

        if 0 <= index < len(values):
            values[index] = new_value
            print("수정되었습니다.")
        else:
            print("없는 위치입니다.")

    except ValueError:
        print("숫자만 입력하세요.")

def show_count():
    print(f"현재 데이터 개수 : {len(values)}개")

def clear_data():
    values.clear()
    print('모든 데이터를 삭제했습니다.')

def show_index():
    try:
        index = int(input("위치 번호 입력: "))

        if 0 <= index < len(values):
            print(values[index])
        else:
            print("없는 위치입니다.")

    except ValueError:
        print("숫자만 입력하세요.")

print("\n========== 메뉴 ==========")
while True:
    try:
        menu = int(input("1.입력  2.보기  3.평균  4.최소값/최대값"
            "5.검색  6.삭제  7.오름차순  8.내림차순  9. 수정 10. count 11. 모두 삭제 12. 원하는 위치 숫자 보기 0.종료:" ))

        if menu == 1:
            add_data()
        elif menu == 2:
            show_data()
        elif menu == 3:
            show_average(values)
        elif menu == 4:
            show_max_min()
        elif menu == 5:
            search_data()
        elif menu == 6:
            delete_data()
        elif menu == 7:
            sort_ascending()
        elif menu == 8:
            sort_descending()
        elif menu == 9:
            update_data()
        elif menu == 10:
            show_count()
        elif menu == 11:
            clear_data()
        elif menu == 12:
            show_index()
        elif menu == 0:
            print("프로그램을 종료합니다.")
            break
        else:
            print("0~8 중에서 선택하세요.")
    except ValueError:
        print("숫자만 입력하세요.")
        break