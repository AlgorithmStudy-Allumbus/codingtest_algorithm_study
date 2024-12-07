import sys
from collections import deque

input = sys.stdin.readline

# 1. 입력 처리
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 2. 초기화
bridge = deque()  # 다리 위 트럭들: (트럭 무게, 다리에서 빠져나갈 시간)
current_weight = 0  # 다리 위의 현재 총 무게
time = 0  # 현재 시간
truck_index = 0  # 대기 중인 트럭의 인덱스

# 3. 시뮬레이션 수행
while truck_index < n or bridge:
    time += 1  # 시간 + 1

    # 3.1 다리에서 빠져나갈 트럭 제거
    if bridge and bridge[0][1] == time:  # 다리에서 나갈 시간인지 확인
        truck_weight, _ = bridge.popleft()
        current_weight -= truck_weight

    # 3.2 새로운 트럭을 다리에 올릴 수 있는지 확인
    if truck_index < n and current_weight + trucks[truck_index] <= L:
        bridge.append((trucks[truck_index], time + w))  # 트럭 추가 (무게, 나갈 시간)
        current_weight += trucks[truck_index]
        truck_index += 1

# 4. 결과 출력
print(time)