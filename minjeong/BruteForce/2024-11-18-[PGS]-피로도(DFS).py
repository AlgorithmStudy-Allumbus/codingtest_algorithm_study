answer = 0
n = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    # 최대 탐험 횟수 갱신
    if cnt > answer:
        answer = cnt

    # 각 던전에 대해 탐험 시도
    for i in range(n):
        if k >= dungeons[i][0] and not visited[i]:  # 최소 필요 피로도 조건 만족
            visited[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons)  # 탐험
            visited[i] = 0  # 상태 복구 (백트래킹)


def solution(k, dungeons):
    global n, visited
    n = len(dungeons)  # 던전 개수
    visited = [0] * n  # 방문 여부 초기화
    dfs(k, 0, dungeons)
    return answer
