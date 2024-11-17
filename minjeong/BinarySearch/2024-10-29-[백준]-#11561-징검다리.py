import sys
input = sys.stdin.readline

def calculate_count(n):
    left = 1 # 가장 적게 밟을 수 있는 징검다리 수는 1개 (최소 범위)
    right = n # 최대 범위는 N
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        # 1부터 mid까지의 합: sum = mid * (mid + 1) // 2
        if mid * (mid + 1) // 2 <= n: # 점프 거리의 합이 n보다 작거나 같으면
            left = mid + 1 # 더 큰 점프 수를 시도합니다 (점프 수를 늘려봄)
            answer = mid # 가능한 점프 수를 저장
        else:
            right = mid - 1 # 합이 너무 크다면 점프 수를 줄인다.
    return answer


t = int(input()) # 테스트케이스 수

for _ in range(t):
    n = int(input()) # 징검다리의 총 수
    print(calculate_count(n))