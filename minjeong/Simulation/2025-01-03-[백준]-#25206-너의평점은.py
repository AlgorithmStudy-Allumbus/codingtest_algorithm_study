import sys
input = sys.stdin.readline

# 1. 과목 평점 테이블 (딕셔너리 사용)
rating = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

# 2. 변수 초기화
total_score = 0  # 총 평점 (학점 * 과목 평점의 합)
total_credit = 0  # 총 학점

# 3. 과목별 입력 및 평점 계산
for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)  # 학점은 소수점으로 변환

    if grade != 'P':  # P 등급 과목 제외
        total_score += credit * rating[grade]
        total_credit += credit

# 4. 전공 평점 계산 및 출력
GPA = total_score / total_credit
print("{:.6f}".format(GPA))  # 소수점 6자리 출력