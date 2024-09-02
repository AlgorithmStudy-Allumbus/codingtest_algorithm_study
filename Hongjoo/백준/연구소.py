

"""

(1) 벽 3개 - 세우기 ->  0중 3 개 조합 구하기
(2) BFS -> 확산시키기 
(3) 안전 영역 계산하기  -> min 이란 비교시 업데이트 
(4) 조합 replay

#bfs 
visited = [False] * 9
def bfs(graph, start, visited):
# start -> queue, visited 
    queue = deque([start])
    visited[start] = True
    while queue : 
        node= queue.popleft()
        for i in  graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


"""
from itertools import combinations
from collections import deque
import sys
import copy

a,b= map(int, sys.stdin.readline().split()) # row, columns

m = []
zero_p = []
virus_p = []
for i in range(a):
    tmp = list(map(int, input().split()))
    for j  in range(b) :
        if tmp[j] == 0:
            zero_p.append([i,j])
        elif tmp[j] == 2 :
            virus_p.append([i,j])
    m.append(tmp)
# print(m)
#1. zero_p 중 3개 조합 구하기 -> combi
combi = list(combinations(zero_p , 3))

#2. BFS
max_safe= 0
for walls in combi:
    graph=copy.deepcopy(m)
    # 벽설치
    for w_x, w_y in walls : 
        graph[w_x][w_y]  = 1 
    
    new_v_count =0
    # virus 들위 위치 = BFS start 위치
    for v in range(len(virus_p)) :
        start=virus_p[v] # start = [x,y]
        queue = deque([start])
        #bfs
        while queue :
            node = queue.popleft()
            # print("#",node, end ="")
            # 인근 node - 상/하/좌/우
            near_node = [[node[0]+1,node[1]] ,
                          [node[0]-1,node[1]],
                           [node[0],node[1]+1],
                            [node[0],node[1]-1] ]
            
            for nn in near_node : 
                x,y = nn
                # out of range 
                if x < 0 or  x >= a or y <0 or y>=b :
                    # print("bump!")
                    continue
                # print(x,y)
                if graph[x][y] == 0 : #방문 x 
                    queue.append(nn)
                    graph[x][y] = 2 # 방문 완료
                    new_v_count+= 1
    
        
    #(3) 안전 영역 계산하기  -> min 이란 비교시 업데이트
    safe_area = len(zero_p)-3 -new_v_count
    if max_safe < safe_area :
        max_safe = safe_area
print(f"{max_safe}")


