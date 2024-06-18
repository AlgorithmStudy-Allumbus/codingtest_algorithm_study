'''
타겟넘버 - 재귀를 이용한 DFS 풀이
'''

def solution(numbers, target):
    answer = 0
    n = len(numbers)

    # dfs를 위한 재귀함수
    def dfs(index, result):
        nonlocal answer # 바깥 함수의 변수를 사용하기 위해 nonlocal 키워드 사용

        if index == n:  # 모든 숫자를 다 사용한 경우, 현재 합이 target과 같은지 확인
            if result == target:
                answer += 1
            return
        else:
            # 현재 합에 다음 숫자를 더하거나 빼는 두 가지 경우로 dfs 함수 호출
            dfs(index+1, result+numbers[index]) # 더한 경우
            dfs(index+1, result-numbers[index]) # 뺀 경우

    dfs(0, 0) # 첫번째 인덱스와 초기합 0

    return answer

# 예제 1: 숫자 배열 [1, 1, 1, 1, 1]로 목표 값 3을 만드는 방법의 수
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))  # 결과: 5

# 예제 2: 숫자 배열 [4, 1, 2, 1]로 목표 값 4를 만드는 방법의 수
numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))  # 결과: 2