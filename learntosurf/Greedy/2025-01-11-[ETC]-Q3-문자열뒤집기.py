import sys 
input = sys.stdin.readline

S = list(input().rstrip())

count_0 = 0 # 0이 연속되는 부분의 개수 
count_1 = 0 # 1이 연속되는 부분의 개수

# 연속된 정수가 다른 정수로 바뀔 때, 연속된 부분의 개수 추가
for i in range(1, len(S)):
    if S[i] != S[i-1]: # 이전 수와 다른 경우
        if S[i-1] == '0': # 이전 수가 0인 경우
            count_0 += 1
        else: # 이전 수가 1인 경우
            count_1 += 1

# 루프에서 처리하지 못한 마지막 숫자 처리
if S[-1] == '0':  # 문자열의 마지막 문자가 0이면
    count_0 += 1
else:             # 문자열의 마지막 문자가 1이면
    count_1 += 1

print(min(count_0, count_1))