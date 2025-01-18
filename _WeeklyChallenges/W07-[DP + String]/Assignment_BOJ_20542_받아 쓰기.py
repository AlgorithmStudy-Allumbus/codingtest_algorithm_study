'''
BOJ #20542. 받아 쓰기 (골드3)
https://www.acmicpc.net/problem/20542
유형: Dynamic Programming(DP), 문자열
'''

N, M = map(int, input().split())
inp = input()
answer = input()

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(M + 1):

        if i == 0 or j == 0:
            if i == 0 and j == 0:
                continue
            # 빈 문자열에서 정답 문자열을 만드는 최소 편집 거리
            if i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] + 1
            # 빈 문자열에서 답안 문자열을 만드는 최소 편집 거리
            if i != 0 and j == 0:
                dp[i][j] = dp[i - 1][j] + 1
        else:
            # 비교 문자가 같은지 아닌지 판단
            if inp[i-1] == answer[j-1]:
                # 같으면 좌상단 대각선 값을 그대로 가져옴
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 비교 문자가 달라도 i나 v를 휘갈겨 쓴 경우
                if inp[i-1] == 'i':
                    if answer[j-1] == 'l' or answer[j-1] == 'j':
                        dp[i][j] = dp[i - 1][j - 1]
                        continue
                elif inp[i-1] == 'v':
                    if answer[j-1] == 'w':
                        dp[i][j] = dp[i - 1][j - 1]
                        continue
                        
                # 비교문자가 다른 경우 위, 좌측, 좌상단 대각선 값 중 최소값을 선택한 후 1을 더해준다.
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

print(dp[N][M])
