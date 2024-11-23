import sys
from collections import deque

input = sys.stdin.readline

'''
1. 일반적인 위상정렬 구현
2. 예외조건 추가 : 일관성이 없는 정보일 경우(IMPOSSIBEL) / 발표된 정보만 가지고 확실한 순위를 만들 수 없는 경우(?)
'''

t = int(input())    # 테스트케이스 개수
for _ in range(t):
    # 각 테스트 케이스에 대해 팀의 수와 작년 순위 정보를 입력받음
    n = int(input())  # 팀의 수
    info = list(map(int, input().split()))  # 작년에 i등한 순서 정보

    # 초기 그래프와 진입차수 초기화
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)  # 진입차수 0으로 초기화

    # 작년 순위 정보를 바탕으로 그래프 생성
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            graph[i].append(info[j - 1])
            indegree[info[j - 1]] += 1

    # 순위가 변경된 팀 쌍의 수
    m = int(input())  # 상대적인 등수가 바뀐 쌍의 수 m
    for _ in range(m):
        a, b = map(int, input().split()) # 순위가 변경된 두 팀

        # 간선 방향을 바꾸기 위한 처리
        a_idx = info.index(a) + 1
        b_idx = info.index(b) + 1

        # 기존에 b가 a보다 뒤에 있는 경우: 간선을 제거하고 새 순서로 간선 추가
        if a in graph[b_idx]:
            # 더 높았던 순위에서 제거
            graph[b_idx].remove(a)
            indegree[b] += 1
            # 새로 갱신된 순위 반영
            graph[a_idx].append(b)
            indegree[a] -= 1
        else:  # 반대 경우: 간선 방향을 다시 바꿔야 하는 경우
            graph[a_idx].remove(b)
            indegree[b] -= 1
            graph[b_idx].append(a)
            indegree[a] += 1


    # 위상 정렬 수행
    def topology_sort():
        ranking = []  # 최종 순위를 저장할 리스트
        queue = deque()

        # 큐에 진입차수가 0인 팀(노드)을 모두 추가
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        # 진입 차수가 0인 정점이 없어 큐가 비어 있다면, 순위를 결정할 수 없다는 의미로 "IMPOSSIBLE" 출력
        if not queue:
            print("IMPOSSIBLE")
            return

        able = True  # 순위 결정 가능 여부

        # 큐가 빌 때까지 반복
        while queue:
            # 큐에서 노드를 꺼내고 최종 순위에 추가
            now = queue.popleft()
            ranking.append(now)

            # 해당 노드와 연결된 다른 노드들의 진입차수를 1씩 감소
            for i in graph[info.index(now) + 1]:
                indegree[i] -= 1
                # 진입차수가 0이 된 노드를 큐에 삽입
                if indegree[i] == 0:
                    queue.append(i)
                # 진입차수가 음수가 되는 경우는 잘못된 정보로 간주
                elif indegree[i] < 0:
                    able = False
                    break

        # 출력 조건을 확인하여 결과 출력
        if not able or n != len(ranking):  # 전체 노드 개수와 결과의 노드 개수가 다를 경우
            print("IMPOSSIBLE")
        else:
            # 확실한 순서가 결정된 경우 순위를 출력
            print(" ".join(map(str, ranking)))

    topology_sort()