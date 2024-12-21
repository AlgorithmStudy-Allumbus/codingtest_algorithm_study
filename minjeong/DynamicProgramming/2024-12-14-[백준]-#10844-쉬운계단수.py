n = int(input())

num = [[0]*10 for _ in range(n+1)]
num[0] = [1,1,1,1,1,1,1,1,0] #0행에 들어가는 값들을 계단수의 경우의수로 초기화

for i in range(1,n+1):
    for j in range(10): #0일때, 9일때, 나머지인 경우를 점화식을 토대로 코드 작성
        if j == 0:
            num[i][j] = num[i-1][1]
        elif j == 9:
            num[i][j] = num[i-1][8]
        else:
            num[i][j] = num[i-1][j-1] + num[i-1][j]

answer = sum(num[n]) % 100000000
print(answer)