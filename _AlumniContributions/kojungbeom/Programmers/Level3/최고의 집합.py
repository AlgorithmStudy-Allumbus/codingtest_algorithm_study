def solution(n, s):
    if n > s:
        return [-1]
    answer = [1] * n

    a, b = divmod(s, n)
    answer = [a]* n
    for i in range(b):
        answer[i % n] += 1

    #print(answer)
    answer.sort()
    return answer