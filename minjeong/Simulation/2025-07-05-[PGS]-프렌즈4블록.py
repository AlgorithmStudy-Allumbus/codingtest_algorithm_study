def check(m, n, board):
    filter = [[0 for _ in range(n)] for _ in range(m)]
    count = 0

    for i in range(m - 1):
        for j in range(n - 1):
            a = board[i][j]
            b = board[i][j + 1]
            c = board[i + 1][j]
            d = board[i + 1][j + 1]
            if a == b == c == d and a != '0':
                filter[i][j], filter[i][j + 1], filter[i + 1][j], filter[i + 1][j + 1] = 1, 1, 1, 1

    for i in range(m):
        for j in range(n):
            if filter[i][j] == 1:
                count += 1
                board[i][j] = '0'

    if count == 0:
        return 0

    for i in range(m - 2, -1, -1):
        for j in range(n):
            k = i
            while 0 <= k + 1 < m and board[k + 1][j] == '0':
                k += 1
            if k != i:
                board[k][j] = board[i][j]
                board[i][j] = '0'

    return count


def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    while True:
        temp = check(m, n, board)
        if temp == 0:
            break
        answer += temp

    return answer