import sys 
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
points = list(map(int, input().split()))
lines = [tuple(map(int, input().split())) for _ in range(M)]

points.sort()

counts = []
for start, end in lines:
    left = bisect_left(points, start)  
    right = bisect_right(points, end)
    counts.append(right - left)

print("\n".join(map(str, counts)))