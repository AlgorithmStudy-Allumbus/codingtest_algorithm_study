import sys 
input = sys.stdin.readline

steps = list(map(int, input().split()))
if steps: 
    steps.pop()  # 마지막 0 제거

# dp 테이블
INF = float('inf') # 무한대 값 
dp = [[INF]*5 for _ in range(5)]
dp[0][0] = 0

def move_power(start, end):
    if start == 0: # 중앙에서 다른 곳으로 이동하는 경우 
        return 2
    if start == end: # 같은 지점을 연속해서 밟는 경우 
        return 1 
    if abs(start - end) == 2: # 반대편으로 이동하는 경우
        return 4 
    return 3 # 인접한 지점으로 이동하는 경우

for step in steps:
    new_dp = [[INF]*5 for _ in range(5)] # 새로운 dp 테이블
    
    for left in range(5):
        for right in range(5):
            if dp[left][right] == INF:
                continue 
            
            current_power = dp[left][right] # 현재 위치의 힘의 소모량
            
            # 왼발을 움직이는 경우 (오른발이 step에 있으면 안 됨)
            if step != right:
                new_dp[step][right] = min(new_dp[step][right], current_power + move_power(left, step))

            # 오른발을 움직이는 경우 (왼발이 step에 있으면 안 됨)
            if step != left:
                new_dp[left][step] = min(new_dp[left][step], current_power + move_power(right, step))
    
    dp = new_dp # dp 테이블 업데이트

print(min(min(row) for row in dp)) 