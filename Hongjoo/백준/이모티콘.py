"""
https://www.acmicpc.net/problem/14226
# 이모티콘 / 골드 4
# goal ) 화면에 S개 이모티콘 만드는데 드는 최소시간 구하기
- 3가지 작업(1sec)로 화면 1개 -> S 개
(1) 화면 속 모든 이모티콘  -> 클립보드에 "복사" <덮어쓰기 - ctrl+c> 
(2) 클립보드 속 모든 이모티콘 -> 화면에  "붙여넣기" <추가- ctrl+v>
- 클립보드가 반드시 비어있지 않아야 붙여 넣기 가능
- 클립 보드 속 이모티콘은 일부만 삭제 , 복사 불가
- 붙여넣기 시, 클립보드에 있는 이모티콘 개수가 화면에 추가됨
(3) 화면 속 이모티콘 1개 삭제 <삭제 - delete>
# FLOW : BFS
i. 
field = [screen : 화면 속 이모티콘 개수 , Backup: 클립보드 속 이모티콘 개수]
ii. 3가지 작업 
[copy]
- Bacup[i] = Screen[i-1] 개수
[put]
if backup[i-1] !=0
- screen[i] = backup[i-1] + screen[i-1]
[delete]
- screen[i] = screen[i-1]
"""
import sys
from collections import deque
input = sys.stdin.readline

S = int(input())
visited = [[False]*1002 for _ in range(1002)]
visited[1][0] = True# visited [screen 개수][클립보드 개수] 조합 시 방문 여부 T/F

q = deque([[1,0,0]]) # screen 개수
# 3가지 각 종류의 작업 이후 화면 속 & 클립보드 속 이모티콘 개수 
def function(num , screen , backup ):
    if num == 0 : # copy
        return screen , screen
    elif num == 1  : # put
        return screen + backup , backup 
    elif num == 2: # delete
        return screen -1 , backup 
# 2. BFS 작업
while q: 
    cs , cb , ct =q.popleft()
    # 목표 달성시-> 끝내기
    if cs == S : 
        break
    if cb == 0 : 
        next_f = [0,2]
    else :
        next_f = [0,1,2]

    for d in next_f : 
        ns , nb = function(d , cs , cb )
        nt = ct+1
        #BFS 화면 적합성
        if 1<= ns <=1001 and not visited[ns][nb] : 
            q.append([ns, nb , nt])
            visited[ns][nb] = True

print(ct)