import sys
input = sys.stdin.readline

X = input()

if X[0] == '0':
    if X[1] == 'x': # 16진수
        answer = int(f'0x{X[2:]}', 16)
    else : # 8진수
        answer = int(f'0o{X[1:]}', 8)
else: # 10진수
    answer = int(X)

print(answer)