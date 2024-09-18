'''
양 모은 수보다 늑대의 수가 같거나 많아지면 종료됨
부모 노드는 방문했지만 자식 노드는 방문하지 않았을 때 방문할 수 있음

'''


def solution(info, edges):
    # info - 0: 양, 1: 늑대
    global answer
    answer = 0
    visited = [False] * len(info)
    visited[0] = True  # 0번 노드는 항상 양이 있음

    def dfs(sheep, wolf):
        global answer

        if wolf < sheep:  # 양이 늑대보다 더 많으면 모을 수 있는 최대 양 마리 수 업데이트
            answer = max(answer, sheep)
        else:  # 늑대가 양의 수와 같거나 더 많을 경우 종료됨
            return

        for parent, child in edges:
            # 부모 노드는 방문했지만 자식 노드는 방문하지 않았을 때
            if visited[parent] and not visited[child]:
                visited[child] = True
                if info[child] == 0:  # 양이라면 양 마리 수 + 1
                    dfs(sheep + 1, wolf)
                else:  # 늑대라면 늑대 마리 수 + 1
                    dfs(sheep, wolf + 1)
                visited[child] = False

    dfs(1, 0)  # (sheep, wolf)

    return answer