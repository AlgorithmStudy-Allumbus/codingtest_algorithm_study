# 15996 : 팩토리얼 나누기
import sys
input = sys.stdin.readline

N, A = map(int, input().split())
k = 0
power = A

while N >= power:
    k += N // power
    power *= A

print(k)