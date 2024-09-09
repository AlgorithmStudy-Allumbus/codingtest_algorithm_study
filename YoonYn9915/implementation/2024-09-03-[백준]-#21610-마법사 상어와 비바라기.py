'''
비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다. 구름은 칸 전체를 차지한다. 이제 구름에 이동을 M번 명령하려고 한다. i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다. 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 이동을 명령하면 다음이 순서대로 진행된다.

모든 구름이 di 방향으로 si칸 이동한다.
각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
구름이 모두 사라진다.
2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
'''

from collections import deque

def copyWater(arr, cloudLoc):
    global N

    # 대각선 방향의 dx와 dy설정
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    for loc in cloudLoc:
        increment = 0
        locX, locY = loc

        for i in range(4):
            row = locX + dx[i]
            col = locY + dy[i]

            if 0 <= row < N and 0 <= col < N and arr[row][col] > 0:
                increment += 1

        arr[locX][locY] += increment


def moveCloudDropRain(arr, d, s, index, cloudLoc):
    # 8가지 이동 경우의 수 설정 (d는 1부터 시작하므로 0-index로 맞춤)
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    newCloudLoc = deque()

    # 각 구름마다 이동
    for loc in cloudLoc:
        locX, locY = loc

        locX = (locX + dx[d[index] - 1] * s[index]) % N
        locY = (locY + dy[d[index] - 1] * s[index]) % N

        # 새로운 구름 위치 저장
        newCloudLoc.append((locX, locY))

        # 이동한 구름 위치에 비 내림
        arr[locX][locY] += 1

    cloudLoc.clear()
    cloudLoc.extend(newCloudLoc)


# 비 바라기 수행. 비구름을 생성하고 M번만큼 구름을 이동시켜 비를 내린다.
def makeRain(arr, d, s):
    global N, M

    # 구름 위치 초기화
    initialCloudLocation = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
    cloudLoc = deque(initialCloudLocation)

    # 구름이 사라진 위치 저장
    disappearedCloudLoc = set()

    for i in range(M):
        # 구름 이동 & 비내리기 함수
        moveCloudDropRain(arr, d, s, i, cloudLoc)

        # 물 복사 함수
        copyWater(arr, cloudLoc)

        # 구름이 사라진 위치 기록
        disappearedCloudLoc = set(cloudLoc)

        # 새로운 구름 위치를 결정
        newCloudLoc = deque()
        for r in range(N):
            for c in range(N):
                # 2 이상의 물이 있고, 사라진 구름 위치가 아닌 경우에만 구름 생성
                if arr[r][c] >= 2 and (r, c) not in disappearedCloudLoc:
                    newCloudLoc.append((r, c))
                    arr[r][c] -= 2  # 물의 양 2 감소

        cloudLoc = newCloudLoc


N, M = map(int, input().split())
arr = []
d, s = [], []

# 초기 물의 양 저장
for _ in range(N):
    arr.append(list(map(int, input().split())))

# M개의 이동 명령 저장
for _ in range(M):
    temp = input().split()
    d.append(int(temp[0]))
    s.append(int(temp[1]))

# 비 바라기 수행
makeRain(arr, d, s)
total_sum = sum(sum(row) for row in arr)
print(total_sum)
