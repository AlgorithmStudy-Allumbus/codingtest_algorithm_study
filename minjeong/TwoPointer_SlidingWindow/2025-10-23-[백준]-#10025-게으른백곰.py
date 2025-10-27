import sys
input = sys.stdin.readline

# N: 얼음 양동이 수, K: 떨어진 거리
N, K = map(int, input().split())
buckets = []
max_x = 0
for _ in range(N):
    # g: 얼음 양, x: 양동이 좌표
    g, x = map(int, input().split())
    buckets.append((g, x))
    max_x = max(max_x, x)

arr = [0] * (max_x+1)
for g, x in buckets:
    arr[x] += g

window_size = 2 * K + 1
current = sum(arr[:window_size])
answer = current
for i in range(window_size, max_x + 1):
    current += arr[i] - arr[i - window_size]
    answer = max(answer, current)

print(answer)