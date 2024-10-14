import sys
input = sys.stdin.readline

N = int(input())                            # 병사 수
soldiers = list(map(int, input().split()))  # 병사의 전투력 리스트
dp = [1 for _ in range(N)]                  # 모든 병사는 자기 혼자일 때 길이가 1인 수열을 가질 수 있으므로, DP의 초기값을 1로 설정

soldiers.reverse()                          # 병사들의 전투력을 내림차순으로 배치하기 위해 리스트를 뒤집는다.

for i in range(1, N):
    for j in range(i):
    # i번째(현재) 병사의 전투력이 j번째(비교) 병사의 전투력보다 클 경우, 즉 내림차순이 유지되는 경우
        if soldiers[i] > soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)    # i번째 병사의 DP 값을 갱신

# (전체 병사 수) - (가장 긴 증가하는 부분 수열의 길이) = (열외해야 할 병사의 수)
print(N - max(dp))