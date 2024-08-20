import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 스크린 칸 수, M: 바구니 크기
J = int(input())    # 떨어지는 사과의 개수
apple_pos = []      # 떨어지는 사과의 위치
for _ in range(J):
    apple_pos.append(int(input()))

#  바구니 초기 위치: 스크린 가장 왼쪽
basket_left = 1
basket_right = M
distance = 0    # 이동거리

for apple in apple_pos:
    # 바구니가 사과를 담을 수 있는 위치에 있는 경우
    if basket_left <= apple <= basket_right:
        continue
    # 바구니가 사과의 왼쪽에 있는 경우
    elif basket_left < apple:
        distance += apple - basket_right
        basket_right = apple
        basket_left = apple - M + 1
    # 바구니가 사과의 오른쪽에 있는 경우
    elif apple < basket_right:
        distance += basket_left - apple
        basket_left = apple
        basket_right = apple + M - 1

print(distance)