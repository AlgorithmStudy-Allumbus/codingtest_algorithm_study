'''
BOJ #1700. 멀티탭 스케줄링 (골드1)
https://www.acmicpc.net/problem/1700
유형: Greedy
'''

import sys
input = sys.stdin.read

data = input().split() 
N, K = int(data[0]), int(data[1]) # 멀티탭 구멍 수와 전기 용품 사용 횟수
sequence = list(map(int, data[2:]))  # 전기 용품 사용 순서

multitap = []  # 현재 멀티탭 상태
unplug_count = 0  # 플러그를 뽑는 횟수

# 순차적으로 전기용품 사용 
for i in range(K):
    current = sequence[i]

    # 1. 이미 멀티탭에 꽂혀 있는 경우
    if current in multitap:
        continue # 아무 작업도 하지 않고 넘어감

    # 2. 멀티탭에 빈 자리가 있는 경우
    if len(multitap) < N:
        multitap.append(current) # 새로운 전기용품을 추가함
        continue

    # 3. 멀티탭이 가득 차 있는 경우: 뽑을 전기 용품 결정
    farthest_idx = -1
    to_unplug = -1
    for plug in multitap:
        if plug not in sequence[i:]:  # 앞으로 사용되지 않는 플러그
            to_unplug = plug
            break
        else:
            # 가장 나중에 사용되는 플러그 
            idx = sequence[i:].index(plug)
            if idx > farthest_idx:
                farthest_idx = idx
                to_unplug = plug

    # 플러그 교체
    multitap.remove(to_unplug)
    multitap.append(current)
    unplug_count += 1

print(unplug_count)