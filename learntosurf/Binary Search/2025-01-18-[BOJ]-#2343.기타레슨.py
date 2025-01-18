import sys 
input = sys.stdin.readline

N, M = map(int, input().split()) # 강의의 수, 블루레이의 수 
time = list(map(int, input().split())) # 강의의 길이 

# time.sort() # 강의의 순서가 바뀌면 안됨 

# 탐색 대상: 블루레이의 크기 
start = max(time)
end = sum(time) 

while start <= end:
    mid = (start + end) // 2 
    
    total = 0 # 현재 블루레이에 담은 강의 길이  
    count = 1  # 블루레이 개수
    for t in time:
        if total + t > mid: # 블루레이의 크기를 초과하는 경우 
            count += 1 # 블루레이 개수 증가
            total = 0 # 블루레이에 담은 강의 길이 초기화
        total += t # 블루레이에 강의 추가
        
        if count <= M: 
            answer = mid # 가능한 블루레이 크기 저장
            end = mid - 1 
        else: 
            start = mid + 1 

print(answer)