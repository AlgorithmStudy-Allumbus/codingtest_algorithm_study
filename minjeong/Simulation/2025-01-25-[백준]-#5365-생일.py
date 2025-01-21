import sys
input = sys.stdin.readline

# 입력 받기
students = []
for _ in range(int(input())):
    name, day, month, year = input().split()
    students.append((int(year), int(month), int(day), name))  # 튜플로 저장

# 정렬: 연도 -> 월 -> 일 기준
students.sort()

# 가장 나이가 적은 사람과 많은 사람 출력
print(students[-1][3])  # 가장 나이가 적은 사람
print(students[0][3])  # 가장 나이가 많은 사람
