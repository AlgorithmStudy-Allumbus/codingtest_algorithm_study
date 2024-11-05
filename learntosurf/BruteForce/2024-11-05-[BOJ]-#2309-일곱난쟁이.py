import sys 
input = sys.stdin.readline 

# 9개의 정수를 한번에 받는다 
heights = [int(input()) for _ in range(9)]

# 9개의 정수 중 7개를 뽑는다
for i in range(9):
    for j in range(i+1, 9):
        if sum(heights) - heights[i] - heights[j] == 100:
            heights.remove(heights[i])
            heights.remove(heights[j])

heights.sort()
print(*heights, sep='\n')