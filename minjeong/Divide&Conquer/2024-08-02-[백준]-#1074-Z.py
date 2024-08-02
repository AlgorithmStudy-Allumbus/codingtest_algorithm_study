import sys
input = sys.stdin.readline

def z_order(N, r, c):
    if N == 0:  # Base case: 크기가 1x1인 경우
        return 0
    half = 2 ** (N - 1)
    if r < half and c < half:  # 1사분면
        return z_order(N - 1, r, c)
    elif r < half and c >= half:  # 2사분면
        return half * half + z_order(N - 1, r, c - half)
    elif r >= half and c < half:  # 3사분면
        return 2 * half * half + z_order(N - 1, r - half, c)
    else:  # 4사분면
        return 3 * half * half + z_order(N - 1, r - half, c - half)

N, r, c = map(int, input().split())
print(z_order(N, r, c))