from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split()))  # 내구도. A1, A2, ..., A2N
robot = deque([0] * n)  # 벨트위에 있는 로봇
result = 0

while True:
    result += 1
    # 1. 벨트 회전한다.
    a.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0    # 내리는 위치에 도달한 경우, 즉시 내림
    # 2. 로봇 이동하기. 이동하려는 칸에 로봇 x, 내구도 1이상 남아야함.
    for i in range(n - 2, -1, -1):  # 먼저 올라간 로봇부터 진행
        if a[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            a[i + 1] -= 1
    robot[-1] = 0  # 내리는 위치에 도달한 경우, 즉시 내림
    # 3. 올리는 위치에 내구도 0 아니면 로봇 올리기 & 내구도 감소
    if a[0] != 0 and robot[0] != 1:
        robot[0] = 1
        a[0] -= 1
    # 4. 내구도 0인 칸 수가 k이상이면 종료
    if a.count(0) >= k:
        break
print(result)