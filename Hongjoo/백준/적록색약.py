"""
https://www.acmicpc.net/problem/10026


- NXN (<= 1000) , R,G,B  
- 상하좌우로 겹쳐진 "구역" = 1개 
- 적록 색약 R = G , B


=(1) 정상 
R + G + B 
(2) 색약
max(R,G) + B
# 유형 : DFS 

# flow 


1.(0,0) 부터 DFS 수행 + 방문(visited) 등록 : 1 X N*N
2. 방문 리스트 : iT False not in visited , 까지 반복
"""


import sys
# 1. 입력 받기 
n = int(input())
field = [ [] for _ in range(n) ]
colors_g = [[] , [] , []]
for i in range(n):
    tmp = sys.stdin.readline().split()
    # print(f"tmp {tmp}")
    for t in range(len(tmp[0])) : 
        field[i].append(tmp[0][t])
        if tmp[0][t] == "R" : 
            colors_g[0].append([i,t])
        elif  tmp[0][t] == "G":
            colors_g[1].append([i,t])
        else :
            colors_g[2].append([i,t])
# print(f"colors-G {colors_g}")

# 2. DFS 
dx = [0,0,-1,1]
dy = [-1,1,0,0,]
def dfs(start_y,start_x, visited, flag , colors ):
    r , g, b= colors
    if field[start_y][start_x] == "R":
        r+=1
    elif field[start_y][start_x] == "G":
        g+=1 
    else : 
        b+=1
    queue = list()
    queue.append([start_y,start_x])
    visited.append([start_y,start_x])
    while queue :
        cur_y , cur_x= queue.pop()
        for i in range(4):
            next_y ,next_x = cur_y + dy[i] , cur_x + dx[i]
            if next_y>= n or next_y < 0 or next_x>= n or next_x < 0:
                print("####")
                continue 
            
            if flag : #적록색약 경우
                if field[cur_y][cur_x] in ["R","G"] and  field[next_y][next_x] in ["R","G"] and [next_y,next_x] not in visited :
                    queue.append([next_y,next_x])
                    visited.append([next_y,next_x]) 
                    continue
            if field[cur_y][cur_x] == field[next_y][next_x] and [next_y,next_x] not in visited : #색상이 같은 경우만 진행 
                queue.append([next_y, next_x])
                visited.append([next_y, next_x]) 
                print(f"visited : {visited}")
    return [r,g,b] ,visited


# 1. 정상
# visited= [ [False for _ in  range(n)] for k in range(n)]

colors = [ 0, 0, 0]
for c in range(3) :
    category_colors = colors_g[c]
    visited = []
    while len(visited) <= len(category_colors): # R 
        for y,x in category_colors : 
            if [y,x] not in visited  :
                colors , visited = dfs(y, x, visited , False , colors)
                print(f"i {colors}")

print(sum(colors))
# visited = []
# colors = [ 0, 0, 0]
# for c in range(3) :
#     category_colors = colors_g[c]
#     while len(visited) <= len(category_colors ): # R 
#         for y,x in category_colors : 
#             if [y,x] not in visited  :
#                 colors , visited = dfs(y, x, visited , True,colors)
# print(sum(colors))
    
    
                
       






