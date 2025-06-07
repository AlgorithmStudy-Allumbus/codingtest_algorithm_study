
import sys
from collections import deque
INF = 1e9
# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

dl= [[-1,1],[1,1],[1,-1],[-1,-1]] # 우상 . 우하 / 좌하 / 좌상
dl_combined = [0,3,1,2,2,3,0,1]
sy ,sx= map(int,sys.stdin.readline().split())
ty,tx = map(int, sys.stdin.readline().split())

field = [[INF]*9 for _ in range(10)]
field[sy][sx] = 0 
field[ty][tx] = -1

q = deque()
q.append([sy,sx])

def check_bound(y,x) :
  if 0<= y <=9 and 0<= x <=8 and field[y][x]!=-1 : # 기물 x , field 안에 , 방문 상관x => 왕 위치만 안됨x
    return True
  return False
def check_bound2(y,x) :
  if 0<= y <=9 and 0<= x <=8 : # 기물 가능
    return True
  return False

while q : 
  cy,cx = q.popleft()
  for i in range(8):
    ny1, nx1 = cy +dy[i//2] , cx+dx[i//2]
    ny2, nx2 = ny1 + dl[dl_combined[i]][0] , nx1 + dl[dl_combined[i]][1] 
    ny3 , nx3 = ny2 + dl[dl_combined[i]][0] , nx2 + dl[dl_combined[i]][1]
    
    if check_bound(ny1, nx1) and check_bound(ny2, nx2) and check_bound2(ny3, nx3) : 
      if ny3 == ty and nx3 == tx : 
        # print(f"succes====")
        print(field[cy][cx] +1)
        
        exit()
      elif field[cy][cx] +1 <= field[ny3][nx3] : 
        field[ny3][nx3] =field[cy][cx] +1 # 업데이트 
        # print(f"{cy}{cx} -> {i}: {ny1}{nx1} / {ny2}{nx2} / {ny3}, {nx3} => field{field[ny3][nx3]} ")
       
        q.append([ny3,nx3])
        # print(f"{cy}{cx} -> {i}: {ny1}{nx2} / {ny2}{nx2} / {ny3}, {nx3} => field{field[ny3][nx3]} ")
  
print(field[ty][tx])