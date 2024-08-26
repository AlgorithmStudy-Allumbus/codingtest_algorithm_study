import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split()) # 고리 회원의 수 N, 치킨 종류의 수 M
likes = [] # 각 회원의 치킨 선호도
for _ in range(N):
    likes.append(list(map(int, input().split())))
# likes = [list(map(int, input().split())) for _ in range(N)]

max_like = 0 # 고리 회원들의 만족도의 합의 최댓값
for a, b, c in combinations(range(M), 3): # M개의 치킨 종류 중에서 3가지를 선택하는 모든 조합
    tmp_like = 0 # 현재 조합에 대한 회원들의 총 만족도를 계산할 임시 변수
    for i in range(N): # 회원별로 만족도 계산
        # 회원 i의 선호도 중에서 선택된 3개의 치킨 중 가장 높은 선호도를 찾는다.
        tmp_like += max(likes[i][a], likes[i][b], likes[i][c])
    max_like = max(max_like, tmp_like)

print(max_like)