Tn = [i * (i+1) // 2 for i in range(1, 46)] 
eureka = [0] * 10001

for i in range(Tn):
    for j in range(Tn):
        for k in range(Tn):
            if i+j+k <= 1000:
                eureka[i+j+k] = 1

T = int(input())
for _ in range(T):
    print(eureka[int(input())])