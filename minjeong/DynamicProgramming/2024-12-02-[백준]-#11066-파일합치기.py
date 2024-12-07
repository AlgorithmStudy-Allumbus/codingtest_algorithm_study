import sys
input = sys.stdin.readline

# 테스트 케이스 입력
T = int(input())

for _ in range(T):
    # 입력 처리
    K = int(input())
    files = [0] + list(map(int, input().split()))
    prefix_sum = [0] * (K + 1)

    # 누적합 계산
    for i in range(1, K + 1):
        prefix_sum[i] = prefix_sum[i - 1] + files[i]

    # DP 배열 초기화
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    # DP 계산
    for count in range(1, K):  # 합치는 파일 개수
        for start in range(1, K - count + 1):  # 시작 인덱스
            end = start + count
            MIN = sys.maxsize
            for mid in range(start, end):  # 중간 분할점
                MIN = min(MIN, dp[start][mid] + dp[mid + 1][end])
            dp[start][end] = MIN + prefix_sum[end] - prefix_sum[start - 1]

    # 결과 출력
    print(dp[1][K])
