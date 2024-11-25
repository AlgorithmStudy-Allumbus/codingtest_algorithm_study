N = int(input())

for i in range(N):
    num = int(input())

    arr = [[-1] * num for _ in range(num)]
    val = 1

    row = 0
    col = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dir = 3

    while True:

        if val > num * num:
            break

        arr[row][col] = val
        val += 1

        newRow = row + dx[dir]
        newCol = col + dy[dir]

        if newRow >= num or newRow < 0 or newCol >= num or newCol < 0 or arr[newRow][newCol] != -1:
            if dir == 0:
                dir = 3
            elif dir == 1:
                dir = 2
            elif dir == 2:
                dir = 0
            elif dir == 3:
                dir = 1

            row = row + dx[dir]
            col = col + dy[dir]
        else:
            row = newRow
            col = newCol

    print(f"#{i+1}")
    for j in range(num):
        for k in range(num):
            print(arr[j][k], end=" ")
        print()
