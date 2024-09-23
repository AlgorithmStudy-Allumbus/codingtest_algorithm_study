
N = int(input())

T = [0]
P = [0]
dp = [0] * (N + 2)

for _ in range(N):
    arr = input().split()
    T.append(int(arr[0]))
    P.append(int(arr[1]))

dp[N + 1] = 0


for i in range(N, 0, -1):
    if i + T[i] <= N + 1:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
    else:
        dp[i] = dp[i + 1]

print(dp[1])
