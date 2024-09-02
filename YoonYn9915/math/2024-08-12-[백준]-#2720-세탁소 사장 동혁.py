# 1. 거스름돈의 개수가 최소여야 하므로 greedy 알고리즘을 이용해서 단위가 큰 쿼터부터 계산해준다.


import sys


def compute(item):
    ans = [0] * 4
    global quarter, dime, nickel, penny

    while item != 0:
        if item - quarter >= 0:
            item -= quarter
            ans[0] += 1
            continue
        if item - dime >= 0:
            item -= dime
            ans[1] += 1
            continue
        if item - nickel >= 0:
            item -= nickel
            ans[2] += 1
            continue
        if item - penny >= 0:
            item -= penny
            ans[3] += 1
            continue
    return ans


inp = sys.stdin.readline

n = int(inp())
arr = []

quarter = 25
dime = 10
nickel = 5
penny = 1

for i in range(n):
    arr.append(int(inp()))

for item in arr:
    answers = compute(item)
    for ans in answers:
        print(ans, end=" ")
    print()
