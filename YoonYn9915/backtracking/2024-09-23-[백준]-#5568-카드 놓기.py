n = int(input())
k = int(input())

card = []
dp = [0] * n

result = 0

for _ in range(n):
    card.append(int(input()))

string = ''
result = set()


def select(cnt):
    global string

    if cnt == k:
        result.add(string)
        return

    for i in range(n):
        if dp[i] == 0:
            dp[i] = 1

            tmp = str(card[i])
            string += tmp

            select(cnt + 1)

            dp[i] = 0
            string = string[:-len(tmp)]


select(0)
print(len(result))