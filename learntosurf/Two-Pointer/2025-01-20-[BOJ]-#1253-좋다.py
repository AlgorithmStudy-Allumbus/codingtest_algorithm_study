import sys
input = sys.stdin.readline

N = int(input())  # 수의 개수
num = list(map(int, input().split()))  # 입력된 숫자 리스트
num.sort()  # 정렬 (투포인터 사용을 위해)

cnt = 0  # 좋은 수의 개수 
for i in range(N):
    goal = num[i]  # 현재 확인할 값
    start = 0
    end = N - 1

    while start < end:  # 두 포인터가 교차할 때까지 반복
        # 현재 두 수의 합이 goal인지 확인
        if num[start] + num[end] == goal:
            if start == i:  # start 포인터가 현재 값(goal)을 가리키면 이동
                start += 1
            elif end == i:  # end 포인터가 현재 값(goal)을 가리키면 이동
                end -= 1
            else:  # 두 수의 합이 goal이면서 현재 값(goal)을 포함하지 않을 때
                cnt += 1
                break
        
        elif num[start] + num[end] > goal:  # 합이 goal보다 크면 큰 값을 줄여야 하므로 end 감소
            end -= 1
        
        else:  # 합이 goal보다 작으면 작은 값을 키워야 하므로 start 증가
            start += 1

print(cnt) 
