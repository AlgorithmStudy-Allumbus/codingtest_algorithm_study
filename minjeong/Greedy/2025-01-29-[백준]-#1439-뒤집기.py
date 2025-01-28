import sys
input = sys.stdin.readline

# 문자열 입력
S = input().strip()

# 0과 1 덩어리 개수 저장 변수
count_0 = 0
count_1 = 0

# 첫 번째 숫자가 0이면 count_0 증가, 1이면 count_1 증가
if S[0] == '0':
    count_0 += 1
else:
    count_1 += 1

# 연속된 숫자가 바뀔 때마다 덩어리 개수 증가
for i in range(1, len(S)):
    if S[i] != S[i - 1]:  # 숫자가 바뀌는 순간
        if S[i] == '0':
            count_0 += 1
        else:
            count_1 += 1

# 최소한의 뒤집기 횟수 출력
print(min(count_0, count_1))
