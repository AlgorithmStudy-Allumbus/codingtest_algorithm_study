"""
https://www.programmers.co.kr/learn/courses/30/lessons/42746
"""

def solution(numbers):
    # 1. number의 같은 길이에 대해서 크기 비교하기
    numbers_str = [str(num) for num in numbers ] # 문자열로 변환
    numbers = sorted(numbers_str ,key = lambda x: x*3 , reverse = True )
    #2. 리스트 원소를 1개의 문자열로 출력 형식 충족하기
    # answer = "".join(numbers)
    # print(answer , type(answer))
    answer = str(int("".join(numbers)))
    # print(answer , type(answer))
    return answer