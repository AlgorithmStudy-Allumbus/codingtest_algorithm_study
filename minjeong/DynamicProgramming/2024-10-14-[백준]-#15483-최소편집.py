import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

# 2차원 배열 초기화: (len(A)+1) x (len(B)+1) 크기
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

# 초기값 설정: 빈 문자열에서 변환 비용
for i in range(len(A)+1):
    dp[i][0] = i
for i in range(len(B)+1):
    dp[0][i] = i

# DP 배열 채우기
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]: # 문자가 같다면 교체 비용 X(왼쪽 대각선 값)
            dp[i][j] = dp[i-1][j-1]
        else: # 다르다면 왼쪽, 위쪽, 왼쪽 대각선 위 중 최소값에 중 +1
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

# 최소 편집 횟수 출력
print(dp[-1][-1])