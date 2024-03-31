def solution(sticker):
    if len(sticker) == 1:
        return sticker.pop()
    
    size = len(sticker)
    # 1번 선택하는 경우 -> 1..n-1번 배열에 대한 DP
    dp1 = [0] + sticker[:-1]
    for i in range(2, size):
        dp1[i] = max(dp1[i-1], dp1[i-2] + dp1[i])
    
    # 2번 선택하는 경우 -> 2...n번 배열에 대한 DP
    dp2 = [0] + sticker[1:]
    for i in range(2, size):
        dp2[i] = max(dp2[i-1], dp2[i-2] + dp2[i])
        
    answer = max(dp1[-1], dp2[-1])
    return answer
    