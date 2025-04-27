import sys

def backtrack(S, path, start):
    if len(path) == 6:
        print(' '.join(map(str, path)))
        return
    for i in range(start, len(S)):
        path.append(S[i])
        backtrack(S, path, i + 1)
        path.pop()

lines = sys.stdin.read().splitlines()
first_case = True

for line in lines:
    if line == '0':
        break

    parts = list(map(int, line.strip().split()))
    S = parts[1:]

    if not first_case:
        print()
    first_case = False

    backtrack(S, [], 0)