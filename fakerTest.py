from faker import Faker
import random

fake = Faker("ko_KR")  # Set the locale to Korean

'''
for i in range(1, 6):  # Generate 5 fake profiles
    print("=== " + str(i) + "번째 데이터 ===")
    print("이름: ", fake.name())
    print("주소: ", fake.address())
    print("이메일: ", fake.email())
    print("전화번호: ", fake.phone_number())
    print()
'''

'''
for _ in range(5):  
    student = {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }
    print(student)
'''

students = []

for i in range(10):
    student = {
        "name": fake.name(),
        "department": random.choice([
            "컴퓨터공학과", 
            "전자공학과",
            "멀티미디어학과"
        ]),
        "korean": random.randint(50, 100),
        "english": random.randint(50, 100),
        "math": random.randint(50, 100)
    }
    students.append(student)
    
print("\n=== 학생 성적 리스트 ===")
for student in students:
    print(f"이름: {student['name']} | 학과: {student['department']} | 국어: {student['korean']}, 영어: {student['english']}, 수학: {student['math']}")
    print()