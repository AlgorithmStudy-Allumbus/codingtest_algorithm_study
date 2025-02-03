import sys
input = sys.stdin.readline

# 0~9까지 숫자의 개수를 저장할 딕셔너리 초기화
dict = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
         5: 0, 6: 0, 7: 0, 8: 0, 9: 0
         }

# 방 번호 입력
room_nums = list(map(int, input().rstrip()))

# 숫자 개수 카운트
for num in room_nums:
    if num == 6 or num == 9:
        if dict[6] <= dict[9]:
            dict[6] += 1
        else:
            dict[9] += 1
    else:
        dict[num] += 1

# 가장 많이 필요한 세트 개수 찾기
answer = 0
for value in dict.values():
    answer = max(answer, value)

print(answer)
