import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1 # 0원을 만드는 경우의 수는 1 (아무 동전도 사용하지 않는 경우)

for coin in coins: 
    for j in range(coin, k+1):
        dp[j] += dp[j - coin] # 점화식

print(dp[k])