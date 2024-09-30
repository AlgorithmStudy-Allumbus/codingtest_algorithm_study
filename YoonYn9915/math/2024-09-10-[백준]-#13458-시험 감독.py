
N = int(input())

arr = list(map(int,input().split()))

B,C = map(int,input().split())

answer = 0

for i in range(N):
    arr[i] = arr[i] - B
    answer += 1
    if arr[i] <= 0:
        continue

    answer += arr[i] // C
    if arr[i] % C != 0:
        answer += 1


print(answer)