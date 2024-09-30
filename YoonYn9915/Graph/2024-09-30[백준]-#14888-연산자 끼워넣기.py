
def dfs(level, total, plus, minus, mul, div):
    global max_result
    global min_result
    global n

    #종료 조건
    if level == n:
        max_result = max(total, max_result)
        min_result = min(total, min_result)

    if plus != 0:
        dfs(level + 1, total + nums[level], plus - 1, minus, mul, div)
    if minus != 0:
        dfs(level + 1, total - nums[level], plus, minus - 1, mul, div)
    if mul != 0:
        dfs(level + 1, total * nums[level], plus, minus, mul - 1, div)
    if div != 0:
        dfs(level + 1, int(total / nums[level]), plus, minus, mul, div - 1)


n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

max_result = -int(1e9)
min_result = int(1e9)
dfs(1, nums[0], op[0], op[1], op[2], op[3])

print(max_result)
print(min_result)
