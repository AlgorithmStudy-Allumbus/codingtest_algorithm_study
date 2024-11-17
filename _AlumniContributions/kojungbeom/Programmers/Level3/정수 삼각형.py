def solution(triangle):
    answer = 0
    t_length = len(triangle)-1

    for h in range(t_length, 0, -1):
        for i in range(len(triangle[h])-1):
            value = max(triangle[h][i], triangle[h][i+1])
            triangle[h-1][i] += value

    return triangle[0][0]