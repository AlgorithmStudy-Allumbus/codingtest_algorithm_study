n = int(input())
origin = [int(n) for n in input().split()]  # 4,1,5,2,3
m = int(input())
compare = [int(m) for m in input().split()]  # 1,3,7,9,5

origin.sort()  # 1,2,3,4,5

for i in range(m):  #
    tag = False
    low = 0
    high = len(origin) - 1
    target = compare[i]  # 5
    while low <= high:
        mid = (low + high) // 2
        if origin[mid] == target:
            tag = True
            print(1)
            break
        elif origin[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    if tag is False:
        print(0)