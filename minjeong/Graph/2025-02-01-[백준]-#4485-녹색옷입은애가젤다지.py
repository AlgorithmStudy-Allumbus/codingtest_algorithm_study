import sys
import heapq

input = sys.stdin.readline

# 오른쪽, 아래, 위, 왼쪽
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 정답 출력을 위한 테스트 케이스 번호 변수
cnt = 0

# 첫 번째 테스트 케이스의 동굴 크기
n = int(input())

while n != 0:
    cnt += 1

    # 동굴의 각 칸에 있는 도둑루피의 크기를 board에 저장
    board = [list(map(int, input().split())) for _ in range(n)]
    heap = []
    dist = [[1e9] * n for _ in range(n)]
    dist[0][0] = board[0][0]

    # 시작점 정보를 (비용, y, x) 형태로 힙에 추가
    heapq.heappush(heap, (board[0][0], 0, 0))

    # 다익스트라 알고리즘
    while heap:
        distance, y, x = heapq.heappop(heap)

        # 최소 비용 우선 탐색이므로, 도착점 [n-1][n-1]에 도착하면 바로 출력
        if y == n - 1 and x == n - 1:
            print(f"Problem {cnt}: {distance}")
            n = int(input())
            break

        # 상하좌우 네 방향에 대해 탐색
        for i in range(4):
            ny = y + dy[i]  # 새로운 y 좌표를 계산
            nx = x + dx[i]  # 새로운 x 좌표를 계산

            # 새로운 좌표가 동굴 내부에 있는지 확인
            if 0 <= ny < n and 0 <= nx < n:
                # 인접한 칸까지 이동했을 때의 누적 비용을 계산
                cost = distance + board[ny][nx]

                # 만약 현재 저장된 비용보다 새로운 비용이 작으면 업데이트
                if dist[ny][nx] > cost:
                    dist[ny][nx] = cost
                    # 새로운 비용과 좌표를 우선순위 큐에 추가
                    heapq.heappush(heap, (cost, ny, nx))
