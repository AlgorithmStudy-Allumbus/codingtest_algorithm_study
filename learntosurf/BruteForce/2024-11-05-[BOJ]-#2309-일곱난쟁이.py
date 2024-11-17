import sys 
input = sys.stdin.readline 

heights = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(i + 1, 9):
        if sum(heights) - heights[i] - heights[j] == 100:
            result = [heights[k] for k in range(9) if k != i and k != j]
            result.sort()  
            print(*result, sep='\n')
            exit()
