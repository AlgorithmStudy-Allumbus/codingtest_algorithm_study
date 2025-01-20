string1 = input()
string2 = input()

dp = [[0] * len(string1) for _ in range(len(string2))]

for i in range(len(string2)):
    for j in range(len(string1)):
        # 두 문자열의 i번째 문자와 j번째 문자가 같을때
        if string2[i] == string1[j]:
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 1
        else:
            dp[i][j] = 0

# dp테이블에서 최댓값 찾기
print(max(max(row) for row in dp))
