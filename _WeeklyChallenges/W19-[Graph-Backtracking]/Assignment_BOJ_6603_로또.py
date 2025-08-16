"""
BOJ #6603. 로또 (실버2)
https://www.acmicpc.net/problem/6603
유형: Graph, Backtracking
"""

"""
#6603. 로또
백트래킹 풀이
"""
import sys
input = sys.stdin.readline
def backtrack(lotto, current):
    if len(lotto) == 6:  # 종료조건
        print(' '.join(map(str, lotto)))
        return

    for i in range(current, k):
        lotto.append(S[i])
        backtrack(lotto, i+1)
        lotto.pop()


while True:
    testcase = input().strip()
    if testcase == '0':
        break
    nums = list(map(int, testcase.split()))
    k, S = nums[0], nums[1:]

    backtrack([], 0)
    print()


"""
#6603. 로또
조합 풀이
"""
import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    testcase = input().strip()
    if testcase == '0':
        break
    nums = list(map(int, testcase.split()))
    k, S = nums[0], nums[1:]
    combs = list(combinations(S, 6))
    for comb in combs:
        print(' '.join(map(str, comb)))
    print()