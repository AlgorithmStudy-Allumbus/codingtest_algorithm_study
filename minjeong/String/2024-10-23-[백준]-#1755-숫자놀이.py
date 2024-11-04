import sys

input = sys.stdin.readline

# 숫자 0부터 9까지의 영어 표현을 리스트에 저장
english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
answer = {}  # 결과를 저장할 딕셔너리 (key: 숫자, value: 영어 표현)

m, n = map(int, input().split())
nums = list(range(m, n + 1))  # m ~ n까지의 숫자 리스트

# 숫자를 영어로 변환하여 사전에 저장
for num in nums:
    temp = ""
    if num // 10 > 0:  # 십의 자리 숫자가 존재하는 경우
        temp += english[num // 10] + " "
    temp += english[num % 10]
    answer[num] = temp  # 딕셔너리에 추가

# 사전순으로 정렬 후 10개씩 출력
cnt = 0
for key, value in sorted(answer.items(), key=lambda x: x[1]):  # value 값을 기준으로 오름차순 정렬
    cnt += 1
    print(key, end=" ")
    if cnt == 10:  # 10개 출력할 때마다 줄바꿈
        print()
        cnt = 0