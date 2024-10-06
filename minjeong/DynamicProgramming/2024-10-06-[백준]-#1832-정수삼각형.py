import sys
input = sys.stdin.readline

n = int(input()) # 삼각형 크기
triangle = []
for i in range(n):
    line = list(map(int, input().split()))
    triangle.append(line)

# DP 채우기
for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1]))