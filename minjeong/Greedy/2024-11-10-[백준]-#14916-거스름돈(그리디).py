import sys
input = sys.stdin.readline

n = int(input())  # 거스름돈 액수

# 예외처리
if n == 1 or n == 3:
    print(-1)
    exit(0)

# 5로 나누어 떨어질 경우
if n % 5 == 0:
    print(n // 5)

else:
    cnt = 0
    while n > 0:
        if (n >= 5) and ((n - 5) % 5 == 0 or (n - 5) % 2 == 0):
            n -= 5
        else:
            n -= 2

        cnt += 1

    print(cnt)