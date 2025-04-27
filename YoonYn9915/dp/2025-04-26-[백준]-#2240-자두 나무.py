from sys import stdin

T, W = map(int, stdin.readline().split())


lst = [0]
dp = [[0]*(W+1) for _ in range(T+1)]

# 입력 받기
for _ in range(T):
    lst.append(int(stdin.readline()))

# DP 테이블 채우기
for i in range(1, T+1):
    if lst[i] == 1:
        # 이동을 한 번도 안 했을 경우 (항상 1번 나무 아래 있음)
        dp[i][0] = dp[i-1][0] + 1  # 자두 먹으면 +1
    else:
        # 1번 나무 아래 있는데 2번 나무에서 자두 떨어지면 못 먹음
        dp[i][0] = dp[i-1][0]

    # 이동 횟수 1회 이상부터
    for j in range(1, W+1):
        if lst[i] == 2 and j % 2 == 1:
            # 홀수번 이동했을 때는 2번 나무 아래 있음 → 2번 나무에서 자두 떨어지면 +1
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif lst[i] == 1 and j % 2 == 0:
            # 짝수번 이동했을 때는 1번 나무 아래 있음 → 1번 나무에서 자두 떨어지면 +1
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            # 자두 못 먹을 경우, 이동하거나 이동 안 하거나 둘 중 최대값만 가져오기
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))
