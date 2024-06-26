def dfs(graph, start, path):
    while start in graph and graph[start]:  # 시작점이 그래프에 있는지 확인하고, 도착지가 있는지 확인
        next_dest = graph[start].pop(0)  # 알파벳 순으로 정렬되어 있으므로 첫 번째 경로를 선택
        dfs(graph, next_dest, path)  # 재귀적으로 다음 도착지에서 다시 탐색
    path.append(start)  # 더 이상 갈 곳이 없으면 현재 위치를 경로에 추가

def solution(tickets):
    # 그래프 초기화
    graph = {}
    for u, v in tickets:  # 주어진 티켓 정보로 그래프 생성
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]

    # 각 출발지의 도착지 리스트를 알파벳 순으로 정렬 (문제 조건에 있음)
    for key in graph.keys():
        graph[key].sort()

    path = []  # 최종 경로를 저장할 리스트
    dfs(graph, "ICN", path)  # "ICN"에서 무조건 시작해야 함 -> ICN부터 DFS ㅇ탐색
    return path[::-1]  # 경로를 역순으로 반환