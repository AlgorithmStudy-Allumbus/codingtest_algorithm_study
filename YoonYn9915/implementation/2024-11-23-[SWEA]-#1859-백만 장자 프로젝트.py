N = int(input())
ansList = []

for i in range(N):
    days = int(input())
    costs = list(map(int, input().split()))
    ans = 0

    maxCost = -1

    for j in range(len(costs) - 1, -1, -1):
        if maxCost > costs[j]:
            ans += maxCost - costs[j]
        else:
            maxCost = costs[j]

    ansList.append(ans)

for i in range(len(ansList)):
    print(f"#{i + 1} {ansList[i]}")
