T = int(input())
result = []

for _ in range(T):
    # 출발점 도착점
    x1, y1, x2, y2 = list(map(int, input().split()))
    # 행성계의 개수
    n = int(input())
    count = 0
    for _ in range(n):
        cx, cy, cr = map(int, input().split())
        dis1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        dis2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        pow_cr = cr ** 2

        if pow_cr > dis1 and pow_cr > dis2:
            pass
        elif pow_cr > dis1:
            count += 1
        elif pow_cr > dis2:
            count += 1
    result.append(count)

for i in result:
    print(i, end="\n")