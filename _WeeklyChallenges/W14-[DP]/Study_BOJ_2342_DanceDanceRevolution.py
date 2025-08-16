'''
BOJ #2342. Dance Dance Revolution (골드3)
https://www.acmicpc.net/problem/2342
유형: Dynamic Programing
'''
import sys 
input = sys.stdin.readline
INF = int(1e9)
commands = list(map(int,input().split()))[:-1]

# 이전 지점에서 현재 지점으로 이동할때 드는 power 값 반환 
def getPower(before_foot , current_foot , preview_power) :
  add_power = 0 
  if before_foot == current_foot : 
    add_power= 1
  elif  before_foot == 0 and current_foot !=0 :
    add_power= 2
  elif abs(before_foot-current_foot)==2 : # 인접 지점 누를 경우
    add_power=4
  else : # 반대편 지점 누를 경우
    add_power= 3
  return preview_power + add_power
    

#1.dp 초기화 (현재 L , R 위치 , 누적 power)
# 3차원 : dp[level][r][l] = 누적 power 
dp = [[[INF for k in range(5)] for i in range(5)] for _ in range(len(commands)+1)]
dp[0][0][0] = 0 

# # #2. 반복문으로 dp  점화식(memorization) 구현
cur_r ,cur_l = 0 ,0
# 각 게임 단계별로 업데이트
for level in range(1,len(commands)+1):
  target = commands[level-1] # 현 단계에서 이동할 자리 
  
  for r in range(5) :
    for l in range(5) :
			# 이전 업데이트 된 r, l 의 경우의 수에 한정(최적화)
      if dp[level-1][r][l] !=INF : 
        cur_p = dp[level-1][r][l]
        # (1) 오른 발만 이동하는 경우
        dp[level][target][l]= min(dp[level][target][l],getPower(r,target,cur_p))
        #(2) 왼 발만 이동하는 경우
        dp[level][r][target]= min(dp[level][r][target],getPower(l,target,cur_p))
      
# 3. 최종 단계에서 최소 힘 출력 
result = INF
for i in range(5):
  for k in range(5):
    result = min(result,  dp[-1][i][k])

print(result)