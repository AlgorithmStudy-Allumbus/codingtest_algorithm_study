import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())  # 로프 개수
rope = [int(input()) for _ in range(N)]

# 내림차순 정렬
rope.sort(reverse=True)

# 최대 중량 계산
max_weight = 0
for i in range(N):
    # i + 1: 현재 사용된 로프 개수
    max_weight = max(max_weight, rope[i] * (i + 1))

print(max_weight)