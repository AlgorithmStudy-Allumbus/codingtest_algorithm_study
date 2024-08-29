import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    number = input().strip()
    cnt = 0
    while number != '6174':
        # 최대, 최소 숫자 계산
        max_num = int(''.join(sorted(number, reverse=True)))
        min_num = int(''.join(sorted(number)))

        # Kaprekar 연산
        number = f'{(max_num - min_num):04d}'
        cnt += 1
    print(cnt)