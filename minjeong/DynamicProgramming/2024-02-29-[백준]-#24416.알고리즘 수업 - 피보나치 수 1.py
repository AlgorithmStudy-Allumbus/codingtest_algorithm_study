import sys
input = sys.stdin.readline

def fibo(n):
    global f
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[-1]

N = int(input())
f = [0] * (N+1)
ans = fibo(N)
# 코드 1 실행횟수  / 코드 2 실행횟수
print(ans, N-2)
