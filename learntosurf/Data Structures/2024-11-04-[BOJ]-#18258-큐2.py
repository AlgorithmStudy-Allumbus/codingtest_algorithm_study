import sys
from collections import deque
input = sys.stdin.read
output = sys.stdout.write

def queue_operations(N, data):
    queue = deque()
    results = []
    
    for i in range(1, N+1):
        command = data[i].split()
        
        if command[0] == 'push':
            X = int(command[1])
            queue.append(X)
        elif command[0] == 'pop':
            if queue:
                results.append(str(queue.popleft()))
            else:
                results.append('-1')
        elif command[0] == 'size':
            results.append(str(len(queue)))
        elif command[0] == 'empty':
            results.append('1' if not queue else '0')
        elif command[0] == 'front':
            if queue: 
                results.append(str(queue[0]))
            else:
                results.append('-1')
        elif command[0] == 'back':
            if queue:
                results.append(str(queue[-1]))
            else:
                results.append('-1')
        
    output("\n".join(results) + "\n")

data = input().splitlines()
N = int(data[0])
queue_operations(N, data)