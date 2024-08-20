import sys
from collections import deque

#1. 입력값 받기
#2. 모든 배열을 돌며 인구이동 조건을 만족하는 나라가 있는지 확인. (1. 인접한 나라 2. 두 국가의 인구 차의 절댓값이 l이상 r이하)
#3. 인구 이동조건을 만족하는 나라가 있으면 bfs로 그래프를 탐색하면서 나라의 개수와 인구의 총합을 구해서 새로운 인구를 구해준다.
#4. visited 배열은 인구 이동날마다 초기화 해야 한다.

# 실제로 인구를 이동시키는 함수
def movePopulation(i, j):
    global n, l, r
    global visited, arr

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(i, j)])
    visited[i][j] = 1
    queue2 = deque([(i, j)])
    populationSum = arr[i][j]
    countrySum = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4): 
            row = x + dx[d]
            col = y + dy[d]

            if 0 <= row < n and 0 <= col < n and visited[row][col] == 0 and l <= abs(arr[x][y] - arr[row][col]) <= r:
                visited[row][col] = 1
                countrySum += 1
                populationSum += arr[row][col]
                queue.append((row, col))
                queue2.append((row, col))

    newPopulation = populationSum // countrySum

    while queue2:
        x, y = queue2.popleft()
        arr[x][y] = newPopulation

# 인구 이동 조건을 만족하는 나라가 있는지 확인하는 함수
def checkCountries():
    global ans

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            for k in range(4):
                row = i + dx[k]
                col = j + dy[k]
                if 0 <= row < n and 0 <= col < n and l <= abs(arr[i][j] - arr[row][col]) <= r:
                    ans += 1
                    return True

    return False


inp = sys.stdin.readline

n, l, r = map(int, inp().split())

arr = []
visited = [[0] * n for _ in range(n)]

ans = 0

for i in range(n):
    arr.append(list(map(int, inp().split())))

while checkCountries():
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                movePopulation(i, j)
    visited = [[0] * n for _ in range(n)]

print(ans)
