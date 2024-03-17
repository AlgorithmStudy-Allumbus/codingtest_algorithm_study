# 입력받기
n = int(input()) # 수의 개수
nums = list(map(int, input().split())) # 수열
operator = list(map(int, input().split())) # 연산자

# 최솟값, 최댓값 초기화
minValue= 1000000000
maxValue= -1000000000 

def calculator(idx, res, add, sub, prd, div):
    global minValue, maxValue

    if idx == n: # 종료조건: 연산자를 모두 사용했을 경우
        # 다 탐색했기 때문에 최대최소 비교해서 최솟값과 최댓값 갱신
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