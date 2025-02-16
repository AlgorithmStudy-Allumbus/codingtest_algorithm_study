import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

dp = [[0] * M for _ in range(N)]

# 첫 줄
dp[0][0] = nums[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j - 1] + nums[0][j]

# 왼쪽 누적합 업데이트 -> 오른쪽 누적합 업데이트, 이후 둘 중 더 큰 값으로 업데이트
for i in range(1, N):

    left_prefix_sum = [0] * M  # 왼쪽 누적합
    right_prefix_sum = [0] * M  # 오른쪽 누적합

    # 왼쪽 누적합
    left_prefix_sum[0] = dp[i-1][0] + nums[i][0]
    for j in range(1, M):
        left_prefix_sum[j] = max(dp[i-1][j], left_prefix_sum[j-1]) + nums[i][j]

    # 오른쪽 누적합
    right_prefix_sum[M-1] = dp[i-1][M-1] + nums[i][M-1]
    for j in range(M-2, -1, -1):
        right_prefix_sum[j] = max(dp[i-1][j], right_prefix_sum[j+1]) + nums[i][j]

    # DP에 저장
    for j in range(M):
        dp[i][j] = max(left_prefix_sum[j], right_prefix_sum[j])

# 정답 출력
print(dp[N-1][M-1])