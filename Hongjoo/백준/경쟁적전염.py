"""
1. bfs
    - queue
    - 인접 node
        (x,y) = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
2. sorting
    낮은 번호부터
"""
from collections import deque
n, k = map(int, input().split())
graph=[[] for _ in range(n)]
for i in range(n):
    graph[i]=list(map(int,input().split()))
s,x,y = map(int, input().split())
print(graph)
# 1.번호 순대로 초기 바이러스 정보 정렬
virus_info = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_info.append([graph[i][j],0,[i,j]]) # [번호,시간,위치] 
#2.dfs
# virus_info == queue
virus_info.sort()
print(virus_info)
t=0
while t < s : 
    virus_info.sort()
    for node in virus_info:
        print("t",t ,"=",virus_info)
        queue = deque([node])
        now = queue.popleft()
        num , t , position = now
        near_nodes= [[position[0],position[1]+1],
                        [position[0],position[1]-1],
                        [position[0]-1,position[1]],
                        [position[0]+1,position[1]]
                        ] # 상하좌우
        
        t+=1
        if t > s :
            break
        for v in near_nodes: # v = [x,y]
            if n> v[0] and v[0]>= 0 and n> v[1] and v[1]>= 0 :
                if graph[v[0]][v[1]] == 0 :
                    virus_info.append([num,t,v]) # 번호, 시간, 위치
                    graph[v[0]][v[1]] = num
        print(f"graph node = {node}, => {graph}")           
                    # print(f"graph {v[0]},{v[1]}:{graph[v[0]][v[1]]}")
            # print(f"num, t, position {num} , {t} , {position}")
        
# print("#",virus_info)
# print("##",graph)
# print("###", graph[x][y])
print(graph[x-1][y-1])