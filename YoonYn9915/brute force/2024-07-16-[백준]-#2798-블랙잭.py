
n,m = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort(reverse=True)
num = 3

result = m
answer = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k] <= m:
                answer = max(answer,arr[i]+arr[j]+arr[k])
                break

print(answer)
