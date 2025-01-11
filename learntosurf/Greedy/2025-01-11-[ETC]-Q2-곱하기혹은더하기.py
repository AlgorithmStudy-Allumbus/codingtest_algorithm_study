import sys 
input = sys.stdin.readline

S = list(map(int, input().rstrip()))

num = S[0] # 첫번째 정수를 초기 결과값으로 지정 

for i in range(1, len(S)):
    # 해당 정수가 1 이하이거나, 초기 결과값이 1 이하일 경우 
    if S[i] <= 1 or num <= 1:
        num += S[i] # 덧셈
    # 해당 정수가 2 이상을 경우 
    else:
        num *= S[i] # 곱셈

print(num)