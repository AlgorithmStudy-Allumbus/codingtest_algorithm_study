import sys
input = sys.stdin.readline

str_A = input().strip()
str_B = input().strip()
LCS = [[0 for j in range(len(str_B)+1)] for i in range(len(str_A)+1)] #LCS 배열 초기화

for i in range(1, len(str_A)+1):
    for j in range(1, len(str_B)+1):
        # 한 글자씩 비교
        if str_A[i-1] == str_B[j-1]:  # 같으면 이전 값에 +1
            LCS[i][j] = LCS[i-1][j-1] + 1
        else: # 다르다면 A 부분수열과 B 부분수열 중 더 큰 값을 선택
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]) 

print(max(max(LCS))) # LCS 배열에서 가장 큰 값을 리턴