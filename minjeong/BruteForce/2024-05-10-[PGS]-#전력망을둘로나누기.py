def dfs(start, graph, visited, check_link):
    cnt = 1
    visited[start] = True     # 방문 체크
    for v in graph[start]:  # v에 연결되어 있는 다른 노드 탐색.
        if visited[v] == False and check_link[start][v] == True: 
            # 연결되어 있지만 방문한 적 없다면 -> DFS 호출하고, 반환값을 cnt에 누적해서 더함
            cnt += dfs(v, graph, visited, check_link) 
    return cnt
    
def solution(n, wires):
    answer = float("inf")                           # answer 초기화
    check_link = [[True]*(n+1) for _ in range(n+1)] # 끊은 간선인지 아닌지 체크하는 용도
    graph = [[] for _ in range(n+1)]                # 송전탑 그래프
    
    # 그래프 연결
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    # 전력망 나누기
    for a, b in wires:
        # 1. 간선 정보를 확인하면서 a, b 그룹에 연결된 송전탑 개수를 세기 위해서 a에서 b로 가는 간선을 끊어본다.
        visited = [False] * (n+1) 
        check_link[a][b] = False                   # 양망향 연결 끊기
        # 2. a와 b에 붙어있는 송전탑 개수
        cnt_a = dfs(a, graph, visited, check_link) # a랑 붙어있는 송전탑 개수
        cnt_b = dfs(b, graph, visited, check_link) # b랑 붙어있는 송전탑 개수
        check_link[a][b] = True
        
        answer = min(answer, abs(cnt_a - cnt_b)) # 송전탑 개수의 차이(절대값) 가장 작은 걸로 저장함
        
    return answer 