# 2644-촌수계산. DFS(백트래킹) 풀이
import sys

input = sys.stdin.readline

n = int(input())                    # 전체 사람 수
a, b = map(int, input().split())    # 촌수 계산해야 하는 두 사람의 번호
m = int(input())                    # 부모 자식들간의 관계의 개수
graph = [[] for _ in range(n + 1)]  # 그래프
visited = [False for _ in range(n + 1)]  # 방문여부
for _ in range(m):
    x, y = map(int, input().split())
    # 그래프 연결
    graph[x].append(y)
    graph[y].append(x)

result = -1  # 기본값은 -1로 설정하여 찾지 못한 경우에 대비

def backtracking(v, level):
    global result
    # 재귀함수 마치는 조건: a,b 촌수를 계산이 되었을 때
    if v == b:
        result = level
        return

    # 탐색
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            backtracking(i, level + 1)  # 자식 노드 방문 level + 1을 넘겨줌으로써 촌수 계산
            visited[i] = False          # 방문했다면 부모노드 다시 방문 기록 지움


visited[a] = True # 초기 노드 방문 체크
backtracking(a, 0)
print(result)