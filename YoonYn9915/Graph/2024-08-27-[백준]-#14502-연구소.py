from collections import deque
import sys
import copy

# 1. 입력값 받기
# 2. 임의로 벽 3개 세우기 (backtracking 사용)
# 3. bfs로 그래프 탐색하며 바이러스가 있는곳(처음에 2인 영역)부터 시작해서 바이러스 확산시키기
# 4. 바이러스 확산 후 안전영역(0인 영역)을 세고 최대값이면 저장


def bfs():
    global arr, virusLocation,N,M, maxSafeAreaCount

    copyArr = copy.deepcopy(arr)

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    queue = deque(virusLocation)

    while queue:
        startRow,startCol = queue.popleft()
        for i in range(4):
            row = startRow + dx[i]
            col = startCol + dy[i]

            if 0<=row<N and 0<=col<M and copyArr[row][col] == 0:
                #바이러스 확산
                copyArr[row][col] = 2
                #방문처리
                queue.append((row,col))

    #안전영역 세기
    safeAreaCount = 0
    for i in range(N):
        for j in range(M):
            if copyArr[i][j] == 0:
                safeAreaCount += 1

    #안전영역의 최댓값 비교
    maxSafeAreaCount = max(maxSafeAreaCount, safeAreaCount)


def makeWall(arr, numOfWall):

    # 세운 벽의 개수가 3개면 바이러스 확산시키기
    if numOfWall == 3:
        bfs()
        return

    # 벽의 개수가 3이 아니면 하나씩 세우기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                makeWall(arr, numOfWall + 1)
                # 3개가 돼서 bfs가 끝나면 원복해주기
                arr[i][j] = 0


#입력값 받기
inp = sys.stdin.readline

N,M = map(int, inp().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, inp().split())))

#바이러스 위치 찾기
virusLocation = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virusLocation.append((i,j))

maxSafeAreaCount = 0

makeWall(arr, 0)
print(maxSafeAreaCount)