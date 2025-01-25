import sys 
input = sys.stdin.readline

T = int(input()) # 테스트케이스의 개수 

for _ in range(T):
    # 수첩1
    N = int(input()) 
    note1 = set(map(int, input().split()))
    # 수첩2
    M = int(input()) 
    note2 = list(map(int, input().split())) 

    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)
    
