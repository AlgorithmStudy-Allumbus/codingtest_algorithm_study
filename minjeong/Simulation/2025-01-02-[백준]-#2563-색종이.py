import sys
input = sys.stdin.readline

n = int(input())  # 색종이의 수
paper = [[0] * 100 for _ in range(100)]  # 100x100 도화지 초기화

# 색종이를 하나씩 붙이기
for _ in range(n):
    x, y = map(int, input().split())

    # 10x10 크기의 영역을 1로 채운다.
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 도화지에서 1의 개수를 모두 더하여 넓이 계산
answer = 0
for row in paper:
    answer += sum(row)

print(answer)