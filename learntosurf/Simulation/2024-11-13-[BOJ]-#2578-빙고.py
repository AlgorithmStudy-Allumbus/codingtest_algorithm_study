import sys 
input = sys.stdin.readline 

board = [list(map(int, input().split())) for _ in range(5)]
num = [int(x) for _ in range(5) for x in input().split()]

visited = [[False] * 5 for _ in range(5)]
bingo = 0 

def update_visited(num, board, visited):
    for row in range(5):
        for col in range(5):
            if board[row][col] == num:
                visited[row][col] = True 

def check_bingo(visited):
    bingo = 0
    
    # 가로줄 검사 
    for row in range(5):
        if all(visited[row][col] for col in range(5)):
            bingo += 1
    
    # 세로줄 검사
    for col in range(5):
        if all(visited[row][col] for row in range(5)):
            bingo += 1
    
    # 대각선 검사
    if all(visited[i][i] for i in range(5)):
        bingo += 1
    if all(visited[i][4-i] for i in range(5)):
        bingo += 1
    
    return bingo 
    

for idx, i in enumerate(num, start=1):
    update_visited(i, board, visited)
    if check_bingo(visited) >= 3:
        print(idx)
        break