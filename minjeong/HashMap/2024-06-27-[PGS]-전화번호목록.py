def solution(phone_book):
    # 전화번호부 phone_book을 집합(set())으로 변환하여 prefixes에 저장. 
    # 집합으로 저장하는 이유는 in 연산이 평균적으로 $O(1)$의 시간 복잡도를 가지고 있으므로 for 문 안에서 사용하더라도 효율적이기 때문
    prefixes = set(phone_book)
    
    for number in phone_book:
        for i in range(1, len(number)):
            # 각 전화번호 number에 대해, 길이가 1이상인 그 전화번호의 모든 접두어를 prefix에 반복하여 저장한다. 
            prefix = number[:i]
            # prefix가 prefixes에 존재하는지 확인한다.
            if prefix in prefixes:
                return False # 존재하면 바로 False
    return True # 모든 번호에 대해 접두어가 발견되지 않는다면 True 반환
