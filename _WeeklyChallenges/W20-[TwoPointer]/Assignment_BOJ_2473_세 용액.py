N = int(input())
sol = list(map(int, input().split()))
sol.sort()

result = [1000000000, 1000000000, 1000000000]
for k in range(N):
    i = k + 1
    j = N - 1
    while i < j:
        if abs(sol[i] + sol[j] + sol[k]) < abs(sum(result)):
            result = [sol[k], sol[i], sol[j]]

        if sol[i] + sol[j] + sol[k] > 0:
            j -= 1
        elif sol[i] + sol[j] + sol[k] < 0:
            i += 1
        else:
            break

print(*result)