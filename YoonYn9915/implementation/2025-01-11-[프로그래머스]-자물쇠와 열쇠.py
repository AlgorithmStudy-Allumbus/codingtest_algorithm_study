# 배열 rotation
def rotation(arr):
    retArr = [[0] * len(arr) for _ in range(len(arr))]
    # 11 > 13 / 12 > 23 / 13 > 33
    for i in range(len(arr)):
        for j in range(len(arr)):
            retArr[j][len(arr) - 1 - i] = arr[i][j]
    return retArr


# 정값 체크
def checkSol(keyArr, lockArr, x, y):
    keySize = len(keyArr)
    lockSize = len(lockArr)

    boardSize = lockSize * 3
    board = [[0] * (boardSize) for _ in range(boardSize)]

    start = lockSize - 1
    end = start + lockSize

    # boardArr 에 lock 삽입
    for i in range(lockSize):
        for j in range(lockSize):
            board[start + i][start + j] += lockArr[i][j]

    # boardArr 에 key 삽입
    for i in range(keySize):
        for j in range(keySize):
            board[i + x][j + y] += keyArr[i][j]  # 값 복사

    # 전부 1인지 체크
    for i in range(start, end):
        for j in range(start, end):
            if board[i][j] != 1:
                return False
    return True


def solution(key, lock):
    for _ in range(4):

        # 값 이동
        for x in range((len(lock) * 2) - 1):
            for y in range((len(lock) * 2) - 1):
                if checkSol(key, lock, x, y) == True:
                    return True

        # key 회전
        key = rotation(key)

    return False