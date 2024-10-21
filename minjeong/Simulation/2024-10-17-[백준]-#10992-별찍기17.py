n = int(input())
if n == 1:
    print("*")
    exit()

# 첫번째 줄
print(" " * (n-1) + "*")

# 가운데 줄
for i in range(1, n-1):
    print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")

# 마지막 줄
print("*"*(2*n-1))

'''
n = int(input())
for i in range(1, n+1):
    if(i==1 or i==n):
        print(" " * (n-i) + "*" * (2*i-1))
    else:
        print(" " * (n-i) + "*" + " " * (2*(i-1)-1) + "*")
'''