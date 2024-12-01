import sys

input = sys.stdin.readline
N = int(input())  # 전체 인원

status = [list(map(int, input().split())) for _ in range(N)]  # 능력치

visited = [False] * N
result = sys.maxsize  # 결과 큰 수로 초기화


def dfs(a, idx):
    global result

    if a == N // 2:  # 반반으로 나뉘었을 경우

        # 각 팀의 능력치 초기화
        team_start = 0
        team_link = 0

        for i in range(N):
            for j in range(N):

                # 방문한 반을 start 팀으로 배정
                if visited[i] and visited[j]:
                    team_start += status[i][j]

                # 방문하지 않은 반을 link 팀으로 배정
                elif not visited[i] and not visited[j]:
                    team_link += status[i][j]

        result = min(result, abs(team_start - team_link))
        return

    else:  # 인원 나누기
        for i in range(idx, N):
            if not visited[i]:
                visited[i] = True
                dfs(a + 1, i + 1)
                visited[i] = False


dfs(0, 0)
print(result)