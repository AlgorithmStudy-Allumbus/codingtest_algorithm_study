N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

# 뒤에서부터 dp 테이블 채우기
for i in range(N - 1, -1, -1):
    time, pay = schedule[i]
    
    # 상담을 할 수 있는 경우
    if i + time <= N:
        dp[i] = max(dp[i + 1], pay + dp[i + time])
    else:
        # 상담이 퇴사 이후까지 걸려서 할 수 없는 경우
        dp[i] = dp[i + 1]

print(dp[0])  