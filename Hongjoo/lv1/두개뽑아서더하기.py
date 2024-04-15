def solution(numbers):
    answer = []
    #pick 2 elements and sum
    for i in range(len(numbers)) : 
        for k in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[k])
    print(answer)
    #delete duple elements
    answer=list(set(answer))
    answer.sort()
    print(answer)
    return answer