
def sort(arr,dp):
    global N

    for i in range(1,N,1):
        for j in range(i-1,-1,-1):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i],dp[j]+1)


N = int(input())

arr = list(map(int,input().split()))
dp = [1] * N

sort(arr, dp)

print(N-max(dp))

