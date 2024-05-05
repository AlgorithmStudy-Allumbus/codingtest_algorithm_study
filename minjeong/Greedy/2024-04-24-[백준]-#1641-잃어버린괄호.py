nums = input()
nums_list = nums.split('-') # 1. 먼저 -를 기준으로 나눈다.

for i, n in enumerate(nums_list):
    num_plus = list(map(int, n.split('+'))) # 2. +를 기준으로 나눈 후, 리스트에 int로 바꿔 저장한다.
    # 저장형태: [55, [50, 50]]
    nums_list[i] = sum(num_plus) # 3. 바꾼 int형을 더한 값을 원래의 식이 있는 리스트에 저장한다.

result = nums_list[0]
for i in range(1, len(nums_list)): # 4. 나머지 값들을 - 연산한다.
    result -= nums_list[i]

print(result)