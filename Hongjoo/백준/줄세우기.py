import sys
from collections import deque

def topology_sort() :
    result = []
    q = deque()

    # 1. indegree= 0인 노드를 큐에 삽입
    for i in range(1,n+1) : 
        if indegree[i] == 0:
            q.append(i)
    
    # 2. 큐가 빌 때 까진 반복
    while q : 
        # 2-1 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now) # resut == queue 꺼내는 순서
        # 2-2 해당 노드와 연결된 노드 (outdegree)들의 진입 차수에서 1 빼기
        for j in graph[now] :
            indegree[j] -=1
            #2-3. 새롭게 indegree=0 인 노드를 큐에 삽입
            if indegree[j] == 0 :
                q.append(j)
    
    # 3.위상정렬을 수행한 결과 출력
    for i in result :
        print(i,end = " ")

n, m = map(int, sys.stdin.readline().split())
#graph 만들기
indegree = [0] * (n+1) # indegree list
graph = [[] for _ in range(n+1)]
for i in range(m): 
    a,b = map(int , sys.stdin.readline().split())# a앞  -> b뒤 
    graph[a].append(b) 
    indegree[b] += 1 


topology_sort()