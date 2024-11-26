N = int(input())

def operation(N):
    dp = [0] * (N+1)
    
    for i in range(2, N+1): # 1은 연산이 필요하지 않음 
        dp[i] = dp[i-1] + 1
        
        if i%2==0:
            dp[i] = min(dp[i], dp[i//2]+1)
        
        if i%3==0:
            dp[i] = min(dp[i], dp[i//3]+1)

    return dp[N]

print(operation(N))