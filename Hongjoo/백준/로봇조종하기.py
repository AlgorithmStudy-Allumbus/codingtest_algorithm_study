"""
https://www.acmicpc.net/problem/1520
"""

import sys
input = sys.stdin.readline
#0. 맵 (N,M) 칸 별 탐사 가치 설정
N , M = map(int,input().split()) # y,x 
fields =list()
for n in range(N) :
  fields.append(list(map(int, input().split())))

# print(fields)
# 2. dp 테이블 초기화 
dp = [[0 for _ in range(M)] for k in range(N)]
left2right = [[0 for _ in range(M)] for k in range(N)]
right2left = [[0 for _ in range(M)] for k in range(N)]
#3.탐색 가능  (1)left2 right <-/ (2) right2left <- 

 # n == 0 경우 : (1) left2right 경로만 존재(누적값)
for m in range(M) :
  dp[0][m] = dp[0][m-1] + fields[0][m] 
# 2번쨰 행 부터 진행 
for n in range(1, N) : 
  #m==0인 경우 초기화 : top-dowm의 경로만 존재
  left2right[n][0] = dp[n-1][0] + fields[n][0]
  right2left[n][M-1] = dp[n-1][M-1] + fields[n][M-1]
  # 1. 왼쪽 -> 오른쪽 방향으로 탐색 진행 
  for m in range(1,M) :
    # (1)left2right , top-down  방향 탐색 누적 값 구하기 
    left2right[n][m] = max(dp[n-1][m], left2right[n][m-1])+ fields[n][m]
    
  #2. 오른쪽 -> 왼쪽 방향으로 탐색 진행 
  for m in range(M-2 , -1 , -1)  : 
    # (2) right2left , top-down 방향 누적값 구하기
    right2left[n][m] = max(dp[n-1][m], right2left[n][m+1])+ fields[n][m]
  #3. 열 m 탐색 완료시 , 최종 dp 값 계산하기
  for m in range(M):
    dp[n][m] = max(left2right[n][m] , right2left[n][m])

print(dp[-1][-1])
