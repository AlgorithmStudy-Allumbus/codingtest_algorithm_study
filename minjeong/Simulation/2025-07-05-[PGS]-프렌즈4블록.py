def check_remove(m, n, grid):
    """
    2×2 같은 블록을 찾아서, 지울 칸을 True로 표시한 2D 배열을 반환한다.
    """
    mark = [[False] * n for _ in range(m)]
    for i in range(m-1):
        for j in range(n-1):
            current = grid[i][j]
            if current and grid[i][j+1] == current \
                and grid[i+1][j] == current \
                and grid[i+1][j+1] == current:
                mark[i][j] = mark[i][j+1] = mark[i+1][j] = mark[i+1][j+1] = True
    return mark

def remove_blocks(m, n, grid, mark):
    """
    mark 배열이 True인 칸으르 찾아서 빈칸으로 바꾸고,
    삭제된 블록의 총 개수를 반환한다.
    """
    removed = 0
    for i in range(m):
        for j in range(n):
            if mark[i][j]:
                grid[i][j] = ""
                removed += 1
    return removed

def down_blocks(m, n, grid):
    """
    중력을 적용하여, 각 열마다 빈칸 위의 블록을 아래로 당긴다.
    """
    for j in range(n):
        stack = []
        for i in range(m):
            if grid[i][j] != "":
                stack.append(grid[i][j])

        for i in range(m-1, -1, -1):
            if stack:
                grid[i][j] = stack.pop()

            else:
                grid[i][j] = ""

def solution(m, n, board):
    # 1. 입력 문자열을 2D 리스트로 변환
    grid = [list(row) for row in board]
    total_removed = 0

    while True:
        # 2. 지울 칸 표시
        mark = check_remove(m, n, grid)
        # 3. 표시된 칸 삭제 및 개수 세기
        removed = remove_blocks(m, n, grid, mark)
        if removed == 0:
            # 더이상 지울 블록이 없다면 반복 종료
            break
        # 4. 전체 삭제 개수에 해당 칸의 삭제 개수 누적해서 더하기
        total_removed += removed
        # 5. 중력 적용
        down_blocks(m, n, grid)

    return total_removed
