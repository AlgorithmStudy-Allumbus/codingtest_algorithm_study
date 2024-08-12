import sys
input = sys.stdin.readline

n = int(input())    # 열의 개수
cipher_txt = input().strip() # 암호화 된 문자
rows = len(cipher_txt) // n # 행의 개수

# 리스트에 채워넣기
arr = []
for i in range(rows):
    if i % 2 == 0: # 왼 -> 오
        arr.append(cipher_txt[i*n:(i+1)*n])
    else: # 오 -> 왼
        arr.append(cipher_txt[i*n:(i+1)*n][::-1])

# 원래의 문자열 복원
original = ""
for i in range(n):
    for j in range(rows):
        original += arr[j][i]
print(original)