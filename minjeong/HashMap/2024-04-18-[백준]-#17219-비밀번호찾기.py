n, m = map(int, input().split()) # n: 저장된 사이트 수, m: 비밀번호를 찾으려는 사이트의 수
password = {} # 비밀번호 딕셔너리 선언

# 저장된 사이트의 수
for _ in range(n):
    site, pw = map(str, input().split())
    password[site] = pw # 사이트에 대한 비밀번호 저장

# 비밀번호를 찾으려는 사이트
for _ in range(m):
    search = input()
    print(password[search])