

n = int(input())

arr = [-1] * 1000001

arr[1] = 0
arr[2] = 1
arr[3] = 1

for i in range(4, n + 1):

    arr[i] = arr[i - 1] + 1

    if i % 3 == 0:
        if arr[i//3] + 1 < arr[i]:
            arr[i] = arr[i//3] + 1
    if i % 2 == 0:
        if arr[i//2] + 1 < arr[i]:
            arr[i] = arr[i//2] + 1


print(arr[n])
