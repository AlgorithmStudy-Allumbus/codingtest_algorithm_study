N = int(input())


for i in range(1, N+1):
    answer = i + sum((map(int, str(i))))
    if answer == N: 
        print(i)
        break 
    if i == N: # 생성자가 없는 경우 
        print(0)