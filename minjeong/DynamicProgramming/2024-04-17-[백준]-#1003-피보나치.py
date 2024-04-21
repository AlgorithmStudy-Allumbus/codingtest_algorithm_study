TC = int(input())
dp = [[0, 0]] * 100 
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 100): # 미리 DP에 저장해두기 (0.25초의 속도를 위함)
    dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]

for _ in range(TC): # 테스트케이스 수만큼 반복
    n = int(input()) # 테스트케이스 n
    print(' '.join(map(str, dp[n]))) # dp에 저장된 값 출력