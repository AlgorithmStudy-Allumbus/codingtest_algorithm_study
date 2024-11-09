N, M = map(int, input().split())

rect = [[input() for _ in range(M)] for _ in range(N)]
square = []
for k in range(1, min(N, M)):
    for i in range(N):
        for j in range(M):
            if rect[i][j] == rect[i][j+k] == rect[i+k][j] == rect[i+k][j+k]:
                square.append((k+1)**2)
                exit()

print(max(square))