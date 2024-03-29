# 내 풀이 
A, B = map(int, input().split())
C = int(input())

if C < 60:
    if B+C >= 60:
        print((A+1)%24, B+C-60)
    else:
        print(A%24, B+C)
elif C == 60:
    print(A+1, B)
else:
    if B+(C%60) >= 60:
        print((A+(C//60)+1)%24, B+(C%60)-60)
    else:
        print((A+(C//60))%24, B+(C%60))
        
# 다른 풀이 
A, B = map(int, input().split())
C = int(input()) 

A += C // 60
B += C % 60

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print(A,B)