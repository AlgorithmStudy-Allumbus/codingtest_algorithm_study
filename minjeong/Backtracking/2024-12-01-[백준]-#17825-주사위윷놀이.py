# 게임판 그래프 정의
graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

# 각 칸의 점수
score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]

dice = list(map(int, input().split()))  # 주사위 값 입력
answer = 0  # 최대 점수 저장 변수

# 백트래킹 함수
def backtracking(depth, result, horses):
    global answer
    # 10개의 주사위를 모두 사용한 경우 최대값 갱신
    if depth == 10:
        answer = max(answer, result)
        return

    # 4개의 말을 순서대로 선택해 이동
    for i in range(4):
        x = horses[i]  # 현재 말 위치

        # 파란색 화살표 처리
        if len(graph[x]) == 2:
            x = graph[x][1]
        else:
            x = graph[x][0]

        # 주사위 값만큼 이동
        for _ in range(1, dice[depth]):
            x = graph[x][0]

        # 이동한 위치가 도착 칸이거나, 다른 말이 없는 칸일 때만 이동
        if x == 32 or (x < 32 and x not in horses):
            before = horses[i]  # 원래 위치 저장
            horses[i] = x  # 말 이동
            backtracking(depth + 1, result + score[x], horses)  # 재귀 호출
            horses[i] = before  # 위치 복구

# 백트래킹 시작
backtracking(0, 0, [0, 0, 0, 0])
print(answer)
