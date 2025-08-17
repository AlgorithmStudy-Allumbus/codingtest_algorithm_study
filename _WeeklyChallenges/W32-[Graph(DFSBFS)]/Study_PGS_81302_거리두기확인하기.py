"""
PGS #81032. 거리두기 확인하기 (Level 2)
https://school.programmers.co.kr/learn/courses/30/lessons/81302
유형: Brute Force, Graph, BFS
"""

"""
풀이1: 완전 탐색
"""


def solution(places):
    def is_safe(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] != 'P':
                    continue

                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if not (0 <= ni < 5 and 0 <= nj < 5):
                        continue
                    if place[ni][nj] != 'P':
                        continue

                    dist = abs(dx) + abs(dy)
                    if dist == 1:
                        return 0  # 거리 1에서 바로 P면 위반
                    elif dist == 2:
                        # 파티션 여부 확인
                        if dx == 0:  # 수평
                            if place[i][j + dy // 2] != 'X':
                                return 0
                        elif dy == 0:  # 수직
                            if place[i + dx // 2][j] != 'X':
                                return 0
                        else:  # 대각선
                            if place[i][nj] != 'X' or place[ni][j] != 'X':
                                return 0
        return 1

    dirs = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # 거리 1
        (-2, 0), (2, 0), (0, -2), (0, 2),  # 일직선 거리 2
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # 대각선 거리 2
    ]

    answer = []
    for place in places:
        answer.append(is_safe(place))

    return answer


"""
풀이2: BFS
"""
from collections import deque


def bfs(p):
    start = []

    for i in range(5):  # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0] * 5 for i in range(5)]  # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:

                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer
