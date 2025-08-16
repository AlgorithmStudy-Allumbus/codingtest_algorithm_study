"""
[BOJ] 스타트링크/ 실버1

- 총 f 층, 현위치 s 층 , 목적지 G층 
- 이동 방법 (1) 위로 U 층 , (2) 아래로 D 층 
- 출력 : 최소 버튼 횟수 (불가능하면 "use the staris")
- 1 <= s , g <= f <= 10^6
#FLOW : 최단 거리 = BFS
1. 총 0 ~f 층 방문 배열 생성(미방문 조건 -> 최단 거리 확보) 
2. BFS 진행 
    - qeueu : [현 위치하는 층수 ] , 방문 여부 visited[층수] = 버튼 횟수(: -1)
    - 탐색 범위 : 1 <= nn <= f 
"""
import sys
from collections import deque
input = sys.stdin.readline


total_floors , cp , tp , up , down = map(int, input().split())


def bfs(start, end , total_floors, up , down):
    building = [-1 for _ in range(total_floors+1)]
    #1. 시작 위치 start 의 초기화
    q = deque([start])
    building[start] = 0 
    #2. bfs 탐색
    while q :
        cn = q.popleft()
        cbutton = building[cn]
        # pruning 조건 :
        if cn == end : 
            break
        for dh in [up , -down] : # 엘베 2가지 조작 방법 :up , down
            nn = cn + dh 
            # 다음 층이 건물 층수 범위내에 존재함& 미방문=> 방문하기
            if 1 <= nn <= total_floors and building[nn] <0 : 
                q.append(nn)
                building[nn] = cbutton +1 
    return building[end]


answer=bfs(cp , tp , total_floors , up , down)
#3. 출력 형식 지정 
if answer < 0 : 
    print("use the stairs")
else :
    print(answer)
