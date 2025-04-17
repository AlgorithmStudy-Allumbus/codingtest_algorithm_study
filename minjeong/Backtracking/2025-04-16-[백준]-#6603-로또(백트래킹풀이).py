import sys
input = sys.stdin.readline

"""
#6603. 로또
백트래킹 풀이
"""

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
