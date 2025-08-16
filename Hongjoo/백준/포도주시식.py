"""
https://www.acmicpc.net/problem/2156
# 문제 : 최대한 많은 양의 포도주 섭취
<조건>
1. 선택한 잔의 포두주는 모두 섭취 ,마신 뒤 원상복귀
2. 연속으로 놓여진 3잔 모두 섭취 불가

# 최대문제 -> "DP" 

점화식
dp[i] : 현재 i  에서 최대 마실 수 있는 포도주 총합
1. 현재 O , 이전 O , 전전 x   : 
2. 현재 , 이전 x , 전전 O  = 
3. 현재 x , 이전  o , 전전 o  = 
 dp[i] = max(cups[i] + cups[i-1] + dp[i-3] , cups[i] + dp[i-2] , dp[i-1])
"""
# 1. 입력변수 
N = int(input())
cups = [int(input()) for _ in range(N)]

# 2. 
dp = [0]*N

dp[0] = cups[0]
if N >=2 : 
    dp[1] = sum(cups[0:2])
if N >= 3 : 
    dp[2] = max(cups[2] + cups[1] , cups[2] + cups[0] , dp[1])
if N >= 4 : 
    for i in range(3,N):
        dp[i] = max(cups[i] + cups[i-1] + dp[i-3] , cups[i] + dp[i-2] , dp[i-1])
# print(dp)
print(dp[-1])