import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().strip().split()))
ops = list(map(int, input().strip().split()))

# 최댓값과 최솟값을 구하기 위해 초기값 설정
max_result = -int(1e9)
min_result = int(1e9)

def dfs(nums, index, current_result, plus, minus, multiply, divide):
    global max_result, min_result
    
    if index == len(nums):
        # 모든 숫자를 다 사용했으면 최댓값과 최솟값 갱신
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return
    
    if plus > 0:
        dfs(nums, index + 1, current_result + nums[index], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(nums, index + 1, current_result - nums[index], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(nums, index + 1, current_result * nums[index], plus, minus, multiply - 1, divide)
    if divide > 0:
        if current_result < 0:
            # 음수일 때의 나눗셈 처리
            dfs(nums, index + 1, -(-current_result // nums[index]), plus, minus, multiply, divide - 1)
        else:
            dfs(nums, index + 1, current_result // nums[index], plus, minus, multiply, divide - 1)



# 초기값은 첫 번째 숫자, index는 1부터 시작
dfs(nums, 1, nums[0], ops[0], ops[1], ops[2], ops[3])

print(max_result)
print(min_result)

'''
# 3달 전 풀이

# 입력받기
n = int(input()) # 수의 개수
nums = list(map(int, input().split())) # 수열
operator = list(map(int, input().split()))

# 최솟값, 최댓값 초기화
maxValue = int(-1e9)
minValue = int(1e9)

def calculator(idx, res, add, sub, prd, div):
    global minValue, maxValue

    if idx == n:
        # 최솟값과 최댓값 갱신
        maxValue = max(maxValue, res)
        minValue = min(minValue, res)
        return 
    
    if add > 0:
        calculator(idx + 1, res + nums[idx], add-1, sub, prd, div)

    if sub > 0:
        calculator(idx + 1, res - nums[idx], add, sub-1, prd, div)

    if prd > 0:
        calculator(idx + 1, res * nums[idx], add, sub, prd-1, div)

    if div > 0:
        calculator(idx + 1, int(res / nums[idx]), add, sub, prd, div-1)

calculator(1, nums[0], operator[0], operator[1], operator[2], operator[3])
print(maxValue)
print(minValue)
'''