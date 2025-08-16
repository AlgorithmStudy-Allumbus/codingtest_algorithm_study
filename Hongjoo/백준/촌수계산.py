"""
[BOJ] #2644. 촌수계산 / 실버2

할아버지 - 아빠 - 나
할아버지 - 그외 기타 등등 
- 촌수 = X <-> Y 까지 거리 
"""
import sys
from collections import deque
input = sys.stdin.readline

#1. 입력 변수 
# 인접 리스트 만들기(양방향)

N = int(input())
nodes = [[] for _ in range(N+1)]
tx , ty = map(int, input().split())


M = int(input())
for _ in range(M):
    x,y= map(int,input().split())
    nodes[x].append(y)
    nodes[y].append(x)

# 2.x -> y 의 최단 거리 찾기 : BFS
# 거리 = level 
q = deque([[tx , 0] ])
visited = []
answer = -1
while q : 
    cn , cl = q.popleft()
    if cn == ty : # target 값에 도달할때만 촌수를 answer에 업데이트 하기
        answer = cl 
        break
    for nn in nodes[cn]: # 인접 리스트 찾기 
        if nn not in visited : 
            visited.append(nn)
            q.append([nn ,cl+1] )

# print(visited)
print(answer)
