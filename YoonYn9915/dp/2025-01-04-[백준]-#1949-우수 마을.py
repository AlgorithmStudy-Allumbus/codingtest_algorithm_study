import sys, collections

sys.setrecursionlimit(10 ** 6)


def dfs(cur):
    visited[cur] = 1
    for u in g[cur]:
        if not visited[u]:
            dfs(u)
            dp[cur][1] += dp[u][0]
            dp[cur][0] += max(dp[u][0], dp[u][1])


n = int(sys.stdin.readline().strip())
cost = [0] + [int(x) for x in sys.stdin.readline().split()]

visited = [0 for _ in range(n + 1)]
dp = [[0, cost[i]] * 2 for i in range(n + 1)]
g = collections.defaultdict(list)

for _ in range(n - 1):
    v, u = map(int, sys.stdin.readline().split())
    g[v].append(u)
    g[u].append(v)

dfs(1)
print(max(dp[1][1], dp[1][0]))
