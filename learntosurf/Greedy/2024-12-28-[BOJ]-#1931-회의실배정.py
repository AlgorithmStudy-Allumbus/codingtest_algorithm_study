import sys 
input = sys.stdin.readline

N = int(input())
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 종료 시간 오름차순 정렬, 종료 시간이 같다면 시작 시간 오름차순 정렬 
meetings.sort(key=lambda x: (x[1], x[0]))

time = 0 # 현재 시점 (마지막으로 회의가 끝난 시간)
answer = 0 # 배정된 회의 개수 

for meeting in meetings: 
    if time <= meeting[0]: # 현재 회의의 시작 시간이 마지막 종료 시간 이후라면 
        time = meeting[1] # 종료 시간을 갱신 
        answer += 1 # 회의 개수 증가 
        
print(answer)