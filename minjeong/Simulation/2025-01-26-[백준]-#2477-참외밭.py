import sys
input = sys.stdin.readline

# 입력 받기
K = int(input())  # 1m2에 자라는 참외의 개수
edges = []
for _ in range(6):
    direction, length = map(int, input().split())
    edges.append((direction, length))

# 큰 직사각형과 작은 직사각형 찾기
big_area = 0
small_area = 0

for i in range(6):
    current = edges[i][1]
    next_edge = edges[(i + 1) % 6][1]  # 인덱스 순환 처리
    big_area = max(big_area, current * next_edge)

# 작은 직사각형의 면적 찾기
for i in range(6):
		# big_area에 해당하는 인덱스를 찾았다면 그 반대 방향의 면적 찾기
    if edges[i][1] * edges[(i + 1) % 6][1] == big_area:
        small_area = edges[(i + 3) % 6][1] * edges[(i + 4) % 6][1]
        break

# 전체 면적 계산
total_area = big_area - small_area
result = K * total_area
print(result)
