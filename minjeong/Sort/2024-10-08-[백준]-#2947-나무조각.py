import sys
input = sys.stdin.readline

li = list(map(int, input().split()))

while li != [1, 2, 3, 4, 5]:  # 최종적으로 1, 2, 3, 4, 5가 될 때까지 반복
    for i in range(4):  # 0번 인덱스부터 3번 인덱스까지 인접한 두 조각 비교
        if li[i] > li[i + 1]:  # 앞의 조각이 뒤의 조각보다 크면 교환
            li[i], li[i + 1] = li[i + 1], li[i]
            print(' '.join(map(str, li)))  # 교환이 발생할 때마다 출력
