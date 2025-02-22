import sys
input = sys.stdin.readline
import heapq

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(N, cave):
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    
    # 우선순위 큐 (손실 루피, x, y)
    pq = []
    heapq.heappush(pq, (cave[0][0], 0, 0))
    dist[0][0] = cave[0][0]

    while pq:
        rupee, x, y = heapq.heappop(pq)

        # 목적지 도착 시 종료
        if x == N - 1 and y == N - 1:
            return rupee
        # 현재 저장된 최소 비용보다 크면 무시
        if rupee > dist[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                new_cost = rupee + cave[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

case_num = 1

while True:
    N = int(input().strip())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra(N, cave)
    print(f"Problem {case_num}: {result}")
    case_num += 1  
