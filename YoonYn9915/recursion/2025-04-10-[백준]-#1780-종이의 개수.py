
import sys

def recursion(paper, row_start, col_start, step):
    # 종이가 같은지 검사
    result = check_paper_same(paper, row_start, col_start, step)

    # 같지 않다면 9분할한뒤 각각을 재귀적으로 검사
    if result == 2:
        for i in range(3):
            for j in range(3):
                row = row_start + (i * step // 3)
                col = col_start + (j * step // 3)
                recursion(paper, row, col, step // 3)
    else:
        # 종이의 칸이 다 같은 경우
        answer[result] += 1



def check_paper_same(paper, row_start, col_start, step):
    base = paper[row_start][col_start]
    for i in range(row_start, row_start + step):
        for j in range(col_start, col_start + step):
            if paper[i][j] != base:
                return 2
    return base


inp = sys.stdin.readline

n = int(inp())

paper = []

# 각각 -1, 0, 1로만 이루어진 종이의 개수 저장 튜플
global answer
answer = {-1: 0, 0: 0, 1: 0}

for i in range(n):
    paper.append(list(map(int, inp().split())))

recursion(paper, 0, 0, n)

print('\n'.join(str(value) for value in answer.values()))
