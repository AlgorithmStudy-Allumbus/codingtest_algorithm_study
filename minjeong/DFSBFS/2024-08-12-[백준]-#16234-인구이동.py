import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    union = [(x, y)] # 연합에 포함된 나라들을 저장할 리스트
    visited[x][y] = 1 # 현재 나라를 방문 표시
    total_population = nation[x][y] # 연합의 총 인구 수

    while queue:
        x, y = queue.popleft() # 큐에서 하나의 나라를 꺼냄
        for nx, ny in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 인접한 네 방향 확인
            dx, dy = x + nx, y + ny
            # 범위 내에 있고, 아직 방문하지 않은 곳이라면
            if (0 <= dx < N and 0 <= dy < N) and visited[dx][dy] == 0:
                # 두 나라의 인구의 차이가 L이상 R이하라면(=연합이 된다면)
                if L <= abs(nation[dx][dy] - nation[x][y]) <= R:
                    visited[dx][dy] = 1     # 방문 표시
                    queue.append((dx, dy))  # 큐에 추가
                    union.append((dx, dy))  # 연합에 추가
                    total_population += nation[dx][dy] # 연합 인구 추가

    # 연합이 2개 이상의 나라로 이루어졌을 경우
    if len(union) > 1:
        new_population = total_population // len(union) # 새로운 인구 수 계산
        for i, j in union:
            nation[i][j] = new_population # 연합 내의 모든 나라에 인구 재배치
        return True  # 인구 이동이 일어났음

    return False # 인구 이동이 일어나지 않음

N, L, R = map(int, input().split())
nation = [list(map(int, input().split())) for _ in range(N)]
day = 0 # 인구이동 발생 일수

while True:
    visited = [[0] * N for _ in range(N)]
    is_moved = False # 인구 이동이 발생했는지 여부를 저장할 변수

    # 모든 나라를 탐색하며 연합 형성, 인구 이동 확인
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:   # 방문하지 않은 나라에서 BFS 시작
                visited[i][j] = 1   # 방문 표시
                if bfs(i, j):       # 한 번이라도 인구 이동이 발생했다면
                    is_moved = True # 인구 이동이 발생했음을 표시

    if not is_moved: # 인구 이동이 발생하지 않았다면 종료
        break

    day += 1 # 인구 이동이 발생한 날 수 증가

print(day)