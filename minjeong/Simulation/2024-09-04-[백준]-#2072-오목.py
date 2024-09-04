import sys
input = sys.stdin.readline


def check_winner(x, y, color):
    # 오목 4개 방향
    directions = [(-1, 0), (0, -1), (-1, -1), (-1, 1)]
    # (-1, 0) - 세로 방향 (위쪽)
    # (0, -1) - 가로 방향 (왼쪽)
    # (-1, -1) - 좌상향 대각선 방향
    # (-1, 1) - 우상향 대각선 방향

    for dx, dy in directions:
        count = 1  # 현재 돌이 포함된 연속된 돌의 개수를 셀 변수 초기화

        # 주어진 방향으로 연속된 돌 개수 세기
        nx, ny = x + dx, y + dy
        while 1 <= nx < 20 and 1 <= ny < 20 and board[nx][ny] == color:
            count += 1
            # 방향 dx, dy로 이동하며 해당 방향에 같은 색의 돌이 있는 한 계속 탐색
            nx += dx
            ny += dy

        # 반대 방향으로도 연속된 돌 개수 세기
        nx, ny = x - dx, y - dy
        while 1 <= nx < 20 and 1 <= ny < 20 and board[nx][ny] == color:
            count += 1
            # 반대 방향으로도 이동하여 연속된 돌의 개수를 추가로 셈
            nx -= dx
            ny -= dy

        # 5개일 경우만 승리로 인정
        if count == 5:
            return True

    return False # 5개의 돌이 연속되지 않을 경우

N = int(input().strip())  # 돌의 개수
board = [[0] * 20 for _ in range(20)]  # 19x19 바둑판 / 바둑돌이 놓인 위치 기록 (1,1)~(19,19)

# 입력된 좌표에 돌을 기록
for i in range(N):
    x, y = map(int, input().strip().split()) # 각 수의 좌표
    color = 1 if i % 2 == 0 else 2 # 홀수 번째 수: 흑돌(1), 짝수 번째 수: 백돌(2)
    board[x][y] = color # 해당 좌표에 돌을 놓음 (바둑판 배열에 기록)

    if check_winner(x, y, color): # 현재 놓은 돌로 인해 승리가 결정되는지 확인
        print(i + 1)              # 승리가 결정되면 현재 몇 번째 수인지 출력하고 프로그램 종료
        sys.exit()

print(-1) # 모든 돌을 놓았지만 승패가 결정되지 않으면 -1 출력