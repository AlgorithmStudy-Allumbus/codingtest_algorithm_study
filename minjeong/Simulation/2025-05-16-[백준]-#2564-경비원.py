import sys
input = sys.stdin.readline

# 1. 입력받기
w, h = map(int, input().split())    # 가로, 세로
store_cnt = int(input())            # 상점의 개수

# 2. 둘레 계산
perimeter = 2 * (w + h)

# 3. (방향, 거리) -> 1차원 위치로 변환 함수
def to_pos(dir, dist):
    if dir == 1:    # 북
        return dist
    if dir == 2:    # 남
        return w + h + (w - dist)
    if dir == 3:    # 서
        return 2*w + h + (h - dist)
    if dir == 4:    # 동
        return w + dist


# 4. 모든 상점의 위치를 1차원 조표로 변환해서 리스트에 모으기
store_loc = []  # 상점의 위치
for _ in range(store_cnt):
    d, dist = map(int, input().split())
    store_loc.append(to_pos(d, dist))

# 5. 경비원 위치도 똑같이 변환
gd, gdist = map(int, input().split())
guard_pos = to_pos(gd, gdist)

# print(f"store: {store_loc}")
# print(f"guard: {guard_pos}")

# 6. 각 상점까지 최단 거리 구해서 합산
total = 0
for store in store_loc:
    diff = abs(store - guard_pos)
    # 시계방향 <-> 반시계방향 중 짧은 거리 선택
    total += min(diff, perimeter - diff)

# 7. 결과 출력
print(total)