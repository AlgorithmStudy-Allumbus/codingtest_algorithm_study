# 재귀적으로 정사각형을 4분할한다.
# 재귀 시작시 ( 출력, 종료시 ) 출력
# 재귀 종료조건은 정사각형의 모든 값이 같거나, 정사각형이 길이가 1일때

import sys


def recursion(arr, n, row, col):
    global ans

    if n == 1:
        ans.append(arr[row][col])
        return

    flag = 0
    first = arr[row][col]
    for i in range(n):
        for j in range(n):
            if arr[row + i][col + j] != first:
                flag = 1
                break

    if flag == 0:
        ans.append(first)
        return
    else:
        ans.append('(')
        recursion(arr, n // 2, row, col)
        recursion(arr, n // 2, row, col + n // 2)
        recursion(arr, n // 2, row + n // 2, col)
        recursion(arr, n // 2, row + n // 2, col + n // 2)
        ans.append(')')



inp = sys.stdin.readline

n = int(inp())
arr = []

for _ in range(n):
    arr.append(inp().strip())

ans = []

recursion(arr, n, 0, 0)

for i in range(len(ans)):
    print(ans[i], end="")
