def solution(numbers):
    answer = 0
    permute = set()
    # DFS로 모든 숫자의 케이스를 set에 저장하자
    stack = [([], [0]*len(numbers))] # current list,  visited
    lenN = len(numbers)
    while stack:
        currentT, visited = stack.pop()
        permute.add(tuple(currentT))
        if len(currentT) == lenN:
            continue

        for i in range(lenN):
            if not visited[i]:
                new_cT = currentT[:]
                new_visisted = visited[:]
                new_cT.append(numbers[i])
                new_visisted[i] = True
                stack.append([new_cT, new_visisted])

    temp = []
    new_permute = []
    for p in permute:
        p_str = ''.join(p)
        if p and not p[0] == '0':
            new_permute.append(int(p_str))

    def sosu(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n//2+1):
                if n % i == 0:
                    return False
            return True
    for p in new_permute:
        if sosu(p):
            answer += 1

    return answer


#ChatGPT의 개선안
from itertools import permutations

def solution(numbers):
    answer = 0
    permute = set()
    for i in range(1, len(numbers) + 1):
        permute |= set(map(int, map(''.join, permutations(numbers, i))))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for p in permute:
        if is_prime(p):
            answer += 1

    return answer


def solution(numbers):
    answer = 0
    visited = [False] * len(numbers)
    permute = set()

    def dfs(current):
        nonlocal permute
        if current:
            permute.add(int(''.join(current)))

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(current + [numbers[i]])
                visited[i] = False

    dfs([])

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for p in permute:
        if is_prime(p):
            answer += 1

    return answer