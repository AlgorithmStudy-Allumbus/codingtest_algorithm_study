import sys
input = sys.stdin.read # 한 번에 모든 입력을 읽어옴
output = sys.stdout.write 

def stack_operations(N, data): 
    stack = []  
    results = [] 
    
    for i in range(1, N+1):
        command = data[i].split() # 명령어를 공백을 기준으로 나눠서 리스트로 저장
        
        if command[0] == '1':
            X = int(command[1])
            stack.append(X)
        elif command[0] == '2':
            if stack:
                results.append(str(stack.pop()))
            else:
                results.append('-1')
        elif command[0] == '3':
            results.append(str(len(stack)))
        elif command[0] == '4':
            results.append('1' if not stack else '0')
        elif command[0] == '5':
            if stack:
                results.append(str(stack[-1]))
            else:
                results.append('-1')
    
    output("\n".join(results) + "\n")
    
data = input().splitlines() # 입력을 줄 단위로 나눠서 리스트로 저장
N = int(data[0])
stack_operations(N, data)