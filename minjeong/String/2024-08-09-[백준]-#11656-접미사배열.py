import sys
input = sys.stdin.readline

S = input().strip()
suffix = []
for i in range(len(S)):
    suffix.append(S[i:])
suffix.sort()
for word in suffix:
    print(word)