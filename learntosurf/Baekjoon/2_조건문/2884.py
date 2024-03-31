# 내 풀이 
H, M = map(int, input().split())

if M < 45: 
    H = H - 1
    M = M + 15
    if H < 0:
        H = 23
else:
    M = M - 45

print(H, M)

# 다른 풀이
H,M = map(int,input().split())

if M > 44:
    print(H, M-45)
elif M<45 and H>0:
    print(H-1,M+15)
else:
    print(23,M+15)