from collections import deque
import sys 
input = sys.stdin.readline

def bfs(start, K):
    queue = deque()
    queue.append(start)
    visited[start] = 0 # 시작 위치까지의 시간은 0으로 초기화
    
    while queue:
        node = queue.popleft()
        if node == K: # 동생의 위치에 도달했을 때 
            print(visited[node])
            return
        
        # 동생의 위치에 도달할 때까지, 3가지 이동 경우를 탐색 
        for next in (node-1, node+1, node*2):
           if (0 <= next < 100001) and not visited[next]:
               visited[next] = visited[node] + 1 # 이동시간을 1초 증가시킨다. 
               queue.append(next)

N, K = map(int, input().split())
visited = [-1] * 100001
bfs(N, K)