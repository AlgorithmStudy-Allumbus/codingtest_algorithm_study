def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for k in range(i,len(numbers)): 
        # 1. n[i] < m 
            if numbers[i] < numbers[k]:
                answer.append(numbers[k])
                break
         # 2. nothing -> m= -1
            if k == len(numbers)-1: 
                answer.append(-1)
    return answer