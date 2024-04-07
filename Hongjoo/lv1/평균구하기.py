def solution(arr):
    answer = 0

    for n in arr : 
        answer += n
    
    answer = answer/len(arr)
    print(answer)
    return answer