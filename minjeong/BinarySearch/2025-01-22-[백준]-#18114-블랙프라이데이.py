import sys

input = sys.stdin.readline

# 입력
N, C = map(int, input().split())  # N: 물건의 개수, C: 목표 무게
items = list(map(int, input().split()))  # 물건의 무게

items.sort()  # 이분탐색을 위해 오름차순 정렬


def binary_search(left, right, target):
    """이분 탐색 함수: 배열에서 target이 존재하면 1, 없으면 0 반환"""
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return 1
        elif items[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0


def check(N, C):
    """조건을 만족하는 조합이 있는지 확인"""

    # 1개만 선택해도 되는 경우
    if C in items:
        return 1

    # 2개 또는 3개 조합 확인
    start, end = 0, N - 1
    while start < end:
        total = items[start] + items[end]

        # 2개로도 C를 만족하는 경우
        if total == C:
            return 1

        # 2개의 물건 무게 합이 C보다 크다면 end를 왼쪽으로
        elif total > C:
            end -= 1
        # 2개의 물건 무게의 합이 C보다 작을 경우 = 3개를 확인해야 하는 경우
        else:
            diff = C - total  # 부족한 무게 계산
            # 차이값이 start나 end에 위치한 값이 아니면서 동시에 부족한 무게를 이분탐색으로 찾는다.
            if items[start] != diff and items[end] != diff and binary_search(start, end, diff):
                return 1
            # 여기서 위의 조건이 성립되지 않는다면 start를 오른쪽으로 이동
            start += 1
    return 0


# 정답 출력
print(check(N, C))
