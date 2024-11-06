import sys
from collections import deque

input = sys.stdin.readline

# 1. 나이트가 이동할 수 있는 8가지 방향을 정의
directions = [(0, 0), (-1, -2), (1, -2), (-2, -1), (2, -1), (-1, 2), (1, 2), (-2, 1), (2, 1)]


# 5. BFS 탐색 함수 정의
def bfs(start_x, start_y):
    # 시작 노드를 큐에 추가하고 해당 위치의 값을 0으로 설정
    queue = deque([(start_x, start_y)])
    chess_map[start_x][start_y] = 0

    # 큐가 빌 때까지 탐색
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 모든 방향으로 이동 시도
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 5.2.1 체스판의 범위를 넘어가지 않는지 확인
            if 0 <= nx < l and 0 <= ny < l:
                # 아직 방문하지 않은 위치라면
                if chess_map[nx][ny] == -1:
                    # 현재 위치에서 1 이동한 값으로 갱신하고 큐에 추가
                    chess_map[nx][ny] = chess_map[x][y] + 1
                    queue.append((nx, ny))

                # 5.2.2. 목표 지점에 도달한 경우, 이동 횟수 반환
                if nx == fin_x and ny == fin_y:
                    return chess_map[nx][ny]

    return -1  # 목표 지점에 도달하지 못한 경우


# 2. 테스트 케이스 개수 입력
t = int(input())
for _ in range(t):
    # 3. 체스판의 크기, 시작 위치, 목표 위치 입력
    l = int(input())  # 체스판의 한 변의 길이 l
    cur_x, cur_y = map(int, input().split())  # 시작 위치
    fin_x, fin_y = map(int, input().split())  # 목표 위치

    # 4. 체스판 초기화 (-1로 초기화하여 미방문 표시)
    chess_map = [[-1] * l for _ in range(l)]

    # 6. BFS 탐색을 통해 결과 출력
    print(bfs(cur_x, cur_y))