import sys
input = sys.stdin.readline

N = input().strip()

# 0이 없으면 무조건 불가능 / 3의 배수인지 확인 (자리수 합이 3의 배수여야 함)
if '0' not in N or sum(map(int, N)) % 3 != 0:
    print(-1)
    exit()

# 가장 큰 수 출력
print(''.join(sorted(N, reverse=True)))