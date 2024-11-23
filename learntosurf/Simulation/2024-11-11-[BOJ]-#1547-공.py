M = int(input())

cups = [1, 2, 3]
 
def change_cups(X, Y):
    x = cups.index(X)
    y = cups.index(Y)
    
    # cups 리스트에서 X번째와 Y번째 요소 교환
    cups[x], cups[y] = cups[y], cups[x]

for _ in range(M):
    X, Y = map(int, input().split())
    change_cups(X, Y)

print(cups[0])