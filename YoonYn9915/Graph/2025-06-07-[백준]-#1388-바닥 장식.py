
def dfs(x, y):
    if graph[x][y] == '-':
        graph[x][y] = 1
        for _y in [1, -1]:
            Y = y + _y
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                dfs(x, Y)
    if graph[x][y] == '|':
        graph[x][y] = 1
        for _x in [1, -1]:
            X = x + _x
            if (X > 0 and X < n) and graph[X][y] == '|':
                dfs(X, y)


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i, j)
            count += 1
