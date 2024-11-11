import sys
from collections import deque
input = sys.stdin.readline

# 이차원 배열의 행과 열 개수 입력
n, m = map(int, input().split())

# 빙산 높이 정보를 저장할 2차원 배열 생성
iceberg = [list(map(int, input().split())) for _ in range(n)]

# 빙산 높이 감소를 계산하는 함수
def get_iceberg_height(iceberg):
    # 감소된 빙산 높이를 저장할 새로운 배열 초기화
    new_height = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:  # 빙산이 있는 칸만 처리
                water_count = 0  # 인접한 바다 칸 개수 초기화

                # 상하좌우 네 방향 탐색
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and iceberg[ni][nj] == 0:
                        water_count += 1

                # 바다에 접한 개수만큼 빙산 높이를 감소시키며 최소 0으로 유지
                new_height[i][j] = max(iceberg[i][j] - water_count, 0)
    return new_height

# BFS를 통해 빙산 덩어리 수를 계산하는 함수
def count_icebergs(iceberg):
    visited = [[False] * m for _ in range(n)]  # 방문 여부를 기록할 배열 초기화
    iceberg_count = 0  # 빙산 덩어리 수 초기화

    for i in range(n):
        for j in range(m):
            # 빙산이 있고 아직 방문하지 않은 경우 새로운 덩어리로 간주
            if iceberg[i][j] > 0 and not visited[i][j]:
                iceberg_count += 1
                # BFS로 연결된 빙산을 모두 방문 처리
                queue = deque([(i, j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        # 빙산이 연결된 인접 노드를 방문 처리
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and iceberg[nx][ny] > 0:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    return iceberg_count

# 연도(시간) 초기화
year = 0

# 빙산이 분리될 때까지 반복
while True:
    year += 1

    # 빙산 높이 감소 계산 및 업데이트
    iceberg = get_iceberg_height(iceberg)

    # 현재 빙산 덩어리 수 계산
    mountain = count_icebergs(iceberg)

    # 빙산 덩어리가 2개 이상으로 분리된 경우
    if mountain >= 2:
        print(year)
        exit(0)

    # 빙산이 모두 녹아 덩어리가 없는 경우
    if mountain == 0:
        print(0)
        exit(0)