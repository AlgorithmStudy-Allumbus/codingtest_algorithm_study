N, K = map(int, input().split())

num_list = [int(input()) for _ in range(N)]

point = 0  # 지목을 하는 사람 (0부터 시작)
M = 0       # 지목 횟수(M번째 지목)

for i in range(N):
    target = num_list[point]    # target: 지목당한 사람
    M += 1                      # 지목했으니까 카운트 1 증가
    if target == K:
        print(M)
        break
    point = target    # 지목당한 사람이 이제는 지목하는 사람이 됨
else:
    print(-1)