import sys
input = sys.stdin.readline

n = int(input())
meetings = [[0,0] for _ in range(n)]

for i in range(n):
    start, end = map(int, input().strip().split())
    meetings[i][0] = start
    meetings[i][1] = end

# 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같으면 시작 시간을 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last_end_time = 0

for start, end in meetings:
    if start >= last_end_time:
        cnt += 1
        last_end_time = end
    
print(cnt)