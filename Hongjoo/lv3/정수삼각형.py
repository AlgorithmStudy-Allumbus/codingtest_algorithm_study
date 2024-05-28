def solution(triangle):

    # 2지 선다 -> A>B , 이면 A 선택

    sum = [[triangle[0][0]]]
    tmp = triangle[0][0]
    sum.append([tmp+triangle[1][0],tmp+triangle[1][1]]) 

    # 중간
    for i in range(2,len(triangle)) : # ith stage: 2~n 
         # s(left) vs s+1(right)
        # 맨 왼쪽
        sub_s = []
        sub_s.append(sum[i-1][0]+triangle[i][0]) 
        ## 중간
        for j in range(1,len(triangle[i])-1):
            tmp = triangle[i][j] + max(sum[i-1][j-1],sum[i-1][j]) 
            #현재 number + 이전 stage number 선택

            sub_s.append(tmp)
        #맨 오른쪽
        sub_s.append(sum[i-1][-1]+triangle[i][-1]) 
        sum.append(sub_s)

    return max(sum[-1])