def link(arr, dir, x, y):
    length = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while True:
        x += dx[dir]
        y += dy[dir]

        # 전선이 전원까지 잘 연결되었으면 전선이 이어지는 부분을 표시하고 길이 반환
        if x < 0 or x >= N or y < 0 or y >= N:
            return length

        # 전선이 중간에 다른 전선을 만났으면 이어지지 못하므로 길이 -1 반환
        if arr[x][y] != 0:
            return -1

        arr[x][y] = 2
        length += 1


def dfs(arr, coreNum, count, wire_length):
    global ans, max_cores

    if coreNum == len(core):
        # 현재 연결된 코어 수가 더 많거나 코어 수가 같은데 전선 길이가 더 짧은 경우 답 갱신
        if count > max_cores or (count == max_cores and wire_length < ans):
            max_cores = count
            ans = wire_length
        return

    x, y = core[coreNum]
    if x == 0 or x == N - 1 or y == 0 or y == N - 1:
        # 가장자리에 있는 코어는 전선이 필요 없으므로 바로 다음 코어 탐색
        dfs(arr, coreNum + 1, count + 1, wire_length)
        return

    for dir in range(4):
        arr_copy = [row[:] for row in arr]  # 백트래킹을 위해 복사
        length = link(arr_copy, dir, x, y)
        if length != -1:
            dfs(arr_copy, coreNum + 1, count + 1, wire_length + length)

    # 현재 코어를 연결하지 않고 다음 코어 탐색
    dfs(arr, coreNum + 1, count, wire_length)


testCaseNum = int(input())
outputs = []

for test_case in range(1, testCaseNum + 1):
    N = int(input())
    arr = []
    core = []
    ans = float('inf')
    max_cores = 0

    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            if arr[i][j] == 1:
                core.append((i, j))

    dfs(arr, 0, 0, 0)
    outputs.append(f"#{test_case} {ans}")

for output in outputs:
    print(output)