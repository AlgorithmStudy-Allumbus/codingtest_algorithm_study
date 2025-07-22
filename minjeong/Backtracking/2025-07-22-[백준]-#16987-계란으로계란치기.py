import sys

input = sys.stdin.readline

N = int(input())  # 계란의 수
eggs = [list(map(int, input().split())) for _ in range(N)]  # 계란의 내구도와 무게를 담은 리스트

max_broken = 0  # 최대 깨진 계란 수를 저장하는 변수


def count_broken_eggs(eggs):
    # 깨진 계란의 수 구하기
    count = 0
    for S, W in eggs:
        if S <= 0:
            count += 1
    return count


def dfs(cur_idx):
    global max_broken
    # 모든 계란을 한 번씩 든 경우
    if cur_idx == N:
        # 깨진 계란의 수 세고 max_broken 갱신
        max_broken = max(max_broken, count_broken_eggs(eggs))
        return

    # 현재 계란이 깨졌다면 다음 계란으로 넘어간다.
    if eggs[cur_idx][0] <= 0:
        dfs(cur_idx + 1)
        return

    broken = False  # 현재 계란으로 다른 계란을 깼는지 여부
    for i in range(N):
        if i == cur_idx or eggs[i][0] <= 0:
            continue

        # 계란끼리 치기
        eggs[cur_idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[cur_idx][1]
        broken = True

        # 탐색
        dfs(cur_idx + 1)  # 다음 계란으로 넘어간다.

        # 상태 복구
        eggs[cur_idx][0] += eggs[i][1]
        eggs[i][0] += eggs[cur_idx][1]

    # 칠 수 있는 계란이 없었던 경우, 다음으로 넘어가야 한다.
    if not broken:
        dfs(cur_idx + 1)


dfs(0)
print(max_broken)