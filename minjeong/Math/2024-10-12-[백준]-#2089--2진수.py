import sys
input = sys.stdin.readline

n = int(input()) # 10진수
result = '' # -2진법 숫자를 저장할 문자열

# 예외처리 / 0인 경우 바로 종료
if n == 0:
    print(0)
    exit()

# n이 0이 될 때까지 반복
while n != 0:
    if n % (-2) == 0:
        result += '0'
        n //= (-2)
    else:
        result += '1'
        n = n // (-2) + 1

print(result[::-1])