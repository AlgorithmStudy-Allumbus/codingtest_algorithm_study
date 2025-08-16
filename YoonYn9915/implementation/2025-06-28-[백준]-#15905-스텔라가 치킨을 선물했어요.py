N = int(input())

arr = []

for _ in range(N):
    q, p = list(map(int, input().split()))
    arr.append([q, p])

arr.sort(reverse=True)

count = 0
for i in range(5, len(arr)):
    if arr[4][0] == arr[i][0]:
        count += 1
    else:
        break

print(count)