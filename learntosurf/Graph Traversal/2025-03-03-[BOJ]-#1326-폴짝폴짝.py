import sys 
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [0] + list(map(int, input().split())) # 1-based index 사용
a, b = map(int, input().split())

def bfs(N, arr, a, b):
    queue = deque([(a, 0)]) # (현재 위치, 점프 횟수)
    visited = [False] * (N + 1) # 방문 여부 체크 
    visited[a] = True # 시작점 방문 처리 
    
    while queue:
        pos, jump = queue.popleft()
        
        # 목표 지점에 도달하면 점프 횟수 반환 
        if pos == b:
            return jump
        
        step = arr[pos] # 현재 위치에서 이동할 수 있는 거리
        if step == 0: 
            continue # 이동할 수 없는 경우는 다음 탐색을 진행
        
        # 양방향 탐색 (오른쪽 방향)
        next_pos = pos + step  # 첫 번째 점프
        while next_pos <= N:
            if not visited[next_pos]:  # 방문하지 않은 곳만 탐색
                if next_pos == b:  # 목표 지점에 도달하면 즉시 반환
                    return jump + 1
                visited[next_pos] = True
                queue.append((next_pos, jump + 1))  # 점프 횟수 증가
            next_pos += step  # 다음 배수 위치 탐색

        # 양방향 탐색 (왼쪽 방향)
        next_pos = pos - step  # 왼쪽 방향 점프
        while next_pos >= 1:
            if not visited[next_pos]:  # 방문하지 않은 곳만 탐색
                if next_pos == b:  # 목표 지점에 도달하면 즉시 반환
                    return jump + 1
                visited[next_pos] = True
                queue.append((next_pos, jump + 1))  # 점프 횟수 증가
            next_pos -= step  # 다음 배수 위치 탐색

     
    # 목표 지점에 도달하지 못하면 -1 반환           
    return -1 

print(bfs(N, arr, a, b))