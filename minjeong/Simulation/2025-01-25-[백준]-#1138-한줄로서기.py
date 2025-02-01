import sys

input = sys.stdin.readline

# 입력 받기
N = int(input())  # 사람 수
taller = list(map(int, input().split()))  # 각 사람이 기억하는 왼쪽 큰 사람의 수

# 결과 리스트 초기화
result = [None] * N

# 키가 작은 사람(1부터 N까지)을 처리
for i in range(1, N + 1):  # i는 현재 사람의 키
    count = taller[i - 1]  # 현재 사람이 기억하는 왼쪽 큰 사람의 수
    idx = 0  # result에서 위치를 찾기 위한 인덱스

    while count > 0 or result[idx] is not None:  # 빈 자리가 아니고 count가 남아있다면 이동
        if result[idx] is None:  # 빈 자리일 경우에만 count 감소
            count -= 1
        idx += 1  # 다음 자리로 이동

    result[idx] = i  # 적절한 자리에 현재 사람 배치

# 결과 출력
print(*result)
