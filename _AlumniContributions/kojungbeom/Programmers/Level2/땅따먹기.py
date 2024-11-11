def solution(land):

    for i in range(1,len(land)):
        for j in range(len(land[0])):
            # j, 즉 이전 row에서 선택한 열을 제외한 row를 생성
            # 한 row의 모든 열에 대해서 똑같은 작업을 진행
            row = land[i-1][:j] + land[i-1][j+1:]
            land[i][j] += max(row)

    return max(land[len(land)-1])