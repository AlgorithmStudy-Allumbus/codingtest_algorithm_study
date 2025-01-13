import sys
input = sys.stdin.readline

# 입력
S1 = input().strip()
S2 = input().strip()

# DP 초기화
dp = [[0] * (len(S1) + 1) for _ in range(len(S2) + 1)]

# DP 채우기
for i in range(1, len(S2)+1):
    for j in range(1, len(S1)+1):
        if S2[i-1] == S1[j-1]:
            # 이전 값을 그대로 가져오거나 직전 문자열이 이어지고 있다면 +1 하거나
            dp[i][j] = dp[i-1][j-1] + 1

# 정답 출력
print(max(max(row) for row in dp))