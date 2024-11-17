def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    while True:
        # 2x2 형태로 같은 블록이 있는지 확인
        blocks_to_remove = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != '#':
                    blocks_to_remove |= {(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)}

        if not blocks_to_remove:
            break

        # 블록 제거
        for i, j in blocks_to_remove:
            board[i][j] = '#'
            answer += 1

        # 블록이 떨어지는 과정
        for j in range(n):
            for i in range(m - 1, -1, -1):
                if board[i][j] == '#':
                    for k in range(i - 1, -1, -1):
                        if board[k][j] != '#':
                            board[i][j], board[k][j] = board[k][j], '#'
                            break

    return answer
