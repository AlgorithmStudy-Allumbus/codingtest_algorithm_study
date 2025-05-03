N, M = map(int, input().split())
visited = [False] * (N + 1)  # 1부터 N까지 사용 여부
result = []

def backtrack():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtrack()
            result.pop()         # 상태 복원
            visited[i] = False   # 방문 초기화

backtrack()