def solution(m, n, puddles):
    puddles = [[q, p] for [p, q] in puddles]

    # dp 초기화    
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1

    # 장애물 있는 경우가 아니면 dp에 누적하여 값 더하기
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] += (dp[i-1][j] + dp[i][j-1])% 1000000007

    # 정답 반환
    return dp[n][m]