def solution(num):
    answer = ''
    if num == 0 or num %2 ==0 : # even
        answer = "Even"
    elif num % 2 == 1 : # odd
        answer = "Odd"
    return answer