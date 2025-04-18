import sys
input = sys.stdin.readline


def min_ops_to_pal(s):
    """
    s: list of chars
    return: 최소 편집 연산(삽입, 삭제, 교체만 허용)으로 s를 팰린드롬으로 만드는 비용
    """
    n = len(s)
    # dp[i][j]: s[i..j]를 팰린드롬으로 만드는 최소 연산 횟수
    dp = [[0] * n for _ in range(n)]
    # 길이 2부터 n까지 늘려가며
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                # 교체(대칭 맞추기), 삭제(왼쪽), 삭제(오른쪽)
                dp[i][j] = min(
                    dp[i + 1][j - 1] + 1,
                    dp[i + 1][j] + 1,
                    dp[i][j - 1] + 1
                )
    for d in dp:
        print(d)

    return dp[0][n - 1] if n > 0 else 0


s = list(input().rstrip())
n = len(s)

# 1. 교환 없이 삽입/삭제/교체만 사용했을 때
ans = min_ops_to_pal(s)
if ans <= 1:
    print(ans)
    exit()

# 2. 서로 다른 문자끼리 한 번만 교환을 허용해봤을 때, 교환 비용 1을 더해보고 개선되는지 확인
for i in range(n):
    for j in range(i + 1, n):
        if s[i] != s[j]:
            # 문자가 같지 않은 경우, SWAP
            s[i], s[j] = s[j], s[i]
            swap_cost = min_ops_to_pal(s) + 1  # swap 비용 포함
            if swap_cost < ans: # swap한 경우가 더 작다면 ans에 업데이트
                ans = swap_cost
            # 복구
            s[i], s[j] = s[j], s[i]
print(ans)
