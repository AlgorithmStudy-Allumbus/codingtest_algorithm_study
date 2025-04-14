'''
BOJ #4963. 섬의 개수 (실버2)
https://www.acmicpc.net/problem/4963
유형: BFS/DFS
'''

import sys
input = sys.stdin.readline
from collections import deque

# 8방향 (상, 하, 좌, 우, 대각선 4개)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y, graph, w, h):
    queue = deque([(x, y)])
    graph[y][x] = 0  # 방문 처리 (1 → 0 변경)

    while queue: # 큐가 빌 때까지 반복
        cx, cy = queue.popleft() # 현재 좌표 꺼내기 
        for i in range(8):  # 8방향 탐색
            nx, ny = cx + dx[i], cy + dy[i] # 새로운 좌표 계산
            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
                graph[ny][nx] = 0  # 방문 처리
                queue.append((nx, ny)) # 큐에 추가 (다음에 탐색할 곳)
 
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break  # 종료 조건
    island = [list(map(int, input().split())) for _ in range(h)]

    count = 0 # 섬의 개수 
    for y in range(h):
        for x in range(w):
            if island[y][x] == 1:  # 새로운 섬 발견
                count += 1
                bfs(x, y, island, w, h) # BFS 실행
    
    print(count)
