t = int(input())

for i in range(t):
    col = int(input())
    graph=[]
    for j in range(2):
        graph.append(list(map(int, input().split())))

    if col == 1:
        print(max(graph[0][0], graph[1][0]))
        continue

    graph[0][1] += graph[1][0]
    graph[1][1] += graph[0][0]

    for k in range(2, col):
        graph[0][k] += max(graph[1][k-1], graph[1][k-2])
        graph[1][k] += max(graph[0][k-1], graph[0][k-2])

    print(max(graph[0][col-1], graph[1][col-1]))