import sys 
input = sys.stdin.readline
from itertools import permutations

N = int(input().strip()) # 질문 횟수 
questions = [list(map(int, input().split())) for _ in range(N)] # 질문 리스트

# 1부터 9까지의 숫자 중 3개를 뽑는 순열
nums = list(permutations(range(1,10), 3)) 
cnt = 0 # 가능한 경우의 수

# 두 수를 비교하여 스트라이크와 볼을 반환
def strike_and_ball(num1, num2):
    strike = sum(a == b for a, b in zip(num1, num2))
    ball = sum(a in num2 for a in num1) - strike
    return strike, ball 
    
for num in nums:
    num_str = ''.join(map(str, num)) # 순열을 문자열로 변환
    valid = True # 가능한 숫자인지 판별
    
    for q_num, q_strike, q_ball in questions:
        q_str = str(q_num) # 입력된 숫자도 문자열 변환 
        strike, ball = strike_and_ball(num_str, q_str)
        if strike != q_strike or ball != q_ball:
            valid = False
            break  # 하나라도 불가능하면 더 볼 필요 없음
    
    if valid:
        cnt += 1

print(cnt)
        