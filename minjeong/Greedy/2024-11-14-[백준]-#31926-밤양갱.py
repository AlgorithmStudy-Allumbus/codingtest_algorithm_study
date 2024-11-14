import sys
input = sys.stdin.readline

n = int(input())

# 기본 시간은 10초
answer = 10

# n이 2의 거듭제곱이 될 때마다 시간을 1씩 증가시킴
while n > 1:
    n //= 2
    answer += 1

print(answer)