import sys
input = sys.stdin.readline

N, K = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
print(li[K-1])