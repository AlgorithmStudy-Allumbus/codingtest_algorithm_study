import sys
input = sys.stdin.readline

# 최대공약수를 구하는 함수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# DP 배열 선언 및 초기화
dp = [0 for _ in range(1001)]
dp[1] = 3

# DP 배열 값 채우기
for x in range(2, 1001):
    cnt = 0
    for y in range(1, x):
        if x == y:
            continue
        if gcd(x, y) == 1: # 서로소라면, (x,y)와 (y,x)가 원점에서 보이므로 +2
            cnt += 2
    dp[x] = dp[x - 1] + cnt

# 테스트 케이스 처리
C = int(input()) # 테스트 케이스의 개수
for _ in range(C):
    N = int(input())
    print(dp[N])