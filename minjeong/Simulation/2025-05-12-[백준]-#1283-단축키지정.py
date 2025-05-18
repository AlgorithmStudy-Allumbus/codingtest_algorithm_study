import sys

input = sys.stdin.readline


def setOptions(option):
    # 1. 각 단어의 첫 글자 우선 확인
    for i in range(len(option)):
        if option[i][0].upper() not in shortcut_key:
            shortcut_key.add(option[i][0].upper())
            option[i] = f"[{option[i][0]}]{option[i][1:]}"
            return option

    # 2. 전체 단어의 모든 글자 중 아직 등록되지 않은 글자 탐색
    for i in range(len(option)):
        for j in range(len(option[i])):
            if option[i][j].upper() not in shortcut_key:
                shortcut_key.add(option[i][j].upper())
                option[i] = f"{option[i][:j]}[{option[i][j]}]{option[i][j + 1:]}"
                return option

    # 3. 지정할 수 있는 단축키가 없는 경우
    return option


N = int(input())
shortcut_key = set()

for _ in range(N):
    option = input().split()
    result = setOptions(option)
    print(' '.join(result))
