"""
20.19
https://www.acmicpc.net/problem/11559
BOJ.#11559_Gold4

#problem
- goal) 연쇄 "연속" 횟수 구하기
[condition]
- 1연쇄 : 해당 turn 에서 상하좌우 4개 연결 -> 삭제 
- 삭제 후 위에 있는 element 는 하강 

- 입력: 현 filed 상황(12x6)
   - (빈공간) / R, G, B, P, Y
   - 빈공간 : 0 
   - 색상 : R,G, B, P, Y = 1,2,3,4,5
[flow] # BFS
1. 상하좌우 연쇄 확인
- 연쇄 확인 
- 삭제
- 연쇄 횟수 증가

"""
import sys
from collections import deque
input = sys.stdin.readline
#1. field 현황 리스트에 담기
field = [list(input())[:-1] for _ in range(12)]

#2. bfs
dy = [-1,1,0,0]
dx =[0,0,-1,1]


def refine_field(x) : # 중간 빈자리
  stack = deque()
  #1.아레=> 위로 스택에 뿌요뿌요 순서대로 축척하기 
  for ny in range(11, -1,-1):
    if field[ny][x] != ".":
      stack.append(field[ny][x])
  for ny in range(11, -1, -1) :
    if stack : 
       field[ny][x] = stack.popleft()
    else :
      field[ny][x] = "."

# 연쇄 확인 및 터짐
def bfs(sy,sx):
  q = deque()
  q.append([sy,sx])
  pop_positions = [[sy,sx]]
  cur_color = field[sy][sx]
  visited.append([sy,sx])
  while q : 
    cy,cx = q.popleft()
    for d in range(4):
      ny ,nx = cy + dy[d] ,cx + dx[d]
      # 같은 색상 -> 삭제 등록하기
      if 0<= ny<12 and 0<= nx < 6 and [ny,nx] not in visited  and field[ny][nx] == cur_color :
        q.append([ny,nx])
        pop_positions.append([ny,nx])
        visited.append([ny,nx])
  
  #2) 터짐 확인
  if len(pop_positions) >= 4 :
    for y,x in pop_positions : 
      field[y][x] = "."
    return True
  return False# 안 터짐

answer = 0 
flag = True
k = 0 
while flag  :
  visited = []
  flag =False
  #1. 전체 field에서 뿌요뿌요 탐색
  for i in range(12):
    for j in range(6):
      if field[i][j]!="." and [i,j] not in visited:
        now_f = bfs(i,j) # 2.해당 위치에서 터짐 여부 확인
        flag = flag or now_f
  #2. 연쇄 계수 추가
  if not flag : # False - 안터짐
    break
  else :
    for row in range(6):
        refine_field(row)
  # 현재 turn 에서 1번 이상 터짐
  answer += 1
print(answer)