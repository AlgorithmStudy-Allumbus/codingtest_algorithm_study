"""
https://www.acmicpc.net/problem/2293

# 문제
- 가치가 다른 n 개의 종류의 동전을 활용해 총합 k 가 되는 경우의 수 
- 사용 순서는 구분하지 않는다(중복제외)

# 경우의 수 
# brude force
- n <= 100 

1. 목표 금액 k에 도달하기 까지 divde conquer /사용하는 동전 종류도 사전 순서대로 사용 
dp[lv][k] = dp[lv-1][k] + dp[lv][k-c]
2. 메모리 초과
=> dp 는 1차원 테이블로

"""
import sys

n , k = map(int,sys.stdin.readline().split())
coins = list()
dp = [0 for _ in range(k+1)]
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
# 가치가 작은 coin 부터 적용
coins.sort()
dp[0] = 1

for c in coins:
    for i in range(c, k+1) :
        dp[i] = dp[i] + dp[i-c]
print(dp[k])