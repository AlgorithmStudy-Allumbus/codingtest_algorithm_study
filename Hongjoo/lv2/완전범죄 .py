def solution(info, n, m):
    answer = 0
    #1. dp 테이블 정의
    dp = [[] for _ in range(len(info))]

    if info[0][0] < n: 
        dp[0].append((info[0][0]  , 0))
    if info[0][1]  < m :
        dp[0].append((0, info[0][1]))
    if len(dp[0]) <= 0 :
        return -1
    # print(f" # item 0 : {dp[0]}")
    for i in range(1, len(info)):
        # dp[i][k]
        for cur_a ,cur_b in dp[i-1]:
            # print(f"##cur_a ,cur_b  {cur_a},{cur_b }")
            up_a = cur_a + info[i][0]
            up_b = cur_b + info[i][1]
            if up_a < n: 
                dp[i].append((up_a , cur_b))
            if up_b < m :
                dp[i].append((cur_a , up_b))
            # print(f" # item {i} : {dp[i]}")
        if len(dp[i]) <= 0 :
            return -1
        # print(f" # item {i} : {dp[i]}")
    # A 최소값 반환 
    answer = sorted(dp[-1])[0][0]
    return answer