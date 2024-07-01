# 내 풀이
n = int(input())

sum = 0 
for i in range(1, n+1):
    sum += i 
print(sum)

# 다른 풀이 
n = int(input())

print(sum(range(1, n+1)))