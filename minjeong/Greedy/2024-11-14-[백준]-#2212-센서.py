import sys
input = sys.stdin.readline

n = int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수
pos = list(map(int, input().split())) # 센서의 좌표

pos = sorted(set(pos)) # 센서 위치 정렬 및 중복 제거
distances = [] # 센서 간 거리 차이

# 센서 간 거리 차이 계산
for i in range(1, len(pos)):
    distances.append(pos[i] - pos[i-1])

# 거리 차이 큰 순서로 정렬
distances.sort(reverse=True)

# 가장 큰 (k-1)개의 거리 차이를 빼고 남은 거리들의 합이 최소가 되는 거리 합
min_dist_sum = sum(distances[k-1:])

print(min_dist_sum)