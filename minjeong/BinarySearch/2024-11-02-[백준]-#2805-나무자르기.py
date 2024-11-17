import sys
input = sys.stdin.readline

# 나무의 수 N, 가져갈 나무의 길이 M
N, M = map(int, input().split())
# 나무의 길이들 입력
trees = list(map(int, input().split()))

# 시작점과 끝점 설정
left = 0
right = max(trees)
answer = 0

while left <= right:
    total = 0
    mid = (left + right) // 2
      # mid 높이로 나무를 잘라서 얻을 수 있는 나무의 길이 계산
    for tree in trees:
        # 나무의 높이가 더 크다면
        if tree > mid:
            total += tree - mid
    # 잘린 나무의 길이가 부족하다면 더 낮은 높이(왼쪽 부분) 탐색
    if total < M:
        right = mid - 1
    # 나무 길이가 충분하다면 answer에 저장하고, 더 높게 잘라(오른쪽 부분) 탐색
    else:
        answer = mid
        left = mid + 1

# 최종 절단기 높이 출력
print(answer)