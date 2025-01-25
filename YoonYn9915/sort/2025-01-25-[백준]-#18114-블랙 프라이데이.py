from collections import deque

N, C = map(int, input().split())

arr = [0]
arr = arr + list(map(int, input().split()))
flag = 0

arr.sort()


def binary_search(start, end, diff):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == diff:
            return 1
        elif arr[mid] > diff:
            end = mid - 1
        else:
            start = mid + 1
    return 0


start = 0
end = len(arr) - 1

if C in arr:
    print(1)
    exit(0)

while start < end:
    arr_sum = arr[start] + arr[end]
    if arr_sum > C:
        end -= 1
    elif arr_sum == C:
        flag = 1
        break
    elif arr_sum < C:
        diff = C - arr_sum
        if diff != arr[start] and diff != arr[end] and binary_search(start, end, diff) == 1:
            flag = 1
            break
        start += 1

if flag == 1:
    print(1)
else:
    print(0)
