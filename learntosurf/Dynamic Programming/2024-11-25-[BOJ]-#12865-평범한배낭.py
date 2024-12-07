import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 물품의 개수, 버틸 수 있는 무게 

items = []
for _ in range(N):
    W, V = map(int, input().split()) 
    items.append((W, V)) # (물건의 개수, 물건의 가치)

def backpack(N, K, items):
    dp = [0] * (K+1) # 배낭 크기만큼 DP 테이블 초기화 
    
    for weight, value in items:
        for w in range(K, weight-1, -1): # 역순으로 반복
            dp[w] = max(dp[w], dp[w-weight] + value)
    
    return dp[K]

print(backpack(N, K, items))
