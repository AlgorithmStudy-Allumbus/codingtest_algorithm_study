import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
write_str = " " + input().strip()
answer_str = " " + input().strip()

# DP
dp = [[0] * (n + 1) for _ in range(m + 1)]

# 공집합 채우기
for i in range(1, m + 1):
    dp[i][0] = i
for j in range(1, n + 1):
    dp[0][j] = j

# 최소 편집으로 DP 채우기
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if write_str[j] == answer_str[i] or \
                (write_str[j] == 'i' and answer_str[i] == 'j') or \
                (write_str[j] == 'i' and answer_str[i] == 'l') or \
                (write_str[j] == 'v' and answer_str[i] == 'w'):
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1

# 정답 출력
print(dp[m][n])
