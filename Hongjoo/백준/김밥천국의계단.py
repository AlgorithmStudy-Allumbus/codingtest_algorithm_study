"""
https://www.acmicpc.net/problem/28069

- 0 ~ N-1 번 계단 옆에 목표 김밥집
- 2가지 중 택 1을 K번 반복하여 김밥집(=N) 에 도달하자

  (1) nex_i = 계단 +1 
  (2) nex_i = i + i//2 
-> goal)K번 행동으로 0 -> N 까지 도달 여부 확인하기
(1<=n<=1000000)
# 유형 : 그래프 탐색 - DFS/BFS
- 목적지 "K" 까지 도달 여부 확인

# 출력 
김밥 도달 = minigimbob
물 = water

# 풀이 renewal : BFS는 시간 초과난다고 하고,  횟수 count 를 어떻게 해야할지 모르겠다
# 보편적 풀이인 DP 로 간다 
- 점화식 


"""
import sys
from collections import deque
#1. 입력 변수
N , K = map(int, sys.stdin.readline().split())
# DP
INF = 1e9
dp = [INF] * (N+1)

dp[0] = 0 
dp[1] = 1  # 1 = 0+1 1가지 밖에 없음

"""
dp[i] : 현재 i 도달하는데 최소 횟수
dp[i+1] = min(dp[i+1] , dp[i]+1) # 유지 , 업데이트 
dp[i + i//2] = min(dp[i+i//2] , dp[i]+1) 
"""

for i in range(1,N+1):
  if i+1 <= N : 
    dp[i+1] = min(dp[i+1] , dp[i]+1) 
  if i+i//2 <=  N : #순간이동 가능한 경우
    dp[i + i//2] = min(dp[i+i//2] , dp[i]+1)

if dp[N] <= K : 
  print("minigimbob")
else : 
  print("water")