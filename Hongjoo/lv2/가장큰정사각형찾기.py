"""
유형 : DP
IDEA : dp(i,j)의 값에 만들 수 있는 정사각형 최대 길이로 할당하기
FLOW 
- if board[i][j] == 1 이면
    -> dp[i,j] = min( (i-1,j), (i,j-1) , (i-1,j-1)) + 1 대입
"""
def solution(board):
    answer = 0
    dp = [[0]*len(board[0]) for _ in range(len(board))]
    #1. 반복문으로 board[i,j] 찾기
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1 :  
            #2. dp로 (i,j)을 정사각형 오른쪽 아래 칸으로 가지는 최대 변의 길이 구하기
                if 0<=i-1<=len(board) and 0<=j-1 < len(board[0]):
                    dp[i][j] = min(dp[i-1][j] , dp[i][j-1] , dp[i-1][j-1]) +1 
                    # print(dp[i][j])
                    
                else :
                    dp[i][j] = 1
                answer= max(answer , dp[i][j])
                
    # print(dp)
    # print(answer)
    return answer**2