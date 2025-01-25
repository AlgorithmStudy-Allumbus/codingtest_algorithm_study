N = int(input())
arr = list(map(int, input().split()))

arr_sorted = sorted(arr)

answer = 0

for i in range(N):
    start = 0
    end = len(arr_sorted) - 1

    while start < end:
        if arr_sorted[start] + arr_sorted[end] == arr_sorted[i]:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                answer += 1
                break
        elif arr_sorted[start] + arr_sorted[end] > arr_sorted[i]:
            end -= 1
        else:
            start += 1

print(answer)
