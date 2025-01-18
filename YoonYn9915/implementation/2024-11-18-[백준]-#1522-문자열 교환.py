'''
1. 문자열 입력받기
2. a의 개수만큼 윈도우 크기 가져간 후
3. 하나씩 옆으로 이동하면서 윈도우 안의 b가 가장 최소가 되는 순간을 구함
'''


def countB(str):
    cnt = 0
    for char in str:
        if char == 'b':
            cnt += 1

    return cnt


str = input()
cnt = 0

# 답 저장 변수
ans = int(1e9)

for char in str:
    if char == 'a':
        cnt += 1


# a의 개수만큼 문자열 순회하면서 윈도우 안의 b가 몇개인지 확인
for i in range(len(str)):
    # 원형을 고려하여 i + cnt 문자열의 길이를 넘어가면 앞에서 가져옴
    if i + cnt > len(str):
        tmp = str[i:]
        tmp2 = str[0: (i + cnt)-len(str)]
        b_cnt = countB(tmp + tmp2)
    else:
        tmp = str[i:i + cnt]
        b_cnt = countB(tmp)
    ans = min(ans, b_cnt)

print(ans)
