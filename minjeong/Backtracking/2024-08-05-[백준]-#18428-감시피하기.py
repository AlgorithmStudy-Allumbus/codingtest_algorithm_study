import sys
input = sys.stdin.readline

# 감시 영역을 확인하는 함수
def is_safe(n, hallway, teachers):
    # 선생님 위치로부터 상하좌우 방향을 장애물/벽을 만날 때까지 계속 이동해보면서 학생 존재 여부 탐색
    for x, y in teachers: # (0, 4), (1, 0), (3, 1), (4, 2)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x, y
            while 0 <= nx < n and 0 <= ny < n:
                if hallway[nx][ny] == 'O': # 장애물 만나면 즉시 종료
                    break
                if hallway[nx][ny] == 'S': # 학생이 있으면 감시됨
                    return False
                # 한 쪽 방향으로 장애물 또는 벽을 만날 때까지 계속 이동
                nx += dx
                ny += dy
    # 학생이 없다면 True 반환
    return True

def set_obstacles(count):
    if count == 3:  # 장애물 3개가 설치되면 감시가 안전한지 확인
        return is_safe(n, hallway, teachers)

    for i in range(n):
        for j in range(n):
            if hallway[i][j] == 'X':
                hallway[i][j] = 'O'
                if set_obstacles(count + 1):
                    return True
                hallway[i][j] = 'X'

    return False

n = int(input())    # 복도 크기
hallway = []        # 복도 정보
teachers = []        # 선생님 위치 리스트

for i in range(n):
    row = list(map(str, input().split()))
    hallway.append(row)
    for j in range(n):
        if hallway[i][j] == 'T':
            teachers.append((i, j))

if set_obstacles(0):
    print("YES")
else:
    print("NO")