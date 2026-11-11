from faker import Faker
from openpyxl import Workbook
import random

# 1. 기본 설정
FILE_NAME = "product_sales.xlsx"
SHEET_NAME = "판매정보"
PRODUCT_COUNT = 8

# Faker 객체 생성
fake = Faker("ko_KR")

# 2. 판매수량을 이용하여 상태 계산
def calculate_status(quantity):
    if quantity >= 15:
        return "인기"
    elif quantity < 5:
        return "주의"
    else:
        return "일반"

# 3. 상품 판매 데이터를 생성하고 Excel 파일로 저장
def create_product_sales():
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = SHEET_NAME

    # 헤더 작성
    sheet.append(["상품명", "판매자", "단가", "판매수량", "매출액", "상태"])

    # 상품 판매 데이터 8개 생성
    for i in range(1, PRODUCT_COUNT + 1):
        product_name = f"상품{i}"
        seller = fake.name()
        # 10,000원 ~ 50,000원 사이 (예시 화면처럼 10,000원 단위)
        price = random.randrange(10000, 50001, 10000)
        # 1 ~ 20개 사이
        quantity = random.randint(1, 20)
        # 매출액 = 단가 x 판매수량
        sales = price * quantity
        status = calculate_status(quantity)

        sheet.append([product_name, seller, price, quantity, sales, status])

    try:
        workbook.save(FILE_NAME)
        print(f"{FILE_NAME} 파일이 생성되었습니다.")
    except PermissionError:
        print("Excel 파일이 열려 있어 저장할 수 없습니다.")
        print("Excel 파일을 닫은 후 다시 실행하세요.")
    finally:
        workbook.close()

# 4. 프로그램 실행
create_product_sales()