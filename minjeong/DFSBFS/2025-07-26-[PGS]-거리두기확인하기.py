def solution(places):
    def is_safe(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] != 'P':
                    continue

                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if not (0 <= ni < 5 and 0 <= nj < 5):
                        continue
                    if place[ni][nj] != 'P':
                        continue

                    dist = abs(dx) + abs(dy)
                    if dist == 1:
                        return 0  # 거리 1에서 바로 P면 위반
                    elif dist == 2:
                        # 파티션 여부 확인
                        if dx == 0:  # 수평
                            if place[i][j + dy // 2] != 'X':
                                return 0
                        elif dy == 0:  # 수직
                            if place[i + dx // 2][j] != 'X':
                                return 0
                        else:  # 대각선
                            if place[i][nj] != 'X' or place[ni][j] != 'X':
                                return 0
        return 1

    dirs = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # 거리 1
        (-2, 0), (2, 0), (0, -2), (0, 2),  # 일직선 거리 2
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # 대각선 거리 2
    ]

    answer = []
    for place in places:
        answer.append(is_safe(place))

    return answer
