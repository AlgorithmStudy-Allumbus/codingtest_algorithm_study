n = int(input())

for i in range(n):
    name = input().split()
    god = 'god' + ''.join(name[1:])
    print(god)