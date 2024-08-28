import sys
input = sys.stdin.readline

# N: 여름 일 수, T: 스타후르츠 자라는데 걸리는 일 수, C: 스타후르츠를 심을 수 있는 칸 수, # P: 개당 가격
N, T, C, P = map(int, input().split())

day = (N-1) // T
profit = day * C * P
print(profit)