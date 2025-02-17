import sys 
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)] # NxN 격자 

# 방향: 좌 -> 하 -> 우 -> 상 
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 모래 이동 비율 (왼쪽으로 이동할 때 기준)
sand_ratio = [
    (-1, 1, 0.01), (1, 1, 0.01),
    (-1, 0, 0.07), (1, 0, 0.07),
    (-2, 0, 0.02), (2, 0, 0.02),
    (-1, -1, 0.10), (1, -1, 0.10),
    (0, -2, 0.05),
    (0, -1, 'alpha') # a: 남은 모래를 놓을 위치 
]

out_sand = 0 # 격자 밖으로 나간 모래의 양

# 주어진 방향에 따라 (dx, dy)를 회전
def rotate_dir(dx, dy, dir):
    for _ in range(dir):
        dx, dy = dy, -dx # 90도 회전
    return dx, dy

# 모래를 현재 위치 (x,y)에서 dir 방향으로 퍼뜨림 
def spread_sand(x, y, dir):
    global out_sand
    total_sand = A[x][y] # 현재 위치의 모래 양 
    spread_sum = 0 # 흩날린 모래 총합
    A[x][y] = 0 # 현재 위치 모래를 먼저 없애줌 
    
    for dx, dy, ratio in sand_ratio:
        if ratio == 'alpha': # a 위치일 때 처리 
            continue
        # 현재 방향(dir)에 맞게 회전 적용 
        nx, ny = rotate_dir(dx, dy, dir) # 회전 적용
        nx, ny = x + dx, y + dy # 이동 좌표 계산 
        sand = int(total_sand * ratio) # 소수점 버림 
        
        if 0 <= nx < N and 0 <= ny < N:
            A[nx][ny] += sand # 격자 내에 있으면 더하기
        else:
            out_sand += sand # 격자 밖이면 밖으로 나간 모래에 추가 
        
        spread_sum += sand # 흩날린 모래 총합 증가 
    
    # 남은 모래를 a 위치에 배치 
    dx, dy = rotate_dir(sand_ratio[-1][0], sand_ratio[-1][1], dir) 
    alpha_x, alpha_y = x + dx, y + dy
    remaining_sand = total_sand - spread_sum # 남은 모래 계산 
    
    if 0 <= alpha_x < N and 0 <= alpha_y < N:
        A[alpha_x][alpha_y] += remaining_sand 
    else: 
        out_sand += remaining_sand # 격자 밖이면 밖으로 나간 모래에 추가 
     
     
x, y = N // 2, N // 2 # 시작위치 (중앙)
steps = 1 # 이동거리 
dir = 0 # 방향 인덱스 (0:좌, 1:하, 2:우, 3:상)

while (x, y) != (0, 0): # (1,1)까지 이동
    for _ in range(2): # 같은 step 크기로 두 번 이동 (좌->하, 우->상)
        for _ in range(steps):
            x += directions[dir][0]
            y += directions[dir][1]
            
            spread_sand(x, y, dir) # 모래 퍼뜨리기 
            
            if x == 0 and y == 0: # (1,1) 도착하면 종료 
                break
    
        dir = (dir + 1) % 4 # 방향 변경 
    
    steps += 1 # step 크기 중가 

print(out_sand)
    