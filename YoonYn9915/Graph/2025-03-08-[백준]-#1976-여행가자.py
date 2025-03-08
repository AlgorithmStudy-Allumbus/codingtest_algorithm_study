import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
network = []
visited = [0 for _ in range(n)]
for _ in range(n):
    network.append(list(map(int, input().split())))
lst = list(map(int, input().split()))


def dfs(start):
    visited[start] = 1
    for index, j in enumerate(network[start]):
        if j == 1 and visited[index] == 0:
            visited[index] = 1
            dfs(index)


dfs(lst[0] - 1)
if 0 not in visited:
    print('YES')
    exit()
for i in lst:
    if visited[i - 1] == 0:
        print('NO')
        exit()
print('YES')
