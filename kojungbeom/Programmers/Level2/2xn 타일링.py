# DP 안 쓴 버전
def solution(n):
    answer = 0
    temp1 = 1
    temp2 = 1
    for i in range(n):
        answer += temp2
        temp1, temp2 = answer, temp1

    return answer % 1000000007


# DP 쓴 버전
def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1] % 1000000007