import math
from collections import defaultdict

N, M, K = map(int, input().split())

# 파이어볼을 나타내는 배열, 순서대로 (x위치, y위치, 질량, 속력, 방향)
fire_balls = []

ans = 0

# 방향을 나타내는 배열
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 파이어볼을 위치별로 묶어두기 위한 딕셔너리
fire_balls_position = defaultdict(list)

# 파이어볼 위치 기록 (위치별 파이어볼 목록)
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_balls.append((r, c, m, s, d))

# K번 만큼 파이어볼 이동
for _ in range(K):
    # 새 위치로 이동한 파이어볼을 임시로 기록
    fire_balls_position.clear()

    for r, c, m, s, d in fire_balls:
        # 파이어볼을 방향과 속력에 따라 이동
        dx, dy = dir[d]
        r = ((r + dx * s - 1) % N) + 1
        c = ((c + dy * s - 1) % N) + 1

        # 새로운 위치에 파이어볼을 추가
        fire_balls_position[(r, c)].append((r, c, m, s, d))

    # 파이어볼 합치기
    fire_balls.clear()
    for (r, c), balls in fire_balls_position.items():
        if len(balls) > 1:  # 한 위치에 2개 이상 파이어볼이 있을 경우
            # 질량, 속력, 방향 계산
            m_sum = sum(ball[2] for ball in balls)
            s_sum = sum(ball[3] for ball in balls)
            count = len(balls)

            # 짝수, 홀수 방향 판별
            flag = -1
            for _, _, _, _, d in balls:
                if flag == -1:
                    flag = d
                elif flag % 2 != d % 2:
                    flag = -10  # 홀수, 짝수 혼합

            # 질량이 0보다 크면 4개로 나눈다
            if m_sum // 5 > 0:
                if flag == -10:
                    fire_balls.extend([(r, c, m_sum // 5, s_sum // count, i) for i in [1, 3, 5, 7]])
                else:
                    fire_balls.extend([(r, c, m_sum // 5, s_sum // count, i) for i in [0, 2, 4, 6]])
        else:
            # 1개일 경우 그대로 남긴다
            fire_balls.extend(balls)

# 결과 출력
ans = sum(m for _, _, m, _, _ in fire_balls)
print(ans)
