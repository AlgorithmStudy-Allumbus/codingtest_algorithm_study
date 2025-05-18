import sys

input = sys.stdin.readline

def main():
    N = int(input())  # 지방의 수
    budgets = sorted(map(int, input().split()))  # 각 지방의 예상요청
    M = int(input())  # 총 예산

    # 1. 모든 요청이 배정될 수 있는 경우, 요청 최대값이 정답
    if sum(budgets) <= M:
        return budgets[-1]

    # 2. 모든 요청이 배정될 수 없는 경우, 상한액 탐색
    left = 0
    right = budgets[-1]
    answer = 0

    while left <= right:
        mid = (left + right) // 2 # 상한액
        total = 0
        for b in budgets:
            total += min(b, mid)

        if total <= M:
            # 이 상한액으로 배정해도 총액이 허용 범위 이내 → C를 더 높여 볼 수 있음
            answer = mid
            left = mid + 1
        else:
            # 총액이 초과 → 상한액을 낮춰야 함
            right = mid - 1

    return answer


if __name__ == '__main__':
    print(main())
