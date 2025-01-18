def solution(n):
    # DP 테이블 초기화
    dp = [0] * (n + 1)
    dp[0] = 1  # 초기값 설정 (괄호가 없는 경우)

    # 카탈란 수 점화식 적용
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[n]  # n개의 괄호쌍으로 만들 수 있는 경우의 수 반환
