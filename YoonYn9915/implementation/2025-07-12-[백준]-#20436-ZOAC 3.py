def coordinate(char):
    for i in range(3):
        if char in keyboard[i]:
            j = keyboard[i].index(char)
            return (i, j)


# 쿼터식 키보드 이중 배열
keyboard = [['z', 'x', 'c', 'v', 'b', 'n', 'm'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']]

l, r = map(str, input().split())
string = str(input())
# 입력된 문자 좌표로 바꾸기
now = [coordinate(l), coordinate(r)]
word = [coordinate(i) for i in string]

sum = 0
for char in word:
    if (char[0] == 0 and char[1] >= 4) or char[1] >= 5:  # 오른손으로 입력하는 경우
        sum += abs(now[1][0] - char[0]) + abs(now[1][1] - char[1]) + 1
        now[1] = char
    else:  # 왼손으로 입력하는 경우
        sum += abs(now[0][0] - char[0]) + abs(now[0][1] - char[1]) + 1
        now[0] = char
print(sum)