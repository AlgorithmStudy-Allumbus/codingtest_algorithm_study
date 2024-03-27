import sys
input = sys.stdin.readline

n = int(input())
cost = []
for i in range(n):
    temp = list(map(int, input().split()))
    cost.append(temp)

# 0: RED, 1: GREEN, 2: BLUE
for i in range(1, n):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0] # RED
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1] # GREEN
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2] # BLUE

print(min(cost[-1][0], cost[-1][1], cost[-1][2]))