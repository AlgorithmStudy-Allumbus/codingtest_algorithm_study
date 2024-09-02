import sys
input = sys.stdin.readline
t, x, m = map(int, input().strip().split())

if m == 0:
    print(t * x)
    exit()

# 첫 번째 몬스터의 거리와 속도 입력 받기
d, s = map(int, sys.stdin.readline().strip().split())
min_time = (d - 1) // s # 초기 최소 도달 시간 설정

# 나머지 몬스터들에 대해 최소 도달 시간 계산
for _ in range(m - 1):
    d, s = map(int, sys.stdin.readline().strip().split())
    time_to_reach = (d - 1) // s
    if min_time > time_to_reach:
        min_time = time_to_reach

if min_time == 0: # 최소 시간이 0이라면 금화를 줍지 못함
    print(0)
elif t > min_time:
    # 총 t 시간 중 min_time 시간을 사용하고 남은 시간은 (t - min_time)
    # 이 남은 시간을 절반씩 나누어 금화를 줍고 기다리는 과정을 반복
    print((min_time + ((t - min_time) // 2)) * x)
else: # t < min_time
    print(t * x)