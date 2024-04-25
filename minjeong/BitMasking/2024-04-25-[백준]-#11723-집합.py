import sys
input = sys.stdin.readline

m = int(input()) # 수행해야 하는 연산의 수
s = 0 # 비어있는 초기 공집합 S
for _ in range(m):
    command = list(map(str, input().strip().split())) # 수행해야 하는 연산 -> all과 empty가 있으므로 리스트로 저장
    # 따라서 command[0]: 연산내용 command[1]: 요소
    if command[0] == 'add':         # 원소 추가 (or)
        s |= (1 << int(command[1]))
    elif command[0] == 'remove':    # 원소 삭제 (not + and)
        s &= ~(1 << int(command[1]))
    elif command[0] == 'check':     # 원소 체크
        if s & (1<< int(command[1])):
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':    # 원소 토글 (xor)
        s ^= (1 << int(command[1]))
    elif command[0] == 'all':       # 원소 채우기
        s = (1 << 21) - 1           
    elif command[0] == 'empty':     #원소 비우기
        s = 0