import sys
input = sys.stdin.readline

# 입력 및 초기화
S1 = input().strip()
S2 = input().strip()
n, m = len(S1), len(S2)
dp = [[""] * (m+1) for _ in range(n+1)]

# DP 채우기
for i in range(1, n+1):
    for j in range(1, m+1):
        # 문자가 같으면 이전 값에 현재 문자 더하기
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + S1[i-1]
        # 문자가 다르면 더 긴 걸로 선택
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

# 정답 출력
print(dp[n][m])