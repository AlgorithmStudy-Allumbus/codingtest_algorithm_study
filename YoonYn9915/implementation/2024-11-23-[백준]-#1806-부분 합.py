import sys

# 입력 처리
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 초기화
ans = float('inf')
start, end = 0, 0
current_sum = 0

# 투 포인터로 부분합 찾기
while end < N:
    current_sum += arr[end]
    end += 1

    # 현재 합이 S 이상일 경우
    while current_sum >= S:
        ans = min(ans, end - start)
        current_sum -= arr[start]
        start += 1


print(0 if ans == float('inf') else ans)
