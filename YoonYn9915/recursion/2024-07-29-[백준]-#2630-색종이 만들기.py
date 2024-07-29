import sys


# 주어진 정사각형이 모두 같은 색인지 확인하는 함수
def checkRectangle(arr, rowStart, rowEnd, colStart, colEnd):
    global ans1, ans2

    # 첫 번째 요소로 초기 색상 설정
    initial = arr[rowStart][colStart]

    # 주어진 정사각형이 모두 같은 색인지 확인
    for i in range(rowStart, rowEnd):
        for j in range(colStart, colEnd):
            if arr[i][j] != initial:
                # 모두 같은 색이 아니면 4개의 작은 정사각형으로 분할하여 재귀 호출
                midRow = (rowStart + rowEnd) // 2
                midCol = (colStart + colEnd) // 2
                checkRectangle(arr, rowStart, midRow, colStart, midCol)
                checkRectangle(arr, rowStart, midRow, midCol, colEnd)
                checkRectangle(arr, midRow, rowEnd, colStart, midCol)
                checkRectangle(arr, midRow, rowEnd, midCol, colEnd)
                return

    if initial == 0:
        ans1 += 1
    else:
        ans2 += 1


n = int(sys.stdin.readline().strip())

ans1 = 0
ans2 = 0
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

checkRectangle(arr, 0, n, 0, n)

print(ans1)
print(ans2)
