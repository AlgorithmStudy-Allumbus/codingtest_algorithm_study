"""
시작 1 ~ N번 node , road : m 개 (cost=1)
최단거리= k인
-> 다익스트라? ....BFS 감사합니다 ㅎ
<BFS>
0. 인접 리스트 graph 정의 , 시작 노드 queue 넣기 & 방문 등록
1.queue 가 빌때 까지 
    queue에서 꺼낸 n 과 인접한 노드 중 방문 안한 노드
        -> queue 넣고 방문 등록
    없으면 : 
        -> queue에서 빼기

=> cost = level : start ~ 거리 
"""
import sys
from collections import deque

n, m, k, start = map(int, sys.stdin.readline().split())
#0.graph 정의
INF = 300001
graph = [[] for _ in range(n+1)]
cost= [INF]*(n+1) # 최단 거리 graph
visited=[False]*(n+1)
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# print(graph)
#2 BFS 
queue = deque([start])
visited[start] = True
cost[start] = 0
answer =list()

while queue :
    now = queue.popleft()
 
    for n in graph[now] :  
  
        if not visited[n]  :
            queue.append(n)
            visited[n] = True
            cost[n] = cost[now] + 1
            if cost[n] == k : 
                answer.append(n)
# 출력
if len(answer)== 0 :
    print(-1)
else :
    answer.sort()
    for a in answer:
        print(a)

