import sys
input = sys.stdin.readline

n = int(input())
answer = []

limit = 10 ** (len(str(n)) // 2 + 1) # 반복 범위 설정 (n의 자릿수의 절반에서 1을 더한 값을 10의 지수)

# 회문수를 생성하여 n과 비교
for i in range(1, limit):
    half = str(i)

    # 짝수 자리수 회문수
    p_even = int(half + half[::-1])
    if p_even <= n:
        answer.append(p_even)

    # 홀수 자리수 회문수
    p_odd = int(half + half[-2::-1])
    if p_odd <= n:
        answer.append(p_odd)

print(len(answer))