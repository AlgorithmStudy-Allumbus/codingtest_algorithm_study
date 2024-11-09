import sys
input = sys.stdin.readline

n = int(input()) # 목표 고양이 수

if n == 0:
    print(0)
    exit(0)

madoka = 1  # 마도카를 위한 최소의 행동 횟수
cat = 1     # 현재 고양이 수

while cat < n:
    cat *= 2
    madoka += 1

print(madoka)