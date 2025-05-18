'''
1. 아이디어
- 방향이 두가지이고 최소거리는 둘레 // 2 보다 작거나 같아야 하므로, 시계방향 거리를 구해서 둘레 // 2와 비교하며 처리하자
- 동근이와 상점의 시계방향 거리를 구할때는 (0,0)을 기준점으로 잡고 기준점부터 동근이의 거리, 기준점부터 상점의 거리를 구한 후 차이를 구하자

2. 시간복잡도
상점 위치 입력 → O(nums)
거리 계산 → O(nums)
최대 O(100)로 1초안에 가능 (n이 100이하니까)

3. 구현
3-1. 입력 받기
3-2. 전체 둘레 계산
3-3. 시계 방향으로 거리 계산 함수 정의
3-4. (0,0)에서부터 시계방향으로 동근이와 상점의 거리 구하기
3-5. 3-4를 기반으로 시계방향으로 동근이와 상점의 거리 구하기
3-6. 시계방향 거리가 전체 둘레의 절반보다 작다면 시계방향을 더하고, 크다면 반시계방향 거리 더하기
3-7. 결과 출력
'''

import sys

inp = sys.stdin.readline

row, col = map(int, inp().strip().split())

# 전체 둘레
round_length = row * 2 + col * 2
answer = 0

# 동근이의 위치와 상점의 좌표 저장
locations = []
n = int(inp().strip())

for _ in range(n + 1):
    dir, num = map(int, inp().strip().split())
    locations.append((dir, num))


def calculate_distance(dir, num):
    if dir == 1:
        return num
    elif dir == 2:
        return row + col + (row - num)
    elif dir == 3:
        return row + col + row + (col - num)
    else:
        return row + num


for i in range(n):
    # 동근이 좌표
    dir, num = locations[n]

    # 상점 좌표
    store_dir, store_num = locations[i]

    # (0,0)에서부터 시계방향으로 동근이의 거리
    d1 = calculate_distance(dir, num)

    # (0,0)에서부터 시계방향으로 상점의 거리
    d2 = calculate_distance(store_dir, store_num)

    # 시계방향 동근이 - 상점간 거리
    distance = abs(d2 - d1)

    if distance < round_length // 2:
        answer += distance
    else:
        answer += round_length - distance

print(answer)