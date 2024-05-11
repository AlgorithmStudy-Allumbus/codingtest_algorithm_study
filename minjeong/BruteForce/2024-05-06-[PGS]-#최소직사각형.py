def solution(sizes):
    widths = []
    heights = []  
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            widths.append(sizes[i][0])
            heights.append(sizes[i][1])
        else:
            widths.append(sizes[i][1])
            heights.append(sizes[i][0])
    answer = max(widths) * max(heights)
    return answer
'''
# 다른 코드 A
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

'''

'''
# 다른 코드 B
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col
'''