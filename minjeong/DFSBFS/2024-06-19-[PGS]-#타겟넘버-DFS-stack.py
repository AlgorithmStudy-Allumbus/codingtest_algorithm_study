'''
타겟넘버 - stack을 이용한 DFS 풀이
queue 풀이와 같은데 popleft -> pop, queue -> stack으로만 바꿔주면 됨
'''
def solution(numbers, target):
    answer = 0
    stack = []
    n = len(numbers)
    # 초기 상태를 스택에 추가. 시작 숫자에서 +와 - 두 가지 경우를 모두 추가 
    # (이때 인덱스값도 함께 추가) [값, 인덱스] (push)
    stack.append([numbers[0], 0])       # 첫 번째 숫자를 더한 경우
    stack.append([-1*numbers[0], 0])    # 첫 번째 숫자를 뺀 경우

    # 스택이 빌 때까지 반복
    while stack: 
        temp, index = stack.pop() # 스택에서 값을 꺼내서 현재 합과 인덱스 가져옴
        index += 1 # 다음 인덱스로 넘어감
        # 인덱스가 리스트의 길이보다 작다면,
        if index < n: 
            # 현재 합에 다음 숫자를 더하거나 빼는 두 가지 경우를 스택에 추가
            stack.append([temp + numbers[index], index])
            stack.append([temp - numbers[index], index])
        else: # 다 순회했다면 temp 값과 target값 비교
            if temp == target:
                answer += 1
    return answer

# 예제 1: 숫자 배열 [1, 1, 1, 1, 1]로 목표 값 3을 만드는 방법의 수
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))  # 결과: 5

# 예제 2: 숫자 배열 [4, 1, 2, 1]로 목표 값 4를 만드는 방법의 수
numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))  # 결과: 2