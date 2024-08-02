import sys

inp = sys.stdin.readline

arr = inp().split()

n = arr[0]
b = int(arr[1])

ans = 0
i = 1
length = len(n)

for char in n:
    if char >= 'A' and char<='Z':
        ans = ans + pow(b,length - i) * (ord(char) - ord('A') + 10)
    else:
        ans = ans + pow(b,length - i) * int(char)
    i+=1

print(ans)