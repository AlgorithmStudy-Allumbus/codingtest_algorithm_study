import sys
input = sys.stdin.readline

# 입력
N = int(input())
meetings = [[0, 0] for _ in range(N)]

for i in range(N):
    start, end = map(int, input().split())
    meetings[i][0] = start
    meetings[i][1] = end

# 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같으면 시작 시간을 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0                         # 회의 개수
last_end_time = 0               # 마지막으로 배정된 회의의 종료 시간

for start, end in meetings:
    if start >= last_end_time:  # 현재 회의 시작 시간이 마지막 회의 종료 시간 이후라면
        cnt += 1                # 회의 배정
        last_end_time = end     # 회의 종료 시간 업데이트

print(cnt)