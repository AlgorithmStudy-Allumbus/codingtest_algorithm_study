import sys
input = sys.stdin.readline

x, y = map(int, input().split())  # 전체 게임 수(x)와 이긴 게임 수(y) 입력
z = (y * 100) // x  # 현재 승률 z 계산

if z >= 99:  # 만약 승률이 99% 이상이면 더 이상 승률을 변화시킬 수 없으므로 -1 출력 후 종료
    print(-1)
    exit(0)

answer = 0
left = 1  # 이분 탐색의 시작값 설정
right = x  # 이분 탐색의 끝값 설정

while left <= right:  # 이분 탐색 시작
    mid = (left + right) // 2  # 중간 값 계산
    if ((y + mid) * 100) // (x + mid) <= z:  # 추가한 게임 후 승률 계산
        left = mid + 1  # 승률이 변하지 않으면 더 많은 게임을 추가해야 하므로 left 증가
    else:
        answer = mid  # 승률이 변하면 해당 mid 값을 저장하고
        right = mid - 1  # 더 적은 게임에서 승률이 변할 수 있는지 확인하기 위해 right 감소

print(answer)  # 최종적으로 구한 최소 게임 수 출력