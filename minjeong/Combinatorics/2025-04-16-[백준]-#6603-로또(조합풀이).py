import sys
from itertools import combinations
input = sys.stdin.readline

"""
#6603. 로또
조합 풀이
"""

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