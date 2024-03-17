import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
check = [False] * N
minValue = 1000000000

def calculate():
    global minValue
    Ateam = 0
    Bteam = 0
    for i in range(N):
        for j in range(N):
            if check[i] and check[j]:
                Ateam += S[i][j]
            if not check[i] and not check[j]:
                Bteam += S[i][j]

    minValue = min(minValue, abs(Ateam - Bteam))

def backtracking(start, size):
    global minValue
    if size == N//2:
        calculate()
        return 

    for i in range(start, N):
        if check[i] == False:
            check[i] = True
            backtracking(i+1, size+1)
            check[i] = False


backtracking(0, 0)
print(minValue)